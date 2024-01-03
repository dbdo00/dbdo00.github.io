all:
	git add *
	git commit -a -m "u"
	python blog.py

serve:
	python serve.py
