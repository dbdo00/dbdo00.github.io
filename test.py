import blog 
import os 

root_dir = os.getcwd()
markdown_dir = f'{root_dir}/markdown'
post_dir = f'{root_dir}/public/post' 
text = blog.text_file_to_string(f'markdown/2023-09-10.md')
print(text)

img = blog.linked_images(text)
print(img)
f = lambda x: os.path.normpath(x)
img = [ 
    "markdown/" + f(x) for x in img 
]

print(img)

blog.publish_images(img, public_dir=post_dir)

blog.main() 