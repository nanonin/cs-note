import sys
"""
tornado web 服务器
"""

if len(sys.argv)==1
    print('请输入端口号，like:facere_start 8098')

port = sys.argv[1]
print(port)

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from face_application import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(9765)
IOLoop.instance().start()