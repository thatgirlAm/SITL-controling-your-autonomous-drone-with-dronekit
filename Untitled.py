from donekit import connect, VehiculeMode
import argparse 

#Connecting 

vehicle = connect(127.0.0.1:14550, wait_ready=True)
 
# obtenir les valeurs actuelles des canaux channels = vehicle.channels
 
# afficher les valeurs des canaux print("Ch1: %s" % channels['1']) print("Ch2: %s" % channels['2']) print("Ch3: %s" % channels['3']) print("Ch4: %s" % channels['4']) print("Ch5: %s" % channels['5']) print("Ch6: %s" % channels['6']) print("Ch7: %s" % channels['7']) print("Ch8: %s" % channels['8'])
