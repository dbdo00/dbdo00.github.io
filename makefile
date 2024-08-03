all: blog.py 
	rm -rf public/post/*  || true
	git add markdown/*  
	git commit -a -m "rebuild with makefile" || true
	python build.py
	
serve: 
	python serve.py

test: blog.py 
	python blog.py

index: index.md .pandoc/*
	pandoc index.md -t html  -o ./public/index.html -o ./public/static/index.html --template=.pandoc/index_template.html --lua-filter=.pandoc/filter.lua 
	pandoc index_zh.md -t html  -o ./public/index_zh.html -o ./public/static/index_zh.html --template=.pandoc/index_template.html --lua-filter=.pandoc/filter.lua 


deploy:
	netlify deploy
	

style: 
	npx tailwindcss -i ./src/style-note-src.css -o ./src/style-note.css 
	cp ./src/style-note.css ./public/style-note.css
