import subprocess
import sys
import os
blog = os.environ.get("blog")

# 替换为你的blog的路径


def execute_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()

execute_command(f"cd {blog}")
def run_blog_script():
    print(f"Running blog.py...")
    execute_command("python blog.py")
    print("Committing and pushing to Git...")
    execute_command("git add * && git commit -m 'update' -a  && git push")

def run_code_and_wait(title):
    print("Running code...")
    execute_command(f"code ./markdown/{title}.md")

    # 等待code窗口关闭
    input("Press Enter to continue...")


    # 继续执行其他操作
    run_blog_script()

# 获取命令行参数
args = sys.argv[1]

if "-p" in args:
    run_blog_script()
elif "-w" in args:
    title = sys.argv[2]
    run_code_and_wait(title)
else:
    print("Invalid argument. Please use either '-p' or '-w'.")

