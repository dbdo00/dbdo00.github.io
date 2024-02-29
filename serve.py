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
        

def updated(file):
    return not hash_same(file)


def build():
    global old_markdown_dir
    import time
    start_time = time.time()
    # TODO. when templates are updated, all pages need to be rebuilt
    render_html_for_each_post(
        template_name="post.html", 
        
        md_dir = markdown_dir, 

        post_dir= post_dir,

        updated = updated   
    ) 
    # TODO. need a better condition for updating the index
    # visibility change
    # title change
    # etc... 
    # or just rebuild index in the background... how?
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

def build_exclusively():
    render_html_for_each_post(
         template_name="post.html", 
        md_dir = markdown_dir, 
        post_dir= post_dir,
    )
    
def run():
    server = Server()
    # TODO. incorporate template path into the glob patter
    server.watch( 'markdown/*',
                 build
     )
    
    server.watch(filepath='template/*', func = build_exclusively, ignore=None)
    
    server.serve(
        root = 'public'
    )

def main():
    # calculate the initial hash
    for file in os.listdir(markdown_dir):
        print(file)
        if file.endswith(".md"):
            filename = f'{markdown_dir}/{file}'
            file_hash[filename] = calculate_file_hash(filename)
    
    global old_markdown_dir
    old_markdown_dir = os.listdir(markdown_dir)
    # TODO. 
    # probably also update the index page on exit
    run()
    

    
if __name__ == "__main__":
    main()



