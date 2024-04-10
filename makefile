all:
	python build.py

serve:
	python serve.py

test:
	python blog.py
index:
	pandoc index.md -t html  -o .\public\index.html --template=.pandoc/index_template.html 
	
