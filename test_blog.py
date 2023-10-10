import blog

mtdt = blog.process_metadata("./markdown/2023-09-10.md")

s = blog.text_file_to_string("./markdown/2023-09-10.md")

print(s)
print(blog.get_title(s))
blog.render_html_for_each_post(md_dir="./markdown", post_dir="./public/post", template_name="post.html")