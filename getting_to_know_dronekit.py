from dronekit import connect, VehiculeMode, LocationGlobalRelative
import time 
import exceptions

#---Connection----
          
import argparse
          
parser = argparse.ArgumentParser(description'Commands')
parser.add_argument('--connect')
args = parser.pars_args()
             
#connection_string is the ip adress of our drone 
connection_string = args.connect  
    
print('Connectiong to vehicule on: %s' connection_string)
vehicule = connect(connection_string, wait_ready = True)
    
#----Guided mode > Armed drone----
    
def arm_and_takeoff(targetAltitude):
        while not vehicule.is_armable:
        
          while not vehicule.is_armable:
                print("Waiting for the drone to initialize..."
                time.sleep(1)
        print("Arming motors")
        vehicule.mode = VehiculeMode("GUIDED")
        vehicule.armed = True

        while not vehicule.armed:
                print("Waiting for arming")
                time.sleep(1)
        print("Taking off")
        vehicule.simple_takoff(targetAltitude)

#the drone has not taken off and is trying to reach targetAltitude (in meters)
        while True:
        print("Altitude: ", vehicule.location.global_relative_frame.alt);
                if vehicule.location.global_relative_frame>= targetAltitude * 0.95: 
               			print("Targetted altitude reached");
               			break;
                        time.sleep(5);
#function to get the drone's' location  
 def get_location():
      return [vehicule.current_location.lat, vehicule.current_location.lon, vehicle.location.global_relative_frame.alt] 
 
 def opening_pods(coordinates):
 	if 45.440693< coordinates[0]<45.439335 and -0.429470< coordinates[1]<-0.428641 or 45.440693< coordinates[0]<45.439335 and -0.429470< coordinates[1] :
 		#open the pods
 		 
 			
                      
#-------MAIN------
arm_and_takeoff(10)

print("setting target airspeed to 3m per second");
vehicile.airspeed = 3;

print(" preparing for step 1 of mission : Navigation")

# first step of mission is navigation, the drone will hover over an area to be #able to reach step two : pods opening;

wayPoint_1 = LocationGlobalRelative(45.440693, -0.428641,20);
wayPoint_2 = LocationGlobalRelative(45.439335, -0.429470,20);
wayPoint_3 = LocationGlobalRelative(45.439213, -0.428641,20);


vehicule.simple_goto(wayPoint_1, groundspeed=20);
time.sleep(5)
vehicule.simple_goto(wayPoint_2, groundspeed=10);
time.sleep(5)
vehicule.simple_goto(wayPoint_3, groundspeed=5;
time.sleep(5)

print("Recognition ok")
time.sleep(3)

print("Starting phase 2 : Payload //")
time.sleep(3)

vehicule.simple_goto(wayPoint_1,groundspeed=3);
#function opening pods
#on va semer du wayPoint_1 au wayPoint_2
time.sleep(3)

#on arrête de semer entre wayPoint_2 et wayPoint_3
opening_pods(coordinates)
vehicule.simple_goto(wayPoint_2, groundspeed=3);
time.sleep(3)

#function opening pods
opening_pods(coordinates)
time.sleep(3)
vehicule.simple_goto(wayPoint_3,groundspeed=3);

# get location 
#coordinates = get_location()
opening_pods(coordinates)
