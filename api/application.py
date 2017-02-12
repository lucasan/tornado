from handlers import *
import tornado.web

class WebApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/api/?", MainHandler),
            (r"/api/loanDecision/?", LoanDecisionHandler)
        ]
        tornado.web.Application.__init__(self, handlers)