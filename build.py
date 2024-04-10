from blog import * 
main()
render_html_for_each_post(
        
        template_name="post.html", 
        
        md_dir = markdown_dir, 
        
        post_dir=post_dir, 

        updated = lambda x: True 
    )