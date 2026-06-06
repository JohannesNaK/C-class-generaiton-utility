This small script aims to allow a more effortless code organization, primarily with Visual Studio. There are two commands,
classgen c <module name> <file name>
will create directories specified in module to both src and include folders, and then a cpp and header file with file name. The script should work on any OS that supports
python. For sake of simplicty, the examples below assumes an operating system with / as a file delimeter.
Example:
classgen c graphics/player texture
would generate the following structure
src
  graphics
    player
        texture.cpp
and 
include
  graphics
    player
      texture.h
The script also creates a basic class definition in the generated header file

Removing a file is done by using the delete command:
classgen d graphics/player texture
Removes texture.cpp and texture.h.
You can delete a folder and all of its contents with *
classgen d graphics/player *
would result insrc
src
  graphics
and 
include
  graphics

Executing  classgen d graphics * would likewise remove player and its content but also graphics directory.
