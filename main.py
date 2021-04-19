class Person:
    def __init__(self, is_truthful):
        self.truthful = int(is_truthful)

    def said(self, claim):
        return claim if self.truthful else not claim

    def is_liar(self):
        return not self.truthful

    def is_truth_teller(self):
        return self.truthful

    def __eq__(self, person):
        return self.truthful == person.truthful

    def __ne__(self, person):
        return self.truthful != person.truthful


def list_solutions(num_of_people, check_function):
    solutions = []

    # There are 2^n possible outcomes.
    for state in range(2 ** num_of_people):

        # Remove "0b" and pad to length "num_of_people".
        binary_repr = bin(state)[2:].zfill(num_of_people)

        # Create the world of people possible with this configuration.
        possible_world = [Person(c) for c in binary_repr]

        if check_function(possible_world):
            solutions.append(binary_repr)

    return solutions

# Your code goes below! Describe the problem and it should solve it.
