import os
import sys 
import datetime
arg = sys.argv[1]

def new_post(arg):
    """
    create a new post 
    blog new <post name>
    """
    
    date = datetime.datetime.date()
    
    header = f"""---
    title: {arg}
    date: 
    """
    
    with open(arg, 'w') as f:
        f.write(header)