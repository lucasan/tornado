from application import WebApplication
from tornado.ioloop import IOLoop

def server():
    app = WebApplication()
    app.settings['template_path'] = './'
    app.listen(80)
    IOLoop.instance().start()

if __name__ == '__main__':
    server()