from slippi import Game
import os
import time
import pandas as pd 
import argparse


"""
TO DO:

Daño por laser
Laser tirados

"""
def is_offstage(position,stage):
	stage_limits = {'BATTLEFIELD': 71.307,
					'FINAL_DESTINATION': 88.473,
					'DREAM_LAND_N64': 80.179,
					'POKEMON_STADIUM': 90.657,
					'FOUNTAIN_OF_DREAMS': 66.255,
					'YOSHIS_STORY': 58.907
					}


	#print(f'stage {stage}  and x_position of player {position}')
	#print(f'limits of the current stage {stage}')
	#print(stage_limits[stage])
	x_pos = float(position.split(',')[0][1:])
	if abs(x_pos) > float(stage_limits[stage]):
		return 1
	else:
		return 0



def winner(s1, s2, p1, p2, c1, c2):
	"""
	Return winner of the match
	"""
	if s1 > s2:
		return c1
	elif s1 < s2:
		return c2
	else:
		#return 'LRASTART or timeout'
		if c1<c2:
			return c1
		else:
			return c2

def search_kills(frames, stage):
	"""
	find kill frames
	"""

	"""with open('frames.txt', 'w') as f:
					for item in frames:
						f.write("%s\n" % item)"""


	death_frames_p1 = []
	death_percent_p1 = [None, None, None, None]
	kill_move_p1 = [None, None, None, None]
	death_frames_p2 = []
	death_percent_p2 = [None, None, None, None]
	kill_move_p2 = [None, None, None, None]

	p1_shield = 0
	p2_shield = 0

	curr_stock_p1 = 0
	curr_stock_p2 = 0

	p1_offstage = 0
	p2_offstage = 0

	for i,j in enumerate(frames):

		if 'DEAD' in str(j.ports[0].leader.post.state):
			if 'DEAD' not in str(frames[i-1].ports[0].leader.post.state):
				death_frames_p1.append(i)
				death_percent_p1[curr_stock_p1] = int(j.ports[0].leader.post.damage)
				kill_move_p2[curr_stock_p1] = str(j.ports[1].leader.post.last_attack_landed).split('.')[-1]
				curr_stock_p1 += 1

		if 'DEAD' in str(j.ports[1].leader.post.state):
			if 'DEAD' not in str(frames[i-1].ports[1].leader.post.state):
				death_frames_p2.append(i)

				death_percent_p2[curr_stock_p2] = int(j.ports[1].leader.post.damage)
				kill_move_p1[curr_stock_p2] = str(j.ports[0].leader.post.last_attack_landed).split('.')[-1]
				curr_stock_p2 += 1

		if 'GUARD' in str(j.ports[0].leader.post.state):
			p1_shield +=1

		if 'GUARD' in str(j.ports[1].leader.post.state):
			p2_shield +=1

		p1_offstage += is_offstage(str(j.ports[0].leader.post.position), stage)
		p2_offstage += is_offstage(str(j.ports[1].leader.post.position), stage)




	end_percent_1 = frames[-1].ports[0].leader.post.damage
	end_percent_2 = frames[-1].ports[1].leader.post.damage

	#print(f'Porcentaje muerte p1: {death_percent_p1}')
	#print(f'Porcentaje muerte p2: {death_percent_p2}')

	#print(f'Porcentaje final p1: {end_percent_1}')
	#print(f'Porcentaje final p2: {end_percent_2}')

	total_damage_dealt_p1 = 0
	total_damage_dealt_p2 = 0

	for dmg in death_percent_p2:
		if dmg != None:
			total_damage_dealt_p1 += dmg

	for dmg in death_percent_p1:
		if dmg != None:
			total_damage_dealt_p2 += dmg

	if None in death_percent_p1:
		total_damage_dealt_p2 += end_percent_1
	if None in death_percent_p2:
		total_damage_dealt_p1 += end_percent_2


	#print(f'Daño total hecho por p1: {total_damage_dealt_p1}')
	#print(f'Daño total hecho por p2: {total_damage_dealt_p2}')

	#print(f'frames en el escudo: {p1_shield}')
	#print(f'frames en el escudo: {p2_shield}')



	return death_percent_p1, death_percent_p2, kill_move_p1, kill_move_p2, int(total_damage_dealt_p1), int(total_damage_dealt_p2), p1_shield, p2_shield, p1_offstage, p2_offstage



def main(folder):

	files = os.listdir(folder)

	data = []

	start_time = time.time()
	for file in files:

		slippi_file = os.path.join(folder,file)
		replay = Game(slippi_file)

		#print(dir(replay))
		#print(replay.frames[-1])

		if replay.start.is_teams:
			# only count singles 1v1
			continue 

		if replay.metadata.duration <= 1800:
			# filter games with less than 1800 frames (30 sec)
			continue

		duration = int(replay.metadata.duration)

		date = replay.metadata.date

		player_1 = replay.metadata.players[0].netplay.name
		player_2 = replay.metadata.players[1].netplay.name

		character_1 = str(list(replay.metadata.players[0].characters.keys())[0]).split('.')[1] 
		character_2 = str(list(replay.metadata.players[1].characters.keys())[0]).split('.')[1]

		code_1 = replay.metadata.players[0].netplay.code
		code_2 = replay.metadata.players[1].netplay.code

		stocks_1 = replay.frames[-1].ports[0].leader.post.stocks
		stocks_2 = replay.frames[-1].ports[1].leader.post.stocks

		percent_1 = replay.frames[-1].ports[0].leader.post.damage
		percent_2 = replay.frames[-1].ports[1].leader.post.damage

		vict_player = winner(stocks_1, stocks_2, percent_1, percent_2, code_1, code_2)

		stage = str(replay.start.stage).split('.')[1]

		stock_dif = abs(int(stocks_1)-int(stocks_2))

		death_percent_p1, death_percent_p2, kill_move_p1, kill_move_p2, total_damage_dealt_p1, total_damage_dealt_p2, p1_shield, p2_shield, p1_offstage, p2_offstage = search_kills(replay.frames, stage)

		match_dict = {'date': date,  
					'duration [frames]': duration,
					'player_1': player_1, 
					'code_1': code_1, 
					'character_1': character_1, 
					'player_2': player_2, 
					'code_2': code_2, 
					'character_2': character_2, 

					'death%_stock1_player1' : death_percent_p1[0],
					'death%_stock2_player1' : death_percent_p1[1],
					'death%_stock3_player1' : death_percent_p1[2],
					'death%_stock4_player1' : death_percent_p1[3],

					'kill_move_1_player1' : kill_move_p1[0],
					'kill_move_2_player1' : kill_move_p1[1],
					'kill_move_3_player1' : kill_move_p1[2],
					'kill_move_4_player1' : kill_move_p1[3],

					'death%_stock1_player2' : death_percent_p2[0],
					'death%_stock2_player2' : death_percent_p2[1],
					'death%_stock3_player2' : death_percent_p2[2],
					'death%_stock4_player2' : death_percent_p2[3],

					'kill_move_1_player2' : kill_move_p2[0],
					'kill_move_2_player2' : kill_move_p2[1],
					'kill_move_3_player2' : kill_move_p2[2],
					'kill_move_4_player2' : kill_move_p2[3],

					'total_damage_dealt_by_p1': total_damage_dealt_p1,
					'total_damage_dealt_by_p2': total_damage_dealt_p2,

					'frames_shield_p1': p1_shield,
					'frames_shield_p2': p2_shield,

					'frames_offstage_p1': p1_offstage,
					'frames_offstage_p2': p2_offstage,

					'stage': stage, 'winner': vict_player, 'stock_dif': stock_dif}

		print(match_dict)
		data.append(match_dict)


	print("--- %s seconds ---" % (time.time() - start_time))

	df = pd.DataFrame(data)
	df.to_csv('Slippi_stats.csv', index=False)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='''Slippi stats .csv''')
	parser.add_argument('-folder', '-f',  type=str, required=True, help='Path to slippi .slp folder')
	args = parser.parse_args()
	main(args.folder)