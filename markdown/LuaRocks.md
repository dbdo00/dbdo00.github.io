---
title: LuaRocks
---

LuaRocks is the package manager for Lua. You can install  lua modules with it. 

As people often say, to write Lua, you need to eat C as breakfast. 

LuaRocks makes things mildly easier by automating the intimidating process of globally install modules, especially those C modules which involves dynamic linking. 

## Building Module `lua-cjson` With LuaRocks 

1. ### Download the source file 
Go to <https://kyne.au/%7Emark/software/lua-cjson.php> and click `lua-cjson-x.y.z.zip` to download. 
![Pasted image 20240809234324.png]
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

