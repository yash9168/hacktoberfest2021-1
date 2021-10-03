import os
import shutil
import sys

def GetAllFile():
    list_dir = os.listdir()
    return list_dir

def MoveFile(data):
    if os.path.isdir(data) or data == sys.argv[0]:
        return
    else:
        SplitName = data.split(".")
        if len(SplitName) == 0:
            shutil.move(src=data,dst="OTHER FILE")
            return
        EXT = SplitName[len(SplitName)-1]
        if not os.path.exists(f"{EXT.upper()} FILE"):
            os.makedirs(f"{EXT.upper()} FILE")
        shutil.move(src=data,dst=f"{EXT.upper()} FILE")

All = GetAllFile()
for i in All:
    try:
        MoveFile(i)
    except PermissionError:
        pass
    except shutil.Error as e:
        print(e)
