all: blog.py 
	python build.py
	
serve: 
	python serve.py

test: blog.py 
	python blog.py

index: index.md .pandoc/*
	pandoc index.md -t html  -o ./public/index.html --template=.pandoc/index_template.html --lua-filter=.pandoc/filter.lua 
