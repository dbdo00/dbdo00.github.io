all: style
	rm public/posts/* -r
	git add markdown/*  
	git commit -a -m "rebuild with makefile" || true
	python build.py
	#git add public/posts/*
	

publish:

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
	mkdir public/posts -p
	cp ./src/style-note.css ./public/posts/style-note.css
