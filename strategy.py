# Strategyパターン
from abc import ABC, abstractmethod

# ストラテジーのインターフェース
class AbstractStrategy(ABC):
    @abstractmethod
    def do(self):
        pass

# 具体的なストラテジー
class StrategyA(AbstractStrategy):
    def do(self):
        print('StrategyA')

class StrategyB(AbstractStrategy):
    def do(self):
        print('StrategyB')

class StrategyC(AbstractStrategy):
    def do(self):
        print('StrategyC')

# クライアント
def client(strategy: AbstractStrategy): # インターフェース（抽象クラス）に依存
    strategy.do()