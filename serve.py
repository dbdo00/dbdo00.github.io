from livereload import shell, Server

def run( ):
    server = Server()
    server.watch("./markdown/*.md", 
                 shell("make addandcommit")
                 )
    server.serve(
        restart_delay=0.3,
        root = 'public'
        )

run()
    




