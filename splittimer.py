name = "Grand Theft Auto V"
import win32ui
import win32api
import time
import numpy as np
import keyboard
import ctypes
import datetime

#Keyoutput Directkeys with ScanCodes
#-------------------------------------------------------------
#One of the Sources of for this direct key output https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
#Various versions of it floating around on stackoverflow

SendInput = ctypes.windll.user32.SendInput
Z = 0x2C

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, 
ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#-------------------------------------------------------------
#Time converter
def timedisplay(inputtime):
    Outputtime = str(datetime.timedelta(milliseconds=int(inputtime*1000)))
    Outputtime=Outputtime[:-3]
    Outputtime=Outputtime[2:]
    print(Outputtime)
    return(Outputtime)

#----------------------------------------------------------
#Clear files
file = open("checkpointblue.txt","w")
file.write("")
file.close()

file = open("checkpointred.txt","w")
file.write("")
file.close()

file = open("time.txt","w")
file.write("")
file.close()

file = open("laptimes.txt","w")
file.write("")
file.close()


#---------------------------------------------------------

#t1 = time.time()
color = {0,0,0}
cursor = [1850,924]
cp = np.array([[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8],[-18,-6],[-8,-5],[-13,-7],[-6,-6],[-11,-6],[-15,-13],[-17,-12],[-12,-6],[-9,-10],[-10,-8]])


w = win32ui.FindWindow( None, name )
dc = w.GetWindowDC()

lcp = 17
ccp = 1

maxlap = 10

time.sleep(2)

start = 0

was_pressed_u = False
was_pressed_o = False
invalidlap = False

dottieI = 255

racetimer = 0
lap = 1

print("Laps: %s\n" % (maxlap))
print("Checkpoints: %s\n" % (lcp))
print("Ready...\n")

def startrace():
    start = 1
    print("GOOOOOOO!!!!")
      


while(start == 0):
    startRGB = dc.GetPixel (1030,266)

    startR =  startRGB & 255
    startG = (startRGB >> 8) & 255
    startB =   (startRGB >> 16) & 255
    startI = (startR+startG+startB)/3

    if(keyboard.is_pressed('i')):
       startrace()
       invalidlap = True
       break
    else:
       pass
    
    if(startI > 250):
        startrace()
        break

    #Decrease max laps
    if(keyboard.is_pressed('u') and maxlap > 1):
        if not was_pressed_u:
            maxlap -= 1
            was_pressed_u = True
            print("Max Lap: %s" % (maxlap))
    else:
        was_pressed_u = False


    #Increase max laps
    if(keyboard.is_pressed('o') and maxlap > 1):
        if not was_pressed_o:
            maxlap += 1
            was_pressed_o = True
            print("Max Lap: %s" % (maxlap))
    else:
        was_pressed_o = False


racetimer = time.time()

besttime = 99999999.999999
bestlap = 0

ccptimings = ([])
ccptimings = np.append(ccptimings, time.time()-racetimer)
bestccptimings = ([])


while(True):

    zboisRGB = dc.GetPixel (1849,924)

    zboisR =  zboisRGB & 255
    zboisG = (zboisRGB >> 8) & 255
    zboisB =   (zboisRGB >> 16) & 255
    zboisI = (zboisR+zboisG+zboisB)/3

    if(zboisI < 234): #234
        pressKey(Z)
        time.sleep(.045)
        releaseKey(Z)

    #sets Current Check Point to 0 if you are at the last checkpoint(lcp)
    if(ccp >= lcp):
        ccp = 0

    #save temporary ccp
    pcp = ccp
        
    tcp = cp[ccp+1]
    RGBint = dc.GetPixel (cursor[0]+tcp[0],cursor[1]+tcp[1])     


    Red =  RGBint & 255
    Green = (RGBint >> 8) & 255
    Blue =   (RGBint >> 16) & 255
    Intensity = (Red+Green+Blue)/3

    #Check for key presses, change checkpoint up and down if something goes wrong
    
    #Decrease max checkpoints
    if(keyboard.is_pressed('u') and keyboard.is_pressed('k') and maxlap > 1):
        if not was_pressed_u:
            lcp -= 1
            was_pressed_u = True
            print("Max Checkpoints: %s" % (lcp))

    #Increase max checkpoints
    elif(keyboard.is_pressed('o') and keyboard.is_pressed('k') and maxlap > 1):
        if not was_pressed_o:
            lcp += 1
            was_pressed_o = True
            print("Max Checkpoints: %s" % (lcp))

    #Decrease max laps
    elif(keyboard.is_pressed('u') and keyboard.is_pressed('l') and maxlap > 1):
        if not was_pressed_u:
            maxlap -= 1
            was_pressed_u = True
            print("Max Lap: %s" % (maxlap))


    #Increase max laps
    elif(keyboard.is_pressed('o') and keyboard.is_pressed('l') and maxlap > 1):
        if not was_pressed_o:
            maxlap += 1
            was_pressed_o = True
            print("Max Lap: %s" % (maxlap))

    #Back 1 checkpoint
    if(keyboard.is_pressed('u') and not ccp <= 1):
        if not was_pressed_u:
            ccp -= 1
            print(ccp)
            was_pressed_u = True
            invalidlap = True
    else:
        was_pressed_u = False
        
    #Forward 1 checkpoint
    if(keyboard.is_pressed('o') and not ccp >= lcp):
        if not was_pressed_o:
            ccp += 1
            print(ccp)
            was_pressed_o = True
            invalidlap = True
            delta = time.time()-racetimer
            
            try:
                ccptimings[pcp] = delta
            except:
                ccptimings = np.append(ccptimings, delta)
            
    else:
        was_pressed_o = False

    if(ccp == 0 and lap == maxlap):
        dottieRGB = dc.GetPixel (1846,1051)
        dottieR =  dottieRGB & 255
        dottieG = (dottieRGB >> 8) & 255
        dottieB =   (dottieRGB >> 16) & 255
        dottieI = (dottieR+dottieG+dottieB)/3

        
        
    #Check if intensity of pixel is reached then do checkpoint
    #CHECKPOINT
    if(Intensity > 235 or dottieI < 235):
        delta = time.time()-racetimer
        try:
            checkpointdelta = delta - bestccptimings[pcp]
            stringerbell = str(checkpointdelta)
            if(checkpointdelta <= 0):
                stringerbell = stringerbell [1:]
                stringerbell = stringerbell [:5]
                
                file = open("checkpointred.txt","w")
                file.write("")
                file.close()
                
                file = open("checkpointblue.txt","w")
                file.write("-00:0%s" % (stringerbell))
                file.close()
            else:

                stringerbell = stringerbell [:5]

                file = open("checkpointblue.txt","w")
                file.write("")
                file.close()
                
                file = open("checkpointred.txt","w")
                file.write("+00:0%s" % (stringerbell))
                file.close()
        except:
            pass
        try:
            ccptimings[pcp] = delta
        except:
            ccptimings = np.append(ccptimings, delta)
        
        ccp += 1
        print("Checkpoint: %s" % (ccp))


    #LAP
    if(ccp == 1 and pcp == 0):

        racetimer = time.time()
        
        timestring = str(timedisplay(delta))


        #BESTLAP
        if(delta < besttime and invalidlap == False):
            besttime = delta
            bestlap = lap
            bestccptimings = np.copy(ccptimings)
            file = open("besttime.txt","w")
            file.write("%d	%s\n" %(lap, timestring))
            file.close()



        
        invalidlap = False

        
        
        file = open("time.txt","w")        
        file.write(timestring)
        file.close()
        
        file = open("laptimes.txt","a")
        file.write("%d	%s\n" % (lap, timestring))
        file.close()

        print("LAP %d!" % (lap))
        lap += 1
        pcp = 1
        if(lap > maxlap):
            dc.DeleteDC()
            quit()
        
        
        
        
        


            






