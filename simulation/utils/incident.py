from datetime import datetime
import pandas as pd
import time
import sys
from incident_response import incident_response_library, ddos_response, r2l_response, u2r_response, probe_response

#ALL INCIDENT INFORMATION IS SAVED TO THIS CLASS FOR FUTURE LOGGING PURPOSES#
class Incident:

	#INTIATING INCIDENT OBJECT LOGS ALL INPUT DATA#  
    def __init__(self, network_info, attack_prediction, other_data='none'):
      
		#SAVED NETWORK DATA TO INCIDENT OBJECT VARIABLE#      
        self.info = network_info
        
        #CROSS REFERENCES LIBRARY TO CONVERT ATTACK LABEL INTO ATTACK NAME#
        self.attack = incident_response_library.get(str(attack_prediction))
        
        self.other = other_data
        current_time = datetime.now()
        
        #DETERMINES IF INCIDENT IS LABELLED A FALSE POSITIVE ALARM#
        self.false_positive = False
        
        #INCIDENT RESPONSE UNIQUE ID IS CREATED#
        self.id = str(attack_prediction) + ":" + current_time.strftime("%d%m%Y%H%M%S")
	
    #SETS false_positive TO TRUE TO MAKE INCIDENT DATA AS FALSE POSITIVE#
    def retrain_info(self, info):
        print("\nSENDING DATA TO RETRAIN CLASSIFIERS")
        for i in range(101):
            time.sleep(0.04)
            sys.stdout.write("\r%d%%" % i)
            sys.stdout.flush()
        print("\n")
        self.false_positive = True
        
    #CROSS REFERENCES CORRECT REPONSE WITH LIBRARY ACCORDING TO ATTACK CLASS#
    def recommended_response(self, attack):
        if attack == 'ddos':
          print(ddos_response)
        if attack == 'u2r':
          print(u2r_response)
        if attack == 'r2l':
          print(r2l_response)
        if attack == 'probe':
          print(probe_response)
          
	#PRINTS OUT INCIDENT DETAILS & ASKS FOR USER INPUT TO CHECK FOR FALSE POSITIVES#
    def respond(self):
      
        #PRINT INCIDENT DETAILS#
        print("\n========== INCIDENT " + str(self.id) + " ==========\n\n")
        print("ATTACK OCCURING: " + str(self.attack)+ "\n")
        
        #ONLY PRINT OUT NECESSARY NETWORK INFORMATION#
        network_inf = self.info.iloc[:,84:]
        print("NETWORK DATA SNAPSHOT: \n" + network_inf.to_string(index=False))
        
        #ASKS FOR USER INPUT TO DETERMINE IF FALSE POSITIVE#
        print("\nPRESS 1 IF ATTACK IS FALSE ALARM, PRESS 0 TO CONTINUE WITH INCIDENT RESPONSE: \n")
        false_alarm = input()
        if false_alarm == '1':
            retrain_info = self.info
            self.retrain_info(self.info)
        if false_alarm == '0':
            self.recommended_response(self.attack)
