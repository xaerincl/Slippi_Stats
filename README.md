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

It will generate a .csv in the same folder as the .py file named Slippi_stats.csv.

Here are the names of the columns and their meaning:

```
'date': date  
'duration [frames]': duration of the match in frames
'p1': name of player 1
'p1_code': code of player 1
'p1_char': character of player 1
'p2': name of player 2
'p2_code': code of player 2
'p2_char': character of player 2

'p1_stock1_death%' : Percentage player 1 had before losing the first stock
'p1_stock2_death%' : Percentage player 1 had before losing the second stock
'p1_stock3_death%' : Percentage player 1 had before losing the third stock
'p1_stock4_death%' : Percentage player 1 had before losing the last stock

'p1_stock1_killmove' : Move used by player 1 to finish the first stock of player 2
'p1_stock2_killmove' : Move used by player 1 to finish the second stock of player 2
'p1_stock3_killmove' : Move used by player 1 to finish the third stock of player 2
'p1_stock4_killmove' : Move used by player 1 to finish the last stock of player 2

'p2_stock1_death%' : Percentage player 2 had before losing the first stock
'p2_stock2_death%' : Percentage player 2 had before losing the first stock
'p2_stock3_death%' : Percentage player 2 had before losing the first stock
'p2_stock4_death%' : Percentage player 2 had before losing the first stock

'p2_stock1_killmove' : Move used by player 2 to finish the first stock of player 1
'p2_stock2_killmove' : Move used by player 2 to finish the first stock of player 1
'p2_stock3_killmove' : Move used by player 2 to finish the first stock of player 1
'p2_stock4_killmove' : Move used by player 2 to finish the first stock of player 1

'p1_damage_dealt': Total damage dealt by player 1 to player 2
'p2_damage_dealt': Total damage dealt by player 2 to player 1

'p1_frames_shield': Amount of frames in shiled by player 1
'p2_frames_shield': Amount of frames in shiled by player 2

'p1_frames_offstage': Amount of frames offstage by player 1
'p2_frames_offstage': Amount of frames offstage by player 2

'stage': stage,
'winner': Who won
'stock_dif': Stock difference at the end of the match
```



# Thanks to


- [The Slippi Team](https://slippi.gg/)
- [hohav](https://github.com/hohav/py-slippi)
- [kyle-swygert](https://github.com/kyle-swygert/slippi-file-rename)
