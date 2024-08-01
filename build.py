from blog import * 

root_dir = os.getcwd()
markdown_dir = f'{root_dir}/markdown'
template_dir = f'{root_dir}/template'
post_dir = f'{root_dir}/public/post' 
index_page_path = f'{root_dir}/public/post/index.html'
render_html_for_each_post(
        
        template_name="post.html", 
        
        md_dir = markdown_dir, 
        
        post_dir=post_dir, 

        updated = lambda x: True 
    )
update_data(md_dir=markdown_dir)
render_index_page(f'{root_dir}/data.json',index_page_path=index_page_path)
    # generate rss.xml
create_rss(data_json=f'{root_dir}/data.json', rss_path = f'{root_dir}/public/rss.xml')
print("Build complete")
