class Person():
    def __init__(self, tellsTheTruth):
        self.am = int(tellsTheTruth)
    
    def said(self, condition):
        return condition if self.am else not condition

    def isLiar(self):
        return not self.am

    def isTruthTeller(self):
        return self.am

    def __eq__(self, person):
        return self.am == person.am

    def __ne__(self, person):
        return self.am != person.am

def list_all_solutions(num_of_people, conditions):
    solutions = []
    for decimal_combination in range(2 ** num_of_people): # Number of different combinations
        bin_from_dec = bin(decimal_combination)[2:] # Strip the first 2 chars as these are '0b'
        binary_combination = (num_of_people - len(bin_from_dec)) * "0" + bin_from_dec
        all_conditions_satisfied_thus_far = True
        for check_condition in conditions:
            """
            We've now converted a combination into binary, e.g. 101
            We can use map() to create a list [Person("1"), Person("0"), Person("1")]
            Which will become a list of a T-teller, Liar, and T-teller, in that order
            """
            if not check_condition(list(map(Person, binary_combination))):
               all_conditions_satisfied_thus_far = False
               break
        if all_conditions_satisfied_thus_far: solutions.append(binary_combination)
    return solutions
    
# Your code below! You should describe the problem and it will (hopefully) solve it

