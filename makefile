all:
	git add *
	git commit -a -m "auto update"
	python blog.py

serve:
	python serve.py

	
