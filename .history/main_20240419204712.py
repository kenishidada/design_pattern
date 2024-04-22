from facade import FacadeSolution
from strategy import StrategyA, client

# FacadePattern
facade = FacadeSolution()
print(facade.solve(10))

StrategyA()


