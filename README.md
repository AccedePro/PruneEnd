# PruneEnd
Just a simple Python script to automatically delete end region files. This works on Minecraft Java Edition Version 1.14-1.16.*

This script deletes all region files that contain the outer end islands and is designed for survival servers where regeneration is neccessary for all players to access good loot. It is intended for use on a fairly large survival server that runs 24/7, as it is to automate the resetting of the end dimension's outer islands. 

Xisumavoid covered this technique in one of his videos:
https://www.youtube.com/watch?v=fGlqDBcgmIc

This is a lightweight program that automates the deletion process and can be used along with my EndSMPTweaks plugin to provide a fair experience to all players.

Before running the script using the included batch file, make sure to check for a few things:

1. The directories in the python code point towards the server's end region folder
2. The batch file points towards your python.exe file (usually in your AppData-Local directory)
3. The batch file also points towards where the python script is located on your PC
