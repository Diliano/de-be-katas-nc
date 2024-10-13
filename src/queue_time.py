class CustomersValidationError(Exception):
    def __init__(self):
        self.message = "Customers must be a list of positive integers"
        super().__init__(self.message)

class CheckoutsValidationError(Exception):
    def __init__(self):
        self.message = "Checkouts must be a positive integer"
        super().__init__(self.message)

def queue_time(customers, checkouts):
    if not isinstance(customers, list):
        raise CustomersValidationError

    all_ints = all(isinstance(customer, int) and customer > 0 for customer in customers)
    if not all_ints:
        raise CustomersValidationError
    
    if not isinstance(checkouts, int) or not checkouts > 0:
        raise CheckoutsValidationError

    tills = [0 for _ in range(checkouts)]

    for time in customers:
        min_till = min(tills)
        min_index = tills.index(min_till)
        tills[min_index] += time

    return max(tills)