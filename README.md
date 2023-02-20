# Little dronekit X Qground control example
drone kit X Qgroundcontrol 

# Install requiered dependencies 

``sudo pip install dronekit``

``sudo pip install mavproxy``

``sudo pip install pymavlink ``

# Launching the TCP connection 

In a terminal tab enter

``dronekit-sitl [the model you want] ``

you can find out your options with 

``dronekit-sitl --list `` 

for this example we're going to use the copter model

so we'll enter 

`` dronekit-sitl copter ``

if your program executes normally, you'll have 

"waiting for connection" at the bottom of your console 

In a new terminal tab, enter the following lines :

``mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501  --out 127.0.0.1:14550 --out 127.0.0.1:14551``

here we use two ports 14550 and 14551, you can go on, but here we'll only use the two ports for now. 

the you'll open your ground station, here it's QgroundControl 

here we'll go : "application's settings > Comm links > Add" 

we'll create TCP port, the host will be 127.0.0.1 and the hotspot will be 5760.

After you create your TCP port (give it a name lol), hit "connect" then look at your terminal

If everything goes well, QgroundControl will display 'Ready to Fly'
