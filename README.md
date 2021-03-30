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


# Thanks to


- [The Slippi Team](https://slippi.gg/)
- [hohav](https://github.com/hohav/py-slippi)
- [kyle-swygert](https://github.com/kyle-swygert/slippi-file-rename)
