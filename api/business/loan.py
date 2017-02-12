from pprint import pprint 

class Loan:
    
    threshold = 50000

    def get_decision(self, requested_amount):
        
        if int(requested_amount) > self.threshold:
            return 'Declined'
        elif int(requested_amount) == self.threshold:
            return 'Undecided'
        elif int(requested_amount) < self.threshold:
            return 'Approved'
        else:
            return 'What are you trying to test?'