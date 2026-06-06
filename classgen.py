import os
import sys
srcPath = "src"
includePath = "include"
path = os.path.realpath(__file__)

def obtainPath(type:str,args:[str]):
    return type+os.sep + args[0]+os.sep + args[1]
def create(target:str):
    print("target is " + target)
    if not os.sep in target:
        open(target, "x")   
    else:
        dirs = target.split(os.sep)
        file = dirs[len(dirs)-1]
        del dirs[len(dirs)-1]
        try:
            os.makedirs(os.sep.join(dirs))
        except FileExistsError:
            pass
        open(target, "x")
def main(args:[str]):
    #module <command> <module path> <file>
    if len(args) != 4:
        print("UNKNOWN ARGUMENTS: \n classgen <c/d> <module path> <file>")
        return
    fileArgs = [args[2],args[3]]
    cppPath =  obtainPath(srcPath,fileArgs) + ".cpp"
    hPath =  obtainPath(includePath,fileArgs) + ".h"
    if args[1].lower() == "c":
        try:
            create(cppPath)
            create(hPath)
        except FileExistsError:
            print("File " + str(fileArgs) + " already exists")
    elif args[1].lower() == "d":
        try:
            os.remove(cppPath)
            os.remove(hPath)
        except:
            print("File " + str(fileArgs) + " already exists")
    else:
        print("UNKNOWN COMMAND " + args )
if __name__ == "__main__":
    main(sys.argv)