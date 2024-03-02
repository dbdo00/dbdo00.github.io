---
title: about
publish : unlisted
---



## 近况 

### 2024-3-1  

It's been two months!   
Rime input method is broken again.   
I set the leader key in vim as `' '`. I find it much easier to press than the default `\`. So I feel a bit happy now. and also set [^1]

[^1]: a problem is vimwiki already had a many keybindins using leader key. So my new keybinding is overwritten by vimwiki's. for instance, with vimwiki I cannot split the window horizontally with `<Leader>wn` because this key combination is bind to "opening a wiki page".  

```lua
vim.g.mapleader = " "
vim.api.nvim_set_keymap("n", "<Leader>w", "<C-w>", { noremap = true })
```



### 2024-1-12


在想评论功能怎么做。放netlify上，一些数据库的基础。需要不需要评论？  
想试验一些网页编辑，比如支持org，通过已有的 org 的 wasm 实现。

### 2023-12-18

上次更新这个页面已经是两个多月以前了。  



