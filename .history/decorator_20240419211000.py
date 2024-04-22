from abc import ABC, abstractmethod

# コーヒーインターフェース
class AbstractCoffee(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

# ベースのコーヒークラス
class Coffee(AbstractCoffee):
    @property
    def cost(self) -> int:
        return 200

    @property
    def description(self) -> str:
        return 'コーヒー'

# コーヒーのトッピングデコレーター
class CoffeeDecorator(AbstractCoffee, ABC): # 抽象クラス（インスタンス化しない）
    def __init__(self, decorated_coffee: AbstractCoffee):
        self.decorated_coffee = decorated_coffee

    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost

    @property
    def description(self) -> str:
        return self.decorated_coffee.description

# トッピングの具体的なデコレータークラス
class CreamDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 50

    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、生クリーム'

class VanillaDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 70

    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、バニラアイス'