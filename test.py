import blog 
import os 

# root_dir = os.getcwd()
# markdown_dir = f'{root_dir}/markdown'
# post_dir = f'{root_dir}/public/post' 
# text = blog.text_file_to_string(f'markdown/2023-09-10.md')
# # print(text)

# img = blog.linked_images(text)
# # print(img)
# path = lambda x: os.path.normpath(x)
# img = [ 
#     "markdown/" + path(x) for x in img 
# ]

# # print(img)

# blog.publish_images(img, public_dir=post_dir)

# blog.main() 


def dict_contains(data:dict, key,value) -> bool:
    return (key,value) in data.items()
        
def img_rec_json(json_input):
    if isinstance(json_input, dict):
        if dict_contains(json_input, 't', 'Image'):
            yield json_input
        else:
            for k, v in json_input.items(): 
                yield from img_rec_json(v)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from img_rec_json(item)

if __name__ == "__main__":

# test json
#     import sys 
#     import json 
#     a = sys.stdin.read()
#     print(a)
#     for i in img_rec_json(json.loads(a)):
#         print(i['c'][-1][0])

# # test pandoc json
#     # from blog import pandoc_json
#     # print(pandoc_json('*a*'))

# # test linked_iamges
#     text = blog.text_file_to_string(f'markdown/2023-09-10.md')
#     print(text)

#     img = blog.linked_images(text)
#     print(img)
    import urllib.parse

    # Example string with HTML special characters
    html_string = "Hello%20World%21"

    # Decode HTML special characters
    decoded_string = urllib.parse.unquote(html_string)

    print(decoded_string)
