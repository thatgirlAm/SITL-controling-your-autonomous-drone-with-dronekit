# Little dronekit X Qground control example
drone kit X Qgroundcontrol 

# Install requiered dependencies 

``sudo pip install dronekit``

``sudo pip install mavproxy``

``sudo pip install pymavlink ``

``sudo pip install dronekit-sitl

# Launching the TCP connection 

In a terminal tab enter : 

``dronekit-sitl [the model you want] ``

you can find out your options with : 

``dronekit-sitl --list `` 

for this example we're going to use the copter model, so we'll enter :

`` dronekit-sitl copter ``

if your program executes normally, you'll have 

"waiting for connection" at the bottom of your console 

In a new terminal tab, enter the following lines :

``mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501  --out 127.0.0.1:14550 --out 127.0.0.1:14551``

here we use two ports 14550 and 14551, you can go on, but here we'll only use the two ports for now. 

the you'll open your ground station, here it's QgroundControl 

here we'll go : "application's settings > Comm links > Add" 

we'll create a TCP port, the host will be 127.0.0.1 and the hotspot will be 5760

<img width="912" alt="Capture d’écran 2023-02-20 à 20 56 05" src="https://user-images.githubusercontent.com/117035426/220189079-f4f655fb-76ae-489d-b637-83cfb84cba83.png">


After you create your TCP port (give it a name lol), hit "connect" then look at your terminal

If everything goes well, QgroundControl will display 'Ready to Fly'
<img width="912" alt="Capture d’écran 2023-02-20 à 20 55 22" src="https://user-images.githubusercontent.com/117035426/220189090-32d96657-6f0b-4c8d-a9d9-9aa19e1bbf20.png">

if you already have a python script, here's how you proceed : (my script's named test.py)

if you're on MacOs, run :

``python3 test.py `` 


