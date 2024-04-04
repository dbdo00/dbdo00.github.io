all:
	python blog.py

serve:
	python serve.py

index:
	pandoc index.md -t html  -o .\public\index.html --template=.pandoc/index_template.html
	
