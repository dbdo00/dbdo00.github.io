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


已经两个月了！  
Rime 输入法又坏了。  
我把 vim 中的领导键设置为 `' '`。我发现它比默认的 `\` 更容易按。所以我现在有点高兴了。还设置了 [^2]


```lua
vim.g.mapleader = " "
vim.api.nvim_set_keymap("n", "<Leader>w", "<C-w>", { noremap = true })
```


[^2]：问题是 vimwiki 已经有了很多使用领导键的绑定键。例如，在 vimwiki 中，我不能用 `<Leader>wn` 水平分割窗口，因为这个组合键与 "打开维基页面 "绑定。 



### 2024-1-12


在想评论功能怎么做。放netlify上，一些数据库的基础。需要不需要评论？  
想试验一些网页编辑，比如支持org，通过已有的 org 的 wasm 实现。

### 2023-12-18

上次更新这个页面已经是两个多月以前了。  



