from abc import ABC, abstractmethod

@abstractmethod
class Model:
    def __init__(self) -> None:
        pass

@abstractmethod
class SupervisedLearningModel(Model):
    def __init__(self) -> None:
        super().__init__()

@abstractmethod
class UnsupervisedLearningModel(Model):
    def __init__(self) -> None:
        super().__init__()

class ReinforcementLearningModel(Model):
    def __init__(self) -> None:
        super().__init__()
    

class NeuralNetworkModel(SupervisedLearningModel):
    pass

class MonteCarloTreeSearchModel(SupervisedLearningModel):
    pass

class AssociationRuleModel(UnsupervisedLearningModel):
    pass