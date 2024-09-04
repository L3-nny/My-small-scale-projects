# Power Usage Tracking System

## Overview
This project provides a web application for tracking and calculating household power usage. Users can input the time spent using various appliances and see how much power has been used and how much remains.


## Background
I went back to my place and forgot to carry my token meter which tracks my remaining energy balance enabling me to gauge my usage.
Since I'll have to wait a week before I get the token meter back, I had to improvise and find a way of tracking my power usage.
It is then that this app was conceived.

## How it works
At the moment, it's for my personal use.
I came up with a way of tracking my power usage. I only have 3 major electrical appliances in my house;
the shower heater, sony speaker and 3 light bulbs.
It therefore has only 3 user inputs; time I spend in the shower, time I spend listening to music on my speaker and time spent with lights on.
I used the manufacturers power ratings in the code to ensure high accuracy of calculations performed.
The output given is in kWh which is the same unit used on the KPLC token meter.
It is therefore a simple solution to my problem of missing my token meter.

![image](https://github.com/user-attachments/assets/b47fea49-32ff-41b7-8052-bf758f29ad00)


## Errors present
1. These values are based on estimations since I don't time how long I stay in the bathroom, how long my speaker is on or how long the lights stay on.
2. The code assumes constant power consumption for each appliance. In reality, appliances may have variable power usage depending on their operation.
For example, a speaker’s power consumption can vary with volume.
3. The code does not account for appliances that consume power even when not actively in use (standby power). This can be significant for some devices like chargers.
4. The code assumes non-overlapping usage of appliances (e.g., I'm either using the shower or the bulbs, but not both at the same time). If multiple
appliances are used simultaneously, the actual power consumption might be higher.
5.There is no validation for user input. For example, if a user inputs a negative time or power value, the application might not handle it correctly
6.The code stores power usage history in memory, which means it will be lost if the app is restarted.Implementing persistent storage
(e.g., saving to a file or database) might be necessary for long-term tracking.
