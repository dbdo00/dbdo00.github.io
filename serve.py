from livereload import shell, Server

def run( ):
    server = Server()
    server.watch("./markdown/*.md", 
                 shell("make")
                 )
    server.serve(
        root = 'public'
        )

run()
    




