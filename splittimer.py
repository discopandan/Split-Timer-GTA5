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
cursorpos = [1865,1858,1858,1858,1859,1858,1860,1859,1858,1847,1855,1848,1848,1848,1849,1848,1850,1848,1848,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1840,1848,1841,1841,1841,1841,1841,1843,1841,1841,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1841,1849,1842,1841,1842,1843,1841,1843,1842,1841,1840,1848,1841,1840,1841,1841,1840,1842,1841,1840,1842,1849,1843,1842,1843,1843,1842,1844,1843,1842,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1840,1848,1841,1840,1841,1841,1840,1842,1841,1840]
#cursor = [1850,924]
cp = np.array([[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-16,-20],[-5,-6],[-10,-8]])


w = win32ui.FindWindow( None, name )
dc = w.GetWindowDC()

lcp = 20
ccp = 1

maxlap = 3

cursorrow = 4
cursor = [cursorpos[lcp-1],924-(cursorrow-4)*43]


time.sleep(2)

start = 0

was_pressed_u = False
was_pressed_i = False
was_pressed_j = False
was_pressed_k = False
was_pressed_h = False
invalidlap = False

#dottieI = 255

racetimer = 0
#lap = 1

print("Laps: %s\n" % (maxlap))
print("Checkpoints: %s\n" % (lcp))
print("Checkpoint at row: %s\n" % (cursorrow))
#print("Ready...\n")

def startrace():
    start = 1
    print("GOOOOOOO!!!!")
      

