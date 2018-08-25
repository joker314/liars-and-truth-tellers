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

def list_all_solutions(num, keys):
    solutions = []
    for i in map(lambda x: (num + 2 - len(bin(x))) * "0" + bin(x)[2:], range(2**num)):
        all_conditions_satisfied_thus_far = True
        for j in keys:
            if not j(map(Person, i)):
               all_conditions_satisfied_thus_far = False
               break
        if all_conditions_satisfied_thus_far: solutions.append(i)
    return solutions
    
# Your code below! You should describe the problem and it will (hopefully) solve it

