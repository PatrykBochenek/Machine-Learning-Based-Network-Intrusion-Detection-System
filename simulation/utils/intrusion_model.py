from sklearn import tree
import pandas as pd

#DECISION TREE INTRUSION ANALYSIS MODEL#
class IntrusionModel:
	
    def __init__(self,x,y):
      	#INSTANTIATES DECISION TREE UPON OBJECT CREATION#
        self.clf = tree.DecisionTreeClassifier()
        #ASSIGNS X_TRAIN DATASET TO OBJECT FOR REFERENCE#
        self.x_train = x
        #ASSIGNS Y_TRAIN DATASET TO OBJECT FOR REFERENCE#
        self.y_train = y
	
    #CLASSIFIER IS TRAINED USING ITS ASSIGNED DATASET#
    def train(self):
        x_train = self.x_train
        y_train = self.y_train
        self.clf = self.clf.fit(x_train,y_train)
	
    #CLASSIFIER RETRAINED USING UPDATED DATASET#
    def retrain(self, x, y):
        self.x_train = x
        self.y_train = y
        self.clf = self.clf.fit(self.x_train,self.y_train)
    
    #CLASSIFIER PREDICTS LABEL BASED ON INPUT DATA#
    def predict(self,data):
        result = self.clf.predict(data)
        return result