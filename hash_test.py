import os 
import time
from blog import *

a = os.listdir('markdown')[0] 
print(a)
start_time = time.time()

for i in os.listdir('markdown'):
    s = text_file_to_string('markdown/'+i)
    h = hash(s)

end_time = time.time()

print(end_time - start_time)

