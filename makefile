all: blog.py 
	rm -rf public/posts/*  || true
	git add markdown/*  
	git commit -a -m "rebuild with makefile" || true
	python build.py
	git add public/posts/*
	
serve: 
	python serve.py

test: blog.py 
	python blog.py

index: index.md .pandoc/*
	cd Landing; make; cp build ../public -r


deploy:
	netlify deploy
	

style: 
	npx tailwindcss -i ./src/style-note-src.css -o ./src/style-note.css 
	cp ./src/style-note.css ./public/style-note.css
