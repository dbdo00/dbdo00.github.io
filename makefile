all: blog.py 
	rm -r public/posts/*  || true
	git add markdown/*  
	git commit -a -m "rebuild with makefile" || true
	python build.py
	#git add public/posts/*
	
serve: 
	python serve.py

test: blog.py 
	python blog.py

index: 
	rm -r public/index.html public/styles || true
	cd Landing; make>/dev/null ; cp build/* ../public -r
	git add public/*


deploy:
	netlify deploy
	

style: 
	npx tailwindcss -i ./src/style-note-src.css -o ./src/style-note.css 
	cp ./src/style-note.css ./public/style-note.css
