import splitfolders # or import splitfolders
input_folder = "/Users/saimkhalid/Desktop/Random Shuffling/TB_Chest_Radiography_Database/input"
output = "/Users/saimkhalid/Desktop/Random Shuffling/Splited_data_v2" #where you want the split datasets saved. one will be created if it does not exist or none is set

splitfolders.ratio(input_folder, output=output, seed=1337, ratio=(.7, .1, .2)) # ratio of split are in order of train/val/test. You can change to whatever you want. For train/val sets only, you could do .75, .25 for example.