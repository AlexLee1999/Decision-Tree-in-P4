import numpy as np
import pandas as pd

Input_File = "./16-09-23.csv"
Output_File = "./16-09-23_withlabel.csv"
device_class = {
    "smart-home devices": 1,
    "sensors"           : 2,
    "audio"             : 3,
    "video"             : 4,
    "other"             : 5
}

Mac_address_with_class = {
    "d0:52:a8:00:67:5e" : 1,    #Smart Things 				        Wired
    "44:65:0d:56:cc:d3" : 3,    #Amazon Echo 			            Wireless
    "70:ee:50:18:34:43" : 1,    #Netatmo Welcome 			        Wireless
    "f4:f2:6d:93:51:f1" : 4,    #TP-Link Day Night Cloud camera 	Wireless
    "00:16:6c:ab:6b:88" : 4,    #Samsung SmartCam 			 	    Wireless
    "30:8c:fb:2f:e4:b2" : 4,    #Dropcam 				 	        Wireless
    "00:62:6e:51:27:2e" : 4,    #Insteon Camera 					Wired 
    "e8:ab:fa:19:de:4f" : 4,    #Insteon Camera                     Wireless
    "00:24:e4:11:18:a8" : 4,    #Withings Smart Baby Monitor 		Wired
    "ec:1a:59:79:f4:89" : 5,    #Belkin Wemo switch 			 	Wireless
    "50:c7:bf:00:56:39" : 1,    #TP-Link Smart plug 			 	Wireless
    "74:c6:3b:29:d7:1d" : 1,    #iHome 					 	        Wireless
    "ec:1a:59:83:28:11" : 2,    #Belkin wemo motion sensor 		 	Wireless
    "18:b4:30:25:be:e4" : 2,    #NEST Protect smoke alarm 			Wireless
    "70:ee:50:03:b8:ac" : 2,    #Netatmo weather station 		 	Wireless
    "00:24:e4:1b:6f:96" : 1,    #Withings Smart scale 			 	Wireless
    "74:6a:89:00:2e:25" : 1,    #Blipcare Blood Pressure meter 		Wireless
    "00:24:e4:20:28:c6" : 2,    #Withings Aura smart sleep sensor 	Wireless
    "d0:73:d5:01:83:08" : 1,    #Light Bulbs LiFX Smart Bulb 		Wireless
    "18:b7:9e:02:20:44" : 3,    #Triby Speaker 				 	    Wireless
    "e0:76:d0:33:bb:85" : 5,    #PIX-STAR Photo-frame 			 	Wireless
    "70:5a:0f:e4:9b:c0" : 5,    #HP Printer 				 	    Wireless
    "08:21:ef:3b:fc:e3" : 5,    #Samsung Galaxy Tab				    Wireless
    "30:8c:fb:b6:ea:45" : 4,    #Nest Dropcam					    Wireless
    "40:f3:08:ff:1e:da" : 5,    #Android Phone					    Wireless
    "74:2f:68:81:69:42" : 5,    #Laptop						        Wireless
    "ac:bc:32:d4:6f:2f" : 5,    #MacBook						    Wireless
    "b4:ce:f6:a7:a3:c2" : 5,    #Android Phone					    Wireless
    "d0:a6:37:df:a1:e1" : 5,    #IPhone						        Wireless
    "f4:5c:89:93:cc:85" : 5,    #MacBook/Iphone					    Wireless
    "14:cc:20:51:33:ea" : 5     #TPLink Router Bridge LAN (Gateway)	
}


df = pd.read_csv(Input_File)

for index, row in df.iterrows():
    src = row['eth.src']
    
    if src in Mac_address_with_class:
        # If there is a match, append a new column (address) with dict's corresponding value
        df.loc[index, "class"] = Mac_address_with_class[src]
    else:
        # If there is no match, delete the entire row
        df = df.drop(index)
        
df["class"] = df["class"].astype(int)

df.to_csv(Output_File, index=False)