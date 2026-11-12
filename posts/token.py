import os
import re

# Read all my posts.
posts = {post_name: open(post_name).read() for post_name in os.listdir('.') if post_name.endswith('.md') }

print(posts)

