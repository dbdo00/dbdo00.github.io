from jinja2 import Environment, FileSystemLoader
import os
import json 
import codecs
import markdown
import sys 
import time
import latex2mathml.converter as latex_to_mathml
import subprocess

def render_html(template_name,content):    
    # template_name : the complete path of the template file  
    # content : the string of the markdown file
    # post_dir : the directory of the generated html files

    # render html for each post
    # env = Environment(loader= FileSystemLoader('./template'))
    template = Environment(loader= FileSystemLoader('./template')).get_template('post.html')

    # get title and tags from the markdown file
    try:
        title = get_title(content)
        tags = get_tags(content)
    except ValueError:
        print('Error in getting title or tags') 
        return ValueError
    # convert markdown to html
    paragraphs_html = markdown.markdown(content)

    # data for rendering the template
    data = {
        'title': title,
        'tags': tags,
        'header': 'title',
        # content is rendered using markdown converter
        'paragraphs': paragraphs_html
    } 
    # 渲染模板并生成静态页面
    output = template.render(data)
    
    return output
def write_html(output, post_dir, title):
    # output : the rendered html
    # post_dir : the directory of the generated html files
    # title : the title of the post

    # write the rendered html to a file
    with open(f'{post_dir}/{title}.html', 'w', encoding ='utf-8' ) as file:
        file.write(output)

def get_title(content): 
    # content : the string of the markdown file
    # 从content中获取title
    # content is a markdown file
     
    # read the first line of the markdown string "content"
    first_line = content.split('\n')[0] 
    #   去掉开头的 "tags:" 但如果标题中有 "tags:" 就会出错
    
    if first_line.replace(" ","").startswith('title:'):
        title = first_line.split('title:')[1].strip()
        if 'title:' not in title:
            return title 
        else:   
            # when the title contains 'title:', generate the title using the precise time of the markdown file
            # the title is in the form of 'title-2020-01-01-00-00-00'
            return f'title-{os.path.getmtime(content)}'

# test get_title
# print('below are titles and tags for the test post')

# print(get_title('markdown/mdtest.md'))

def get_tags(content):
    # 从content中获取tags
    # content is a string of markdown file
    # tags are specified after a line of 'tags:', seperated by ','
    # tags are in the form of 'tag1, tag2, tag3'

# find the line starting with 'tags:' in the string of markdown file "content"
    for line in content.split('\n'):
        if line.startswith('tags:'):
            tags = line[5:].strip() # remove the leading and trailing spaces
            return [tag.strip() for tag in tags.split(',')] # return the stripped tags as a list
                    
def file_ctime(filename):
    # filename : the precise path of a file
    # return the creation time of the file
    # the format is year-month-day-hour-minute-second
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(os.path.getmtime(filename))) 

def get_file_last_modified_date(file_path):
    try:
        # 运行 git log 命令获取文件的最后修改日期
        command = ["git", "log", "-1", "%Y-%m-%d %H:%M", file_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        modified_date = result.stdout.strip().split('\n')
        for line in modified_date:
            if line.startswith('Date:'):
                date = line.split('Date:')[1].strip()        
        return date
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None
    
# update data for each post
def update_data(md_dir):
    # md_dir : the directory of markdown files
    # return a list of dictionaries, each dictionary is the data for a post
    # save the list of dictionaries to a json file

    data = [] 
    for md in os.listdir(md_dir): 
        if md.endswith('.md'):
            markdown_content = text_file_to_string(f'{md_dir}/{md}')
            title = name_a_file(f'{md_dir}/{md}') 
            html_filename = f'{title}.html'  
            print("MAKE SURE THAT:")
            print('The current post directory is `post`')
            print('The current markdown directory is `markdown`')
            
            file_data={ 
                'title': title,
                'tags': get_tags(markdown_content),
                # concatenate the directory to specify the path of markdown and html files 
                'html_path' : f"post/{html_filename}",
                'md_path' : f"markdown/{md}", 
                'ctime' : file_ctime(f'{md_dir}/{md}')
            }
            data.append(file_data)
    
    # save data to a json file
    with open('data.json', 'w') as file:
        json.dump(data, file)

# test update_data
# update_data('.')

def text_file_to_string(filename):
    # filename : a text file's precise path
    # return the string of the text file
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read() 

def name_a_file(filename):
    # filename : the precise path of a file
    # return the name of the file without the extension
    markdown_content = text_file_to_string(filename)

    if get_title(markdown_content) == None:
                # when the title is not specified, generate the title using the precise time of the markdown file
                # the title is in the form of 'title-2020-01-01-00-00-00'
                title = get_file_last_modified_date(filename)
    else: 
        title = get_title(markdown_content)
    return title

# print(name_a_file('markdown/readme.md'))

# render html for each post
def render_html_for_each_post(md_dir, post_dir):
    # md_dir : the directory of markdown files
    # render html for each post
    for md in os.listdir(md_dir): 
        # print(md,'is passed to render_html_for_each_post')
        # put markdown file into a string 
        markdown_content = text_file_to_string(f'{md_dir}/{md}')
        output = render_html('post.html', markdown_content)  
        # write the rendered html to a file
        write_html(output, post_dir,  name_a_file(f'{md_dir}/{md}'))

# render data for index page to a list of links to each post 
# written in markown 

def render_index_page(data_json, index_page_path):
    
    # data_json : the json file containing data for each post
    # render a markdown file for index page
    # each post is a link to the post
    
    # the link in the markdown file is the form "[title](html_path)"
    
    with open(data_json, 'r') as file:
        data = json.load(file)
        # the link in the json file is the form "html_path": "/post/mdtest.html"
        # the link in the markdown file is the form "[title](html_path)"

        # order the posts by the creation time of the markdown file
        try:
            posts = sorted(data, key=lambda x: x['ctime'], reverse=True)
        except KeyError:
            print('KeyError in sorting data.We will skip this time.')
            pass 

        # print(type(posts[1]))
        # change the dates in the format in chinese
        for post in posts:
            post['ctime'] = post['ctime'][:11].replace('-', '年', 1).replace('-', '月', 1).replace('-', '日', 1) 

        # create the index page using jinja2 from the data in the json file 
        print("posts contain: ", posts)
        template = Environment(loader= FileSystemLoader('./template')).get_template('index.html')
        output = template.render(posts=posts)
        # write the rendered html to a file
        with open(f'{index_page_path}', 'w', encoding='utf-8') as file:
            file.write(output)

def main():
    # root : the root directory of the blog
    root_dir = os.getcwd()
    markdown_dir = f'{root_dir}/markdown'
    template_dir = f'{root_dir}/template'
    post_dir = f'{root_dir}/public/post' 
    index_page_path = f'{root_dir}/public/index.html'
    # render html for each post
    update_data(md_dir=markdown_dir)
    render_html_for_each_post(md_dir = markdown_dir, post_dir=post_dir)
    
    # render index markdown 
    render_index_page(f'{root_dir}/data.json',index_page_path=index_page_path)
    # put index markdown into a string
    # index_md = text_file_to_string(f'{markdown_dir}/index.md')
    # render html for index page's markdown 
    # output = render_html(template_name=f'{template_dir}/index.html', content=index_md )   
    # write the rendered html to a file
    # write_html(output, root_dir, 'index')

if __name__ == '__main__':
    main()
    # if --debug is specified, open a http server to view the generated html
    try: 
        if sys.argv[1] == '--debug':
            os.system('python -m http.server 5051')
    except IndexError:
        pass


        

