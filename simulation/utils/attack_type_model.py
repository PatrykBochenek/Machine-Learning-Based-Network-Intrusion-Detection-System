from sklearn import tree
import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.neural_network import MLPClassifier

#MLP-DT CLASSIFIER#
class AttackTypeModel:

    def __init__(self,x,y,x_test,y_test):
      	
        #INSTANTIATES HYBRID CLASSIFIER
        mlp_clf = MLPClassifier(hidden_layer_sizes=[100]*6)
        score_mlp = mlp_clf.fit(x,y).score(x_test,y_test)
  
        dt_clf = tree.DecisionTreeClassifier()
        score_dt = dt_clf.fit(x,y).score(x_test,y_test)

        self.clf = VotingClassifier(estimators=[('MLP', mlp_clf), ('DT', dt_clf)], voting='soft', weights=[1.1,1])
		
        #SAVES TRAINING DATASET TO OBJECT#
        self.x_train = x
        self.y_train = y
	
    #TRAINS THE MLP-DT CLASSIFIER#
    def train(self):
        x_train = self.x_train
        y_train = self.y_train
        self.clf = self.clf.fit(x_train,y_train)

    #RETRAINS THE CLASSIFIER WITH FALSE POSITIVE RESULT#
    def false_positive_retrain(self, network_data):
        x_train = self.x_train
        y_train = self.y_train
        self.x_train = pd.concat([x_train,network_data],axis=0)
        self.y_train = pd.concat([y_train,1],axis=0)
        self.clf = self.clf.fit(self.x_train,self.y_train)
    
    #PREDICT LABEL OF INPUT DATA#
    def predict(self,data):
        result = self.clf.predict(data)
        return result