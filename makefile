all: blog.py 
	git rm -rf public/post --cache
	rm -rf public/post 
	git add markdown/*
	git commit -a -m "update"
	python build.py
	
serve: 
	python serve.py

test: blog.py 
	python blog.py

index: index.md .pandoc/*
	pandoc index.md -t html  -o ./public/index.html -o ./public/static/index.html --template=.pandoc/index_template.html --lua-filter=.pandoc/filter.lua 
	pandoc index_zh.md -t html  -o ./public/index_zh.html -o ./public/static/index_zh.html --template=.pandoc/index_template.html --lua-filter=.pandoc/filter.lua 


new: 
	

