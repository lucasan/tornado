
import tornado.web
from business.loan import Loan

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class LoanDecisionHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", '*')
        requested_amount = self.get_argument('requested_amount')
        loan = Loan()
        answer = loan.get_decision(requested_amount)

        self.write(answer)