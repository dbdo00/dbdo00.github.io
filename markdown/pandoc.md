---
title: pandoc
publish: draft
---

模板里有标题时，输出也不包含标题: `-V title:""`

在 subrocess 里面用要注意 
```python
flags=['--mathml','-V','title:']
```
而不是`'title:""'`. 否则pandoc 会把标题都当成两个引号"".

完整写法是:
```python
pandoc_process = subprocess.Popen(['pandoc', flags,'--template=web_blank_pandoctemp.html'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = pandoc_process.communicate(input=content)
```

## 多文件输出

<https://github.com/jgm/pandoc/issues/6122>
#pandoc  支持多个文件输出 (一个标题下内容是一个文件）。输出文件类型选项是 -t chunkedhtml

使用例子: 
<https://github.com/jgm/pandoc/issues/6122#issuecomment-1377891056>

如果是旧版本，也可以输出成 epub 之后解压。解压以后，`EPUB/text` 文件夹下面是每个标题下内容（包含标题）的 xhtml 输出。
