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

