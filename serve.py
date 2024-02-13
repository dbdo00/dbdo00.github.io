from livereload import shell, Server
from blog import *
file_hash = {}

def calculate_file_hash(file_path):
    return hash(open(file_path, 'rb').read())

def hash_same(file):
    current_hash = calculate_file_hash(file)
    try:
        if file_hash[file] == current_hash:
            return True
        else:
            file_hash[file] = current_hash
            return False
    except KeyError:
        # add the new file and its hash into the dictionary
        file_hash[file] = current_hash
        # build the new file
        return False
        

def updated( file):
    return not hash_same(file)


def build():
    global old_markdown_dir
    import time
    start_time = time.time()
    render_html_for_each_post(
        
        template_name="post.html", 
        
        md_dir = markdown_dir, 
        
        post_dir=post_dir,

        updated = updated
    ) 
    if len(os.listdir(markdown_dir)) != len(old_markdown_dir):
        old_markdown_dir = os.listdir(markdown_dir)
        print("index changed")
        execute('git add *')
        execute(f'git commit -a -m "{str(time.time())}"')
        update_data(md_dir=markdown_dir)
        render_index_page('./data.json', index_page_path)
    end_time = time.time()
    print(f"Build time: {end_time - start_time} seconds")

def execute(cmd: str):
    # execute a command
    os.system(cmd)

def run( ):
    server = Server()
    # TODO. incorporate template path into the glob patter
    server.watch( 'markdown/*',
                build
    )

    server.watch('template/*', build, ignore=None)
    
    server.serve(
        root = 'public'
    )


# calculate the initial hash
for file in os.listdir(markdown_dir):
    print(file)
    if file.endswith(".md"):
        filename = f'{markdown_dir}/{file}'
        file_hash[filename] = calculate_file_hash(filename)

old_markdown_dir: list[str] = os.listdir(markdown_dir)


# TODO. 
# probably also update the index page on exit

run()
    




