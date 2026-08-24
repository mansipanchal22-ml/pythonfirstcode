#q-3 -Create an abstract class MLModel with abstract methods:
# -train()
# -predict()
# -Create subclasses LinearRegressionModel and DecisionTreeModel implementing them.
# -Instantiate both and show how they share the same interface (train(), predict()), even with different implementations.

from abc import ABC, abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):

    def train(self):
        return "Linear Regression model is training"
    
    def predict(self):
        return "Linear Regression prediction"
    
class DecisionTreeModel(MLModel):

    def train(self):
        return "Decision Tree model is training"
    
    def predict(self):
        return "Decision Tree prediction"
    
linear_model = LinearRegressionModel()
tree_model = DecisionTreeModel()

print(linear_model.train())
print(linear_model.predict())

print(tree_model.train())
print(tree_model.predict())
