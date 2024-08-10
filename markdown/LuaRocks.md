---
title: LuaRocks
---
## What is LuaRocks
LuaRocks is the package manager for Lua. You can install  lua modules with it. 

As people often say, to write Lua, you need to eat C as breakfast. 

LuaRocks manages the installation process for Lua modules, including the complex tasks associated with C modules, such as handling makefiles and interacting with C compilers. By automating these tasks, LuaRocks simplifies the installation process and reduces the hassle.
## Building Module `lua-cjson` With LuaRocks 

1. ### Download the source file 
Go to <https://kyne.au/%7Emark/software/lua-cjson.php> and click `lua-cjson-x.y.z.zip` to download. 
![](<Pasted image 20240809234324.png>)
2. ### Build from the source
First, uncompress the zip file. Use the command
`unzip lua-cjson-2.1.0.zip`. 
Then enter the directory:
```sh
cd lua-cjson-2.1.0
```
Install the module globally:
```sh
sudo luarock make
```
If you want to specify the version of lua, say lua5.3, use:
```sh
sudo luarock-5.3 make
```
instead. 

