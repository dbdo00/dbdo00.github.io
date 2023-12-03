from jinja2 import Environment, FileSystemLoader
import os
import json 
import markdown
from markdown.preprocessors import Preprocessor
import sys 
import subprocess
import re
from datetime import datetime
import pytz
import subprocess
import yaml
from ignore_section import IgnoreSectionExtension
# markdown preprocessor that ignore that yaml metadata

def pandoc(content:str, flags:list) -> str:
   
        
    template = """
$if(title)$
<header id="title-block-header">
<h1 class="title">$title$</h1>
</header>
$endif$


$if(toc)$
<nav id="TOC">
    $toc$
</nav>
$endif$
$body$

"""
    with open("web_blank_pandoctemp.html", "w") as f:
        f.write(template)


    pandoc_process = subprocess.Popen(['pandoc', *flags,'--template=web_blank_pandoctemp.html'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = pandoc_process.communicate(input=content)

    # delete template file
    os.remove("web_blank_pandoctemp.html")
    
    return stdout 

def render_html(template_name,content):        
    # template_name : the complete path of the template file  
    # content : the string of the markdown file
    # post_dir : the directory of the generated html files

    # render html for each post
    # env = Environment(loader= FileSystemLoader('./template'))
    template = Environment(loader= FileSystemLoader('./template')).get_template(template_name) 

    # get title and tags from the markdown file
    try:
        title = get_title(content)
        # print("title:", title)
        tags = get_tags(content)
    except ValueError:
        print('Error in getting title or tags') 
        return ValueError
    # convert markdown to html
   
    paragraphs_html = pandoc(content, ['--mathml', '--toc'])
    data = {
        'title': f"{title} | Dbdowjfb ",
        'heading' : title,
        'tags': tags,
        'paragraphs': paragraphs_html
    }
    
    # 渲染模板并生成静态页面
    # print( title)
    output = template.render(data)
    
    return output
def write_html(output, post_dir, title):
    # output : the rendered html
    # post_dir : the directory of the generated html files
    # title : the title of the post

    # write the rendered html to a file
    with open(f'{post_dir}/{title}.html', 'w', encoding ='utf-8') as file:
        file.write(output)

def get_title(content): 
    # 从content中获取title
    return process_metadata(content)['title'] if process_metadata(content) else get_metadata(content)['date']

# test get_title
# print('below are titles and tags for the test post')

# print(get_title('markdown/mdtest.md'))

def get_tags(content : str) -> list:
    # content : the string of the markdown file
    # return a list of tags
    try:
        return process_metadata(content)['tags']
    except KeyError:
        return None
                   
def file_ctime(filename):
    # filename : the precise path of a file
    # return the creation time of the file
    # the format is year-month-day-hour-minute-second 
    # return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(os.path.getmtime(filename))) 
    return get_file_date(filename)

def get_file_date(file_path):
    print("file_path:", file_path)
    try:
        # 运行 git log 命令获取文件的最后修改日期
        command = ["git", "log","--reverse", r"--date=format:%Y-%m-%d %H:%M", "--date=iso-local", file_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        modified_date = result.stdout.strip().split('\n')
        for line in modified_date:
            if line.startswith('Date:'):
                print("listified_line:", line.split('Date:')[1].strip().split(' '))
                listified_line = line.split('Date:')[1].strip().split(' ') # dates and tzone after 'Date:
                print("listified_line2:", listified_line)        
                break     
        # print("file:", file_path)
        # print("listified_line3:", listified_line)
        return ' '.join(listified_line).strip()
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Error:", e.stderr)
        print("file:", file_path)
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
            title = get_title(markdown_content) 
            html_filename = f'{name_a_file(f"{md_dir}/{md}")}'  
            print("MAKE SURE THAT:")
            print('The current post directory is `post`')
            print('The current markdown directory is `markdown`')
            
            file_data={ 
                'title': title,
                'tags': get_tags(markdown_content),
                # concatenate the directory to specify the path of markdown and html files 
                'html_path' : f"post/{html_filename}.html",
                'md_path' : f"markdown/{md}", 
                'ctime' : file_ctime(f'{md_dir}/{md}'), # the date of the initial commit
                'publish' : post_vivsibility(process_metadata(markdown_content))
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
                title = get_file_date(filename)
    else: 
        title = get_title(markdown_content)
    return re.sub(r'\s', '-', title) # replace the spaces in the title with '-'


# print(name_a_file('markdown/readme.md'))

# render html for each post
def render_html_for_each_post(template_name, md_dir, post_dir):
    # md_dir : the directory of markdown files
    # render html for each post
    # ALSO delete unpublished posts


    for file in os.listdir(md_dir) :
        
        if file.endswith('.md'): 

            file_content = text_file_to_string(f'{md_dir}/{file}')
            visibility = post_vivsibility(process_metadata(file_content))
            
            if os.path.isfile(f"{md_dir}/{file}") and visibility != 'draft' :
                
                md = file 
                # put markdown file into a string 
                markdown_content = text_file_to_string(f'{md_dir}/{md}') 
                
                output = render_html(template_name, markdown_content) 
                

                # write the rendered html to a file
                # print("filename", name_a_file(f'{md_dir}/{md}'))
                write_html(output=output, post_dir=post_dir,title=  name_a_file(f'{md_dir}/{md}')) 

                # publish images in the markdown file to the post directory
                # concatenate the directory to specify the path of markdown file 
                convert_path = lambda x: os.path.basename(x)
                pubimg = linked_images(markdown_content)
                pubimg = [
                    f'{md_dir}/{convert_path(img)}' for img in pubimg
                    ]
                publish_images(pubimg, post_dir)
            elif visibility == 'draft':
                post_file = f'{post_dir}/{name_a_file(f"{md_dir}/{file}")}'
                delete_post(post_file)
                delete_post(post_file +'.html')
                

# render data for index page to a list of links to each post 
# written in markown 

def render_index_page(data_json, index_page_path) -> None:
    
    # data_json : the json file containing data for each post
    # render a markdown file for index page
    # each post is a link to the post
    
    # the link in the markdown file is the form "[title](html_path)"
    
    with open(data_json, 'r') as file:
        data : list = filter(lambda x: x['publish'] == 'public',json.load(file))
        # the link in the json file is the form "html_path": "/post/mdtest.html"
        # the link in the markdown file is the form "[title](html_path)"

        # order the posts by the creation time of the markdown file
        try:
            posts = sorted(data, key=lambda x: x['ctime'], reverse=True)
        except KeyError:
            print('KeyError in sorting data. We will skip this time.')
            pass 
        
        # print(type(posts[1]))
        # change the dates in the format in chinese
        for post in posts:
            post['ctime'] = post['ctime'][:11].replace('-', '年', 1).replace('-', '月', 1).replace('-', '日', 1) 

        # create the index page using jinja2 from the data in the json file 
        # print("posts contain: ", posts)
        
        template = Environment(
            loader= FileSystemLoader('./template')).get_template('index.html')
        
        output = template.render(posts=posts, title="Dbdo")

        # write the rendered html to a file
        with open(f'{index_page_path}', 'w', encoding='utf-8') as file:
            file.write(output)

def rss_time(time):
    input_datetime_str = ' '.join(time.split(' ')[:2]).strip()
    input_datetime = datetime.strptime(input_datetime_str, r'%Y-%m-%d %H:%M:%S')
    input_offset = time.split(' ')[-1]
    # return the current time in the format of rss
    # 解析时区偏移字符串
    offset_hours = int(input_offset[:3])  # 提取小时部分
    offset_minutes = int(input_offset[3:])  # 提取分钟部分

    # 创建时区对象
    offset_tz = pytz.FixedOffset(offset_hours * 60 + offset_minutes)

    # 将datetime对象应用时区偏移
    localized_datetime = input_datetime.replace(tzinfo=offset_tz)

    # 转换为UTC时间
    utc_datetime = localized_datetime.astimezone(pytz.UTC)

    return utc_datetime.strftime(r"%a, %d %b %Y %H:%M:%S GMT")

    


def create_rss(data_json, rss_path):
    rss_content = f'''<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:admin="http://webns.net/mvcb/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    >
    <channel>
    <description>Dbdo 的网站</description>
    <link > http://dbdo.website </link>
    <title>Dbdo 的网站</title>
     <atom:link href="http://dbdo.website" rel="self" type="application/rss+xml" />
    @@@ 
    </channel>
    </rss>
    '''
    items = ''
    with open(data_json, 'r') as file:
        site_url = 'https://dbdo.website'
        data = json.load(file)
        # the link in the json file is the form "html_path": "/post/mdtest.html"
        # the link in the markdown file is the form "[title](html_path)"
        try:
            # order the posts by the creation time of the markdown file
            posts = sorted(data, key=lambda x: x['ctime'], reverse=True)
            print("posts:", posts)
        except KeyError:
            print('KeyError in sorting data. We will skip this time.')
            pass 
        
        # iterate through the sorted list of posts
        for post in posts:
            # append posts info to the rss_content between <channel> and </channel>
            # create a new item tag
            with open(post['md_path'], 'r') as file:
                content = file.read()
            
            content = pandoc(content, flags=['--mathml','-V','title:'])
            item = f'''
            <item>
                <title>{post['title']}</title>
                <link>{site_url}/{post['html_path']}</link>
                <description>{post['title']}</description>
                <content:encoded><![CDATA[
                {content}
                ]]>
                 </content:encoded>
                <pubDate>{rss_time(post['ctime'])}</pubDate>
                <guid>{site_url}/{post['html_path']}</guid>
            </item>
            '''
            items += item
    rss_content = rss_content.replace('@@@', f'{items}\n') 
    with open(rss_path, 'w') as file:
        file.write(rss_content)

md_sample = """
    title: test
    tags: test

"""
# TEST
# print("generate metadata")
# print(generate_metadata(md_sample, '2020-01-01 00:00:00 +0800'))
def get_metadata(markdown_content : str) -> str:
        # print("get metadata is called")
        yaml_metadata = ''
        in_metadata_block = False
        # if no metadata return None
        if not markdown_content.startswith('---'):
            print(markdown_content)
            raise ValueError('No metadata')
        # if there is metadata, return the metadata
        else:    
            for lines in markdown_content.split('\n'):

                if lines.startswith('---') and not in_metadata_block:
                    # print('metadata block starts')
                    in_metadata_block = True
                    continue
                elif lines.startswith('---') and in_metadata_block:
                    # print('metadata block ends')
                    in_metadata_block = False
                    break
                if in_metadata_block:
                    yaml_metadata += lines + '\n'
                    # print('yaml_metadata:', yaml_metadata)

            return yaml_metadata

def process_metadata(markdown_content) -> dict:
    

# print(get_metadata(string))
    
    def yamlparser(yamlstring):
        """
        parse yaml string to a dictionary
        """
        return yaml.load(yamlstring, Loader=yaml.FullLoader)
    
    
#     def generate_metadata(markdown_content : str, file_date : str) -> str:
#             """
#             generate metadata for a markdown file
#             where the metadata is missing
#             markdown_path : the path of a markdown file
            
#             insert metadata in the form of yaml and insert 
#             in the start of the markdown content and then
#             return the markdown content with metadata

#             also clean up the old unenclosed metadata
#             """
            
#             return f"""---
# title: {get_title(markdown_content)}
# date: {file_date}
# tags: {get_tags(markdown_content) 
#         if get_tags(markdown_content) else ''}
# ---\n\n{    
#             ''.join([clearup_md(line)                      
#                      for line in markdown_content.splitlines()])
#             }"""

    # def insert_metadata(markdown_path):
    #     """
    #     insert metadata in the form of yaml and insert 
    #     in the start of the markdown content and then
    #     return the markdown content with metadata
    #     """
    #     with open(markdown_path, 'r') as file:
    #         markdown_content = file.read()
    #         file_date = get_file_date(markdown_path)
    #         file_with_metadata = generate_metadata(markdown_content, file_date)
    #     overwrite_file(markdown_path, file_with_metadata)
    
    # def overwrite_file(filename, content) -> None:
    #     with open(filename, 'w') as file:
    #         file.write(content)

    # def clearup_md(line : str) -> str:
    #     """
    #     clear up the metadata not enclosed in ---
    #     in the markdown file
    #     """
        
    #     if line.startswith('title:') or line.startswith('tags:'):
    #         return ''
    #     else:
    #         return line
    try:
        metadata = get_metadata(markdown_content)
        # print("metadata:", metadata)
        return yamlparser(metadata)
    except ValueError:
        print('ValueError in processing metadata')
        return None


def post_vivsibility(metadata : dict) -> str:
    """
    dict : a dictionary of a post's metadata
    return the visibility of the post
    default visibility is public
    """
    try:
       return metadata['publish']
    except KeyError:
        return 'public'

def linked_images(markdown_content : str) -> list:
    list_of_images = re.findall(r'!\[.*?\]\((.*?)\)', markdown_content)
    return list_of_images

def publish_images(list_of_images : list, public_dir : str) -> None:
    """
    list_of_images : a list of images in the markdown file
    (each image is in the form of 'assets/image.png')
    public_dir : the directory of the generated html files
    publish images in the markdown file to the post directory
    """
    if 'assets' not in os.listdir(public_dir):
        print('assets not in public_dir')
        os.mkdir(f'{public_dir}/assets')

    for image in list_of_images:
        if image in os.listdir(public_dir):
            continue
        else:
            # if the operating system is windows, use powershell to copy the image
            # if the operating system is linux, use cp to copy the image
            if os.name == 'nt':
                os.system(f'powershell -c " cp {image} {public_dir}/assets" ')
            elif os.name == 'posix':
                os.system(f'cp {image} {public_dir}/assets')
            else:
                raise OSError('Unsupported operating system')

def delete_post(post_path : str) -> None:
    """
    post_path : the path of a post
    delete the post
    """
    try:
        os.remove('{post_path}')
    except FileNotFoundError:
        print('FileNotFoundError in deleting post')
        # pass


def main():
    # root : the root directory of the blog
    root_dir = os.getcwd()
    markdown_dir = f'{root_dir}/markdown'
    template_dir = f'{root_dir}/template'
    post_dir = f'{root_dir}/public/post' 
    index_page_path = f'{root_dir}/public/index.html'
    # render html for each post
    update_data(md_dir=markdown_dir)
    render_html_for_each_post(
        
        template_name="post.html", 
        
        md_dir = markdown_dir, 
        
        post_dir=post_dir
    )
    print("OK move on")
    # render index markdown 
    render_index_page(f'{root_dir}/data.json',index_page_path=index_page_path)
    # generate rss.xml
    create_rss(data_json=f'{root_dir}/data.json', rss_path = f'{root_dir}/public/rss.xml')

if __name__ == '__main__':
    main()
    # if --debug is specified, open a http server to view the generated html
    try: 
        if sys.argv[1] == '--debug':
            os.system('python -m http.server -d ./public 5000')
    except IndexError:
        pass


        

