all:
	python blog.py

serve:
	python serve.py

index:
	pandoc index.md -t html -s --css="" -o .\public\index.html
	
