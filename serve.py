from livereload import shell, Server

def run( ):
    server = Server()
    server.watch("./markdown/*.md", 
                 shell('git add * && git commit && make')
                 )
    server.serve(
        restart_delay=0.3,
        root = 'public'
        )

run()
    




