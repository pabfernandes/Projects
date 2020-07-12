#  This is just a test about car makers

# definindo a classe car maker:
def CarMaker(self, maker, country):
    n_makers = 0  # number of car makers
    all_makers = []

    def __new__(cls):
        if n_makers < 10:
            return object.__new__(cls)

    # defining the car maker
    def __init__(self, maker, country):
        self.maker = maker
        self.country = country
        self.n_makers += 1
        self.allmakers.append(maker)

    def __str__(self, maker, country):
        return f'The maker {self.maker} is from {self.country}'

    def __