while(True):
    
    while(start == 2):
        if(keyboard.is_pressed('h')):
            
            start = 0
            
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
            was_pressed_h = True
            break
            
    print("Ready... waiting for race to start or input press 'H' to start")    
    while(start == 0):
        
        startRGB = dc.GetPixel (1030,266)

        startR =  startRGB & 255
        startG = (startRGB >> 8) & 255
        startB =   (startRGB >> 16) & 255
        startI = (startR+startG+startB)/3

        if(keyboard.is_pressed('h')):
            if not was_pressed_h:
                startrace()
                invalidlap = True
                was_pressed_h = True
                break
        else:
            pass
            was_pressed_h = False
        
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
        if(keyboard.is_pressed('i') and maxlap < 99):
            if not was_pressed_i:
                maxlap += 1
                was_pressed_i = True
                print("Max Lap: %s" % (maxlap))
        else:
            was_pressed_i = False


    racetimer = time.time()

    lcp = 20
    lap = 1
    ccp = 1
    dottieI = 255

    besttime = 99999999.999999
    bestlap = 0

    ccptimings = ([])
    ccptimings = np.append(ccptimings, time.time()-racetimer)
    bestccptimings = ([])


    while(True):

        #zboisRGB = dc.GetPixel (1849,924)
        zboisRGB = dc.GetPixel (53,31)

        zboisR =  zboisRGB & 255
        zboisG = (zboisRGB >> 8) & 255
        zboisB =   (zboisRGB >> 16) & 255
        zboisI = (zboisR+zboisG+zboisB)/3

        if(zboisI < 234) and not (ccp == 0 and lap == maxlap): #234
            pressKey(Z)
            time.sleep(.055)
            releaseKey(Z)

        #sets Current Check Point to 0 if you are at the last checkpoint(lcp)
        if(ccp >= lcp):
            ccp = 0

        #save previous ccp
        pcp = ccp
            
        tcp = cp[ccp+1]
        #cursor = [cursor[0],cursor[1]-(cursorrow-4)*43]
        RGBint = dc.GetPixel (cursor[0]+tcp[0],cursor[1]+tcp[1])
        

        Red =  RGBint & 255
        Green = (RGBint >> 8) & 255
        Blue =   (RGBint >> 16) & 255
        Intensity = (Red+Green+Blue)/3

        #Check for key presses
        
        #Cursors row increase
        if(keyboard.is_pressed('i') and keyboard.is_pressed('o') and cursorrow < 10):
            if not was_pressed_i:
                cursorrow += 1
                cursor = [cursor[0],cursor[1]-43]
                print("Checkpoint Row: ▲ %s" % (cursorrow))
                print(cursor)
                was_pressed_i = True
                
        #Cursor row decrease
        elif(keyboard.is_pressed('u') and keyboard.is_pressed('o') and cursorrow > 1):
            if not was_pressed_u:
                cursorrow -= 1
                cursor = [cursor[0],cursor[1]+43]
                print("Checkpoint Row: ▼ %s" % (cursorrow))
                print(cursor)
                was_pressed_u = True
                print("don't know what's going on")
                
        #Decrease max checkpoints -10
        elif(keyboard.is_pressed('j') and keyboard.is_pressed('o') and lcp > 11):
            if not was_pressed_j:
                lcp -= 10
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_j = True
                print("Max Checkpoints: ▼ %s" % (lcp))

        #Increase max checkpoints +10
        elif(keyboard.is_pressed('k') and keyboard.is_pressed('o') and lcp < 89):
            if not was_pressed_k:
                lcp += 10
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_k = True
                print("Max Checkpoints: ▲ %s" % (lcp))

        #Back 1 checkpoint
        elif(keyboard.is_pressed('j') and keyboard.is_pressed('l') and not ccp <= 1):
            if not was_pressed_j:
                ccp -= 1
                print("Current Checkpoint: ▼ %s" % (ccp))
                was_pressed_j = True
                invalidlap = True
            
        #Forward 1 checkpoint
        elif(keyboard.is_pressed('k') and keyboard.is_pressed('l') and not ccp >= lcp):
            if not was_pressed_k:
                ccp += 1
                print("Current Checkpoint: ▲ %s" % (ccp))
                was_pressed_k = True
                invalidlap = True
                delta = time.time()-racetimer
                
                try:
                    ccptimings[pcp] = delta
                except:
                    ccptimings = np.append(ccptimings, delta)
                
        #Forward 1 lap
        elif(keyboard.is_pressed('i') and keyboard.is_pressed('l') and lap < maxlap):
            if not was_pressed_i:
                lap += 1
                print("Current Lap: ▲ %s" % (lap))
                was_pressed_i = True        
      
        #Backwards 1 lap
        elif(keyboard.is_pressed('u') and keyboard.is_pressed('l') and lap > 1):
            if not was_pressed_u:
                lap -= 1
                print("Current Lap: ▼ %s" % (lap))
                was_pressed_u = True        
       
        #Decrease max checkpoints
        if(keyboard.is_pressed('j') and lcp > 1):
            if not was_pressed_j:
                lcp -= 1
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_j = True
                print("Max Checkpoints: ▼ %s" % (lcp))
        else:
            was_pressed_j = False
                    
        #Increase max checkpoints
        if(keyboard.is_pressed('k') and lcp < 99):
            if not was_pressed_k:
                lcp += 1
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_k = True
                print("Max Checkpoints: ▲ %s" % (lcp))
        else:
            was_pressed_k = False
                    
        #Decrease max laps
        if(keyboard.is_pressed('u')):
            if not was_pressed_u and maxlap > 1:
                maxlap -= 1
                was_pressed_u = True
                print("Max Lap: ▼ %s" % (maxlap))
        else:
            was_pressed_u = False
                    
        #Increase max laps
        if(keyboard.is_pressed('i') and maxlap < 99):
            if not was_pressed_i:
                maxlap += 1
                was_pressed_i = True
                print("Max Lap: ▲ %s" % (maxlap))
        else:
            was_pressed_i = False
            
        #Restart race
        if(keyboard.is_pressed('h') and maxlap < 99):
            if not was_pressed_h:
                maxlap += 1
                was_pressed_h = True
                print("Max Lap: ▲ %s" % (maxlap))
        else:
            was_pressed_h = False


        if(ccp == 0 and lap == maxlap):
            dottieRGB = dc.GetPixel (1846,1051)
            dottieR =  dottieRGB & 255
            dottieG = (dottieRGB >> 8) & 255
            dottieB =   (dottieRGB >> 16) & 255
            dottieI = (dottieR+dottieG+dottieB)/3

            
        #print(Intensity)
        #time.sleep(.1)
        #Check if intensity of pixel is reached then do checkpoint
        #CHECKPOINT
        if(235 <= Intensity <= 240 and not (ccp == 0 and lap == maxlap) or dottieI < 235):
            print(Intensity)
            print(cursor[0]+tcp[0],cursor[1]+tcp[1])
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

            print("LAP %d completed!" % (lap))
            lap += 1
            pcp = 1
            if(lap > maxlap):
                print("Paused... waiting for input press 'H' to start")
                start = 2
                break
            
        
        
        
        
        


            






