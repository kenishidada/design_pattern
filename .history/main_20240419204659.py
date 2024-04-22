from facade import FacadeSolution
from strategy import StrategyA, client

# FacadePattern
facade = FacadeSolution()
print(facade.solve(10))

strategy = StrategyA()
print(client(strategy))

