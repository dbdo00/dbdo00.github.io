import blog
import os
# mtdt = blog.process_metadata("./markdown/2023-09-10.md")

# s = blog.text_file_to_string("./markdown/2023-09-10.md")

# print(s)
# print(blog.get_title(s))
# blog.render_html_for_each_post(md_dir="./markdown", post_dir="./public/post", template_name="post.html")


md_sample = """
---
title: "My First Post"
date: 2023-09-10
---

# This is my first post
$E = mc^2$

## This is a subtitle

This is a paragraph

This is another paragraph

This is a third paragraph

This is a fourth paragraph



"""

with open("web_blank_pandoctemp.html", "w") as f:
    template = """
<header id="title-block-header">
<h1 class="title">$title$</h1>
</header>

$toc$
$body$

"""
    f.write(template)


html = blog.pandoc(md_sample,["--toc", "--mathml",])

print(html)

print("type is ", type(html))   


# delete template file
os.remove("web_blank_pandoctemp.html")