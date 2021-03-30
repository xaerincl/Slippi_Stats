# Slippi_Stats
![https://github.com/kyle-swygert/slippi-file-rename/blob/391be3491fa179f2da384255efcadcc75e7398c9/slippi-logo.png](https://github.com/kyle-swygert/slippi-file-rename/blob/391be3491fa179f2da384255efcadcc75e7398c9/slippi-logo.png)

# Installation
Requires Python >= 3.7. 

It needs both py-slippi and pandas, install by:

```
$ pip install py-slippi
$ pip install pandas
```


# Usage

```
$ python slippi_csv.py -folder <path to your replay folder>
```

It can be a relative path or full path. For example if you place the .py file inside the Documents folder (assuming that the Slippi folder with the replays is indeed inside the Documents folder), you can just run:

```
$ python slippi_csv.py -folder Slippi
```

Be aware that games with less than 1800 frames (30 sec) and games not played in tournament legal stages will not be included in the csv. Edit line 148 and line 175 if you want to change that.




# Output

It will generate a .csv in the same folder as the .py file named Slippi_stats.csv

```

'date': date  
'duration [frames]': duration
'p1': player_1 
'p1_code': code_1
'p1_char': character_1
'p2': player_2
'p2_code': code_2
'p2_char': character_2

'p1_stock1_death%' : death_percent_p1[0]
'p1_stock2_death%' : death_percent_p1[1]
'p1_stock3_death%' : death_percent_p1[2]
'p1_stock4_death%' : death_percent_p1[3]

'p1_stock1_killmove' : kill_move_p1[0]
'p1_stock2_killmove' : kill_move_p1[1]
'p1_stock3_killmove' : kill_move_p1[2]
'p1_stock4_killmove' : kill_move_p1[3]

'p2_stock1_death%' : death_percent_p2[0]
'p2_stock2_death%' : death_percent_p2[1]
'p2_stock3_death%' : death_percent_p2[2]
'p2_stock4_death%' : death_percent_p2[3]

'p2_stock1_killmove' : kill_move_p2[0]
'p2_stock2_killmove' : kill_move_p2[1]
'p2_stock3_killmove' : kill_move_p2[2]
'p2_stock4_killmove' : kill_move_p2[3]

'p1_damage_dealt': total_damage_dealt_p1
'p2_damage_dealt': total_damage_dealt_p2

'p1_frames_shield': p1_shield
'p2_frames_shield': p2_shield

'p1_frames_offstage': p1_offstage
'p2_frames_offstage': p2_offstage

'stage': stage,
'winner': vict_player
'stock_dif': stock_dif

```



# Thanks to


- [The Slippi Team](https://slippi.gg/)
- [hohav](https://github.com/hohav/py-slippi)
- [kyle-swygert](https://github.com/kyle-swygert/slippi-file-rename)
