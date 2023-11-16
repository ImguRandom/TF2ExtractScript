# TF2ExtractScript
Python extraction script for a package of old Team Fortress 2 builds from 2007 - 2013.

**The purpose of this repo is just to hold the extraction script as I am currently intending to rewrite the script to be more user friendly. I'll still document its current usage below in this readme, though the instructions will change over time with the changes I make.**

This readme is in a shit state but I will rework it slowly.

[Package downloads, as well as downloads for the extraction script, diff lists and version identifying lists can be found here.](https://drive.google.com/drive/folders/1GsAevCvOEIL3Mfkwz4IsZXUII92wBQjT)

Download everything in there, and extract it all to a folder somewhere. That will be your new workspace for working with these packages.

To use the extraction script, first install Python on your machine. Then open a Terminal window or a PowerShell window in the folder and run commands such as:

`python example_extract.py tf2 441 20`

Optionally you can also specify a certain file path and file to extract from a specified manifest and depot.

`python example_extract.py tf2 441 126 tf/scripts/items/items_game.txt`

Todo: show all command args, explain what the numbers in the commands mean, explain link between 2nd number (3rd arg) and the specific build version.

