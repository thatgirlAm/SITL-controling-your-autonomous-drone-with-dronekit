# Little dronekit X Qground control example
drone kit X Qgroundcontrol 

# Install requiered dependencies 

``sudo pip install dronekit``

``sudo pip install mavproxy``

``sudo pip install pymavlink ``

``sudo pip install dronekit-sitl ``

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

`mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550``

What it does is that Mavproxy creates a TCP server on the 5670 port then forward all the packets on the port 14550. That's where you need to connect on your script.


Then you'll open your ground station, here it's QgroundControl.

There is a known bug between Python scripts and mavlink that disallow any script to control and change the VehicleMode.

It's supposed to be fixed by going back to pymavlink version 2.4.8 but I didn't test it yet because I found a work-around.

It's messy but hey, it works.

You basically have to manually change the VehicleMode on your QGroundStation :

![Capture d'écran_20230223_195417](https://user-images.githubusercontent.com/109297892/221003463-de3af800-c32d-4b58-b738-44976ecc2507.png)

See the "Stabilize" on the top ? Click on it and select "Guided".

Now that it has been done, you can go ahead and launch your script using

`` python (your_script.py) ``

When your script is launched, the "Ready to Fly" will change into a "Communication Lost". Don't worry, communication is lost because your script is now controlling the drone. Now you have to wait until your script finishes and you'll see that your drone moves according to your script.

NB: Sometimes, when you launch your script, it loads "Waiting for arming" for infinity. I have no idea why, so I just Ctrl-C and launch the python command again.

Now, profit !!

![drone](https://user-images.githubusercontent.com/109297892/221008823-1de2011f-6aa8-4f09-99da-aa0f5002b7b8.png)


