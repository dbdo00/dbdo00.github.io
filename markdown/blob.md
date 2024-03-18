---
title: git 里 file object 的使用
---


-
  ```
  git hash-object -w <FILENAME>
  ```

- 这是 文件blob hash。 不会因为该文件名而改变

- 用 这个hash 来看log

	- ` git log --find-object=`

- 参考：`git log --help`, [Git-Internals-Git-Object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)

