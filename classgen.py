import os
import shutil
import sys
srcPath = "src"
includePath = "include"
path = os.path.realpath(__file__)

def obtainFilePath(type:str,args:[str]):
    return type+os.sep + args[0]+os.sep + args[1]
def obtainModPath(type:str, modName):
    return type+os.sep+modName
def create(target:str, content:str):
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
        with open(target, "w") as file:
            file.write(content)
def main(args:[str]):
    #module <command> <module path> <file>
    if len(args) != 4:
        print("UNKNOWN ARGUMENTS: \n classgen <c/d> <module path> <file>")
        return
    fileArgs = [args[2],args[3]]
    cppPath =  obtainFilePath(srcPath,fileArgs) + ".cpp"
    hPath =  obtainFilePath(includePath,fileArgs) + ".h"
    if args[1].lower() == "c":
        try:
            name = fileArgs[1][0].upper() + fileArgs[1][1:].lower()
            capName = name.upper()
            create(cppPath,"#include \"" + name + "\"\n")
            create(hPath,"#ifndef " + capName +  "_H\n#define " + capName + "_H\n"
                   + "\n"*4+"class " + name +"{"+"\n"*4+"};"+"\n"*4 + "#endif")
        except FileExistsError:
            print("File " + str(fileArgs) + " already exists")
    elif args[1].lower() == "d":
        if fileArgs[1] == "*":
            shutil.rmtree(obtainModPath(srcPath,fileArgs[0]))
            shutil.rmtree(obtainModPath(includePath,fileArgs[0]))
            return  
        try:
            os.remove(cppPath)
            os.remove(hPath)
        except:
            print("File " + str(fileArgs) + " already exists")
    else:
        print("UNKNOWN COMMAND " + args )
if __name__ == "__main__":
    main(sys.argv)