import os
import time

exception = ["r.-3.-3.mca","r.-3.-2.mca","r.-3.-1.mca","r.-3.0.mca","r.-3.1.mca","r.-3.2.mca","r.-2.-3.mca","r.-2.-2.mca","r.-2.-1.mca","r.-2.0.mca","r.-2.1.mca","r.-2.2.mca","r.-1.-3.mca","r.-1.-2.mca","r.-1.-1.mca","r.-1.0.mca","r.-1.1.mca","r.-1.2.mca","r.0.-3.mca","r.0.-2.mca","r.0.-1.mca","r.0.0.mca","r.0.1.mca","r.0.2.mca","r.1.-3.mca","r.1.-2.mca","r.1.-1.mca","r.1.0.mca","r.1.1.mca","r.1.2.mca","r.2.-3.mca","r.2.-2.mca","r.2.-1.mca","r.2.0.mca","r.2.1.mca","r.2.2.mca"]
filelist = os.listdir('C:/Users/WinServ/Documents/IsisCraft (Bungeecord)/Servers/Main [1.16.5]/main_the_end/DIM1/region')
#this path does not require a final slash at the end
found = []
notfound = []

for directories in filelist:
    for value in exception:
        if value in directories:
            found.append(directories)


for files in filelist:
    if files in found:
        print(files + " found.")
    else:
        files.replace("'","")
        notfound.append(files)

if len(notfound) == 0:
    print("no files to delete...")
    exit()
else:
    print("getting ready to delete files...")

time.sleep(3)

for deletefile in notfound:
    print(deletefile + " deleted.")
    os.remove('C:/Users/WinServ/Documents/IsisCraft (Bungeecord)/Servers/Main [1.16.5]/main_the_end/DIM1/region/' + deletefile)
    #make sure to include a slash at the very end of the path for this one                                     ^^

    
