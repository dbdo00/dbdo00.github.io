from livereload import shell, Server
from blog import *
file_hash = {}

def calculate_file_hash(file_path):
    return hash(open(file_path, 'rb').read())

def hash_same(file):
    current_hash = calculate_file_hash(file)
    if file_hash[file] == current_hash:
        return True
    else:
        file_hash[file] = current_hash
        return False

def updated( file):
    return not hash_same(file)

def build():
    import time
    start_time = time.time()
    render_html_for_each_post(
        
        template_name="post.html", 
        
        md_dir = markdown_dir, 
        
        post_dir=post_dir,
        updated=updated 
    )
    end_time = time.time()
    print(f"Build time: {end_time - start_time} seconds")

def execute(cmd: str):
    # execute a command
    os.system(cmd)

def run( ):
    server = Server()
    server.watch( 'markdown/*',
                build,
                 )
    server.serve(
        root = 'public'
        )


# calculate the initial hash
for file in os.listdir(markdown_dir):
    print(file)
    if file.endswith(".md"):
        filename = f'{markdown_dir}/{file}'
        file_hash[filename] = calculate_file_hash(filename)


run()
    




