
These python scripts will take a bunch of files from an online repo (say a diagnostics package for an Earth system model, but in principle it is not necessarily that restrictive) and organize them into a long ppt file, through which one can 'flick' to easily process the differences between the different runs.

There are two scripts.
1) PPE_output_ppt_organizer.py
2) generate_marp_from_directories.py

PPE_output_ppt_organizer.py is the user interface, where one defines
- the path to the folder with the images in
- the names of the directories within that one wishes to use
- a list of variables/filenames to plot
- a path to where you want the resulting ppt file to go

The other file is the workhorse script which creates a markdown file and then converts that into a ppt file. 