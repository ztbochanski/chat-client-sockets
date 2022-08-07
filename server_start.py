from server.server import Server

server = Server()
server.listen(2)
server.on_connection()
