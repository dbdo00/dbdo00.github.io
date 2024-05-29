import os 
import re 
import utils

input_path = "mkd"
output_path = "output"

dir = os.listdir(input_path)
print(dir)

data = open("index.txt", 'r').read().splitlines()

class Entry:
    def __init__(self, name):
        self.name = name
        self.uri = self.uri()

    def uri(self):
        for line in data:
            if utils.is_comment(line): continue     
            current_name, current_title, current_uri = line.split(',')
            if current_name == self.name:
                return current_uri.strip()
    
    def title(self):
        for line in data:
            if utils.is_comment(line): continue     
            current_name, current_title, current_uri = line.split(',')
            if current_name == self.name:
                return current_title.strip()

a = Entry("page")
print(a.name, a.uri)

for i in dir:
    if i.endswith(".md"):
        # the parsed html content 
        print(f"parsing {i}...")
        parsed = os.popen(f"python parser.py {input_path}/{i}").read()
        # name of the markdown file without extension
        name = i.split('.md')[0] 
        entry = Entry(name)
        open(f"{output_path}/{entry.uri}.html", 'w').write(parsed)
        print(f"finished writing to {output_path}/{entry.uri}.html")


