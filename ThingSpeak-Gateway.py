import serial.tools.list_ports
import thingspeak 
import keyboard


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

def thingSpeak(channel=None, apikey=None, data=None ):   
    datas = data[2:-5]       
    ch = thingspeak.Channel(int(channel), apikey,'json')
    d = datas.split(":")  
    d = dict([(k, v) for k,v in zip (d[::2], d[1::2])])
    print("sent: ", d) 
    ch.update(d)


for onePort in ports:
    portsList.append(str(onePort))
    print("\n************************************")
    print("*        ThingSpeak Gateway        *")
    print("*                                  *")   
    print("************************************")
    print("\nPort found: ")
    print(str(onePort))

print("\n")
val = input("Select Port: COM")

print("\n==== ThingSpeak Configuration =====\n")
valchannel = input("Enter Channel ID: ")

valkey = input("Enter Write API Key: ")
print("\n=================================== \n")


for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

print(">>>>> Press 'q' to exit <<<<<")

while keyboard.is_pressed('q') == False:
	
    if serialInst.in_waiting:
        packet = str( serialInst.readline() )
        thingSpeak( str(valchannel), str(valkey), packet )
    

serialInst.close() 
print("\nTchau!!") 

