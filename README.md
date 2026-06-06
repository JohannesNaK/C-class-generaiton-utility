This small script aims to allow more effortless code organization, primarily with Visual Studio.

There are two commands:

```bash
classgen c <module name> <file name>
classgen d <module name> <file name or *>
```


This creates directories specified in `<module name>` inside both `src` and `include`, then creates a `.cpp` and header file using `<file name>`.

Example:

```bash
classgen c graphics/player texture
```

would generate:

```text
src/
  graphics/
    player/
      texture.cpp
```

and:

```text
include/
  graphics/
    player/
      texture.h
```

The script also creates a basic class definition in the generated header file.

Removing a file is done with the delete command:

```bash
classgen d graphics/player texture
```

This removes:

```text
src/graphics/player/texture.cpp
include/graphics/player/texture.h
```

You can delete a folder and all of its contents with `*`:

```bash
classgen d graphics/player *
```

Result:

```text
src/
  graphics/

include/
  graphics/
```

Executing:

```bash
classgen d graphics *
```

would likewise remove `player` and its contents, but also the `graphics` directory.
