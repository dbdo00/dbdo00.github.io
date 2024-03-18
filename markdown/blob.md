---
title: git 里 file object 的使用
---


-
  ```
  git hash-object -w <FILENAME>
  ```

- 会打印文件Object id。这个 id 不会因为该文件名改变而改变

- 用 这个hash 来看log

	- ` git log --find-object=<object id>`

- 参考：`git log --help`, [Git-Internals-Git-Object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)

