
import os
import sys
import json
from datetime import datetime
from subprocess import call

action = sys.argv[1]
config = open('list.json')
data = json.load(config)
if (action == "backup"):
    for file in data:
        command = "cp " + file[0] + " " + "./" +file[1]
        call(command, shell = True)
elif (action == "restore"):
    for file in data:
        command = "cp " + "./" + file[1] + " " + file[0]
        call(command, shell = True)
elif (action == "push"):
    for file in data:
        command = "cp " + file[0] + " " + "./" +file[1]
        call(command, shell = True)
    call("git add .", shell = True)
    call("git commit -m '"+str(datetime.now())+"' ", shell = True)
    call("git push origin master", shell = True)
