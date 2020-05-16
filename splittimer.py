import win32ui
import win32api
import d3dshot
import time
import numpy as np
import keyboard
import ctypes
import datetime
name = "Grand Theft Auto V"

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
#----------------------------------------------------------
#Load keybindings from keybindings.txt

with open("keybindings.txt","r") as f:
    mylist = f.read().splitlines()

keybindings = []

for i in mylist:
    i = i [5:]
    i = i [:i.find(" ")]
    keybindings.append(i)


keybind_1 = keybindings[1]  #KEY1:I     Max lap +1 / Max lap +10 / Forward 1 lap         | LAP KEY UP  
keybind_2 = keybindings[2]  #KEY2:U     Max lap -1 / Max lap -10 / Backwards 1 lap 	 | LAP KEY DOWN
keybind_3 = keybindings[3]  #KEY3:K 	Max CP +1  / Max CP +10  / Forward 1 Checkpoint  | CHECKPOINT KEY UP
keybind_4 = keybindings[4]  #KEY4:J 	Max CP -1  / Max CP -10  / Backwards 1 Checkpoint| CHECKPOINT KEY DOWN
keybind_5 = keybindings[5]  #KEY5:H 	START 	   / PAUSE       / RESTART		 | START
keybind_6 = keybindings[6]  #KEY6:O 	MODIFIER					 | MODIFIER
keybind_7 = keybindings[7]  #KEY7:L 	CHEAT MODIFIER					 | CHEAT MODIFIER
keybind_8 = keybindings[8]  #KEY8:F     YOUR IN GAME RESPAWN BUTTON                      | PREVENTS FALSE CHECKPOINT TRIGGER WHEN RESPAWNING

print("           NORMAL     / +MODIFIER   / +CHEAT MODIFIER")
print("KEY1:%s     Max lap +1 / Max lap +10 / Forward 1 lap         | LAP KEY UP" % (keybind_1))
print("KEY2:%s     Max lap -1 / Max lap -10 / Backwards 1 lap 	    | LAP KEY DOWN" % (keybind_2))
print("KEY3:%s     Max CP +1  / Max CP +10  / Forward 1 Checkpoint  | CHECKPOINT KEY UP" % (keybind_3))
print("KEY4:%s     Max CP -1  / Max CP -10  / Backwards 1 Checkpoint| CHECKPOINT KEY DOWN" % (keybind_4))
print("KEY5:%s     START      / PAUSE       / RESTART		    | START" % (keybind_5))
print("KEY6:%s     MODIFIER					    | MODIFIER" % (keybind_6))
print("KEY7:%s     CHEAT MODIFIER				    | CHEAT MODIFIER" % (keybind_7))
print("KEY8:%s     YOUR IN GAME RESPAWN BUTTON                      | PREVENTS FALSE CHECKPOINT TRIGGER WHEN RESPAWNING" % (keybind_8))
print("")


was_pressed_1 = False
was_pressed_2 = False
was_pressed_3 = False
was_pressed_4 = False
was_pressed_5 = False
was_pressed_6 = False
was_pressed_7 = False
was_pressed_8 = False

#---------------------------------------------------------
#Load settings

with open("settings.txt","r") as f:
    mylist = f.read().splitlines()

settings = []

for i in mylist:
    i = i [8:]
    i = i [:i.find("	")]
    i = int(i)
    settings.append(i)

#   settings[0] maxlap | MAX LAPs
#   settings[1] lcp | MAX CPs
#   settings[2] cursorrow | Checkpoint Row
#   settings[3] graceperiod | Grace Period at start of race in seconds
#   settings[4] fullscreen | If the game is run in fullscreen or not, 1 or 0

#-----------------------------------------------------------

cursorpos = [1865,1858,1858,1858,1859,1858,1860,1859,1858,1847,1855,1848,1848,1848,1849,1848,1850,1848,1848,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1840,1848,1841,1841,1841,1841,1841,1843,1841,1841,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1841,1849,1842,1841,1842,1843,1841,1843,1842,1841,1840,1848,1841,1840,1841,1841,1840,1842,1841,1840,1842,1849,1843,1842,1843,1843,1842,1844,1843,1842,1840,1848,1842,1841,1842,1842,1841,1843,1842,1841,1840,1848,1841,1840,1841,1841,1840,1842,1841,1840]
#cursor = [1850,924]
cp = np.array([[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8],[-18,-8],[-9,-17],[-13,-7],[-11,-11],[-11,-6],[-13,-19],[-17,-7],[-5,-19],[-14,-10],[-10,-8]])

if(settings[4] == 1):
    fullscreen = 1
else:
    fullscreen = 0

if(fullscreen == 0):
    w = win32ui.FindWindow( None, name )
    dc = w.GetWindowDC()


#Just creating variables, don't change here, scroll down
prevgrace = 0
lcpendinone = False
respawntimer = 0
maxlap = 1
was_maxlap_changed = False

start = 2



invalidlap = False

racetimer = 0

def getintensity(inX,inY):

    if(fullscreen):

        #the y and x are reversed because that's the way it comes out from d3dshot
        frame = d.get_latest_frame()        
        #print(inX)
        #print(inY)
        #print(np.shape(frame))
        
        frame = frame[inY,inX]
        #print(frame)
        intensityFullscreen = (int(frame[0])+int(frame[1])+int(frame[2]))/3
        #print(intensityFullscreen)
        return(intensityFullscreen)
    
    else:
        intRGB = dc.GetPixel (inX,inY)
        
        intR =  intRGB & 255
        intG = (intRGB >> 8) & 255
        intB =   (intRGB >> 16) & 255
        intI = (intR+intG+intB)/3
        return(intI)

def startrace():
    start = 1
    print("GOOOOOOO!!!!")
      
#d = d3dshot.create(capture_output="numpy",frame_buffer_size=10)
while(True):
    
    print("PAUSED... waiting for input press '%s' to load script" % (keybind_5))
    while(start == 2):
        #time.sleep(0.05)
        if(keyboard.is_pressed(keybind_5)):
            if not was_pressed_5:

                if(fullscreen):
                    d = d3dshot.create(capture_output="numpy",frame_buffer_size=10)
                    d.capture(target_fps = 100)
                    time.sleep(.1)
                
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
                was_pressed_5 = True
                break
        else:
            was_pressed_5 = False
            
    print("READY... waiting for race to start or input press '%s' to start" % (keybind_5))    
    while(start == 0):
        
        #startRGB = dc.GetPixel (1030,266)

        startI = getintensity(1030,266)

        if(keyboard.is_pressed(keybind_5)):
            if not was_pressed_5:
                startrace()
                invalidlap = True
                was_pressed_5 = True
                break
        else:
            was_pressed_5 = False
        
        if(startI > 250):
            startrace()
            break

        #Decrease max laps
        if(keyboard.is_pressed(keybind_2 + "+" + keybind_6) and maxlap > 1):
            if not was_pressed_2:
                maxlap -= 1
                was_pressed_2 = True
                was_maxlap_changed = True
                print("Max Lap: %s" % (maxlap))
        else:
            was_pressed_2 = False


        #Increase max laps
        if(keyboard.is_pressed(keybind_1 + "+" + keybind_6) and maxlap < 99):
            if not was_pressed_1:
                maxlap += 1
                was_pressed_1 = True
                was_maxlap_changed = True
                print("Max Lap: %s" % (maxlap))
        else:
            was_pressed_1 = False

#---------------------------------------------------------------
#RACESTART!
#---------------------------------------------------------------

    racetimer = time.time()

    #   settings[0] maxlap | MAX LAPs
    #   settings[1] lcp | MAX CPs
    #   settings[2] cursorrow | Checkpoint Row
    #   settings[3] graceperiod | Grace Period at start of race
    #   settings[4] fullscreen | If the game is run in fullscreen or not
    
    if(was_maxlap_changed == False):
        maxlap = settings[0]
    else:
        was_maxlap_changed = False

    graceperiod = settings[3]
    gracecounter = graceperiod+1
    
    lcp = settings[1]

    if(lcp in (11, 21, 31, 41, 51, 61, 71, 81, 91)):
        lcpendinone = True
    else:
        lcpendinone = False
    
    cursorrow = settings[2]
      
    cursor = [cursorpos[lcp-1],924-(cursorrow-4)*43]

    lap = 1
    ccp = 1
    dottieI = 255
    
    besttime = 99999999.999999
    bestlap = 0

    ccptimings = ([])
    ccptimings = np.append(ccptimings, time.time()-racetimer)
    bestccptimings = ([])

    print("Laps: %s\n" % (maxlap))
    print("Checkpoints: %s\n" % (lcp))
    print("Checkpoint at row: %s\n" % (cursorrow))

    #last_time = time.time()
    releaseme = time.time()-5

    while(True):
        #script was too fast so had to sleep it a bit
        time.sleep(0.000001)

        
        #print('Loop took %s seconds' % (time.time()-last_time))
        #last_time = time.time()

        #zboisRGB = dc.GetPixel (1849,924)
        #zboisRGB = dc.GetPixel (50,30)
        #zboisI = getintensity(zboisRGB)
        
        #if(zboisI < 234) and not (ccp == 0 and lap == maxlap): #234
            #pressKey(Z)
            #time.sleep(.055)
            #releaseKey(Z)
                
        #zboisRGB = dc.GetPixel (58,34)
        zboisI = getintensity(57,34)        

        #globeRGB = dc.GetPixel (1210,17)        
        globeI = getintensity(1210,17)

        #Added releaseme delta because it would run twice, so it waits .75 sec before going again
        releasemedelta = time.time()-releaseme
        
        if(globeI > 0 and zboisI < 245 and not (ccp == 0 and lap == maxlap) and releasemedelta > .75): #234
            #print(globeI)
            pressKey(Z)
            time.sleep(.015)
            releaseKey(Z)
            count = 0
            releaseme = time.time()
            while(True):
                
                #zboisRGB = dc.GetPixel (58,34) #(50,30)
                zboisI = getintensity(57,34)
                #print(zboisI)
                time.sleep(0.005)
                count += 1
                if(zboisI > 245):
                    #print(count)
                    #print("i did it actually, wtf")
                    #print("Looped: %s times" % (count))
                    time.sleep(0.05)
                    zisset = False
                    break
                
                elif(count > 29):
                    print(zboisI)
                    print("57,34")
                    print("I got suck in vinkelvolten: %s times" % (count))
                    break

        #just in case Z is pressed it corrects it back to normal
        elif(zboisI < 245 and not (ccp == 0 and lap == maxlap) and releasemedelta > .25):

            if not zisset:
                zisset = True
                ztime = time.time()
                
            if zisset:
                if(time.time()-ztime > .25):
                    
                    print("Reopened UI")
                    pressKey(Z)
                    time.sleep(.015)
                    releaseKey(Z)
                    releaseme = time.time()
                    zisset = False

        
        #sets Current Check Point to 0 if you are at the last checkpoint(lcp)
        if(ccp >= lcp):
            ccp = 0

        #save previous ccp
        pcp = ccp

        #target cp    
        tcp = cp[ccp+1]
        
        #RGBint = dc.GetPixel (cursor[0]+tcp[0],cursor[1]+tcp[1])
        
        Intensity = getintensity(cursor[0]+tcp[0],cursor[1]+tcp[1])


#----------------------------------------------------------------------------------------------
        #Check for key presses

        
        #Cursors row increase
        if(keyboard.is_pressed(keybind_1 + "+" + keybind_6) and cursorrow < 10):
            if not was_pressed_1:
                cursorrow += 1
                cursor = [cursor[0],cursor[1]-43]
                print("Checkpoint Row: ▲ %s" % (cursorrow))
                print(cursor)
                was_pressed_1 = True
                
        #Cursor row decrease
        elif(keyboard.is_pressed(keybind_2 + "+" + keybind_6) and cursorrow > 1):
            if not was_pressed_2:
                cursorrow -= 1
                cursor = [cursor[0],cursor[1]+43]
                print("Checkpoint Row: ▼ %s" % (cursorrow))
                print(cursor)
                was_pressed_2 = True
                
        #Decrease max checkpoints -10
        elif(keyboard.is_pressed(keybind_4 + "+" + keybind_6) and lcp > 11):

            if not was_pressed_4:
                lcp -= 10
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_4 = True
                
                if(lcp in (11, 21, 31, 41, 51, 61, 71, 81, 91)):
                    lcpendinone = True
                else:
                    lcpendinone = False
                print("Max Checkpoints: ▼ %s" % (lcp))

        #Increase max checkpoints +10
        elif(keyboard.is_pressed(keybind_3 + "+" + keybind_6) and lcp < 89):
            if not was_pressed_3:
                lcp += 10
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_3 = True

                if(lcp in (11, 21, 31, 41, 51, 61, 71, 81, 91)):
                    lcpendinone = True
                else:
                    lcpendinone = False
                print("Max Checkpoints: ▲ %s" % (lcp))

        #Back 2 checkpoint
        elif(keyboard.is_pressed(keybind_4 + "+" + keybind_7) and not ccp <= 1):
            if not was_pressed_4:
                ccp -= 2
                print("Current Checkpoint: ▼ %s" % (ccp))
                was_pressed_4 = True
                invalidlap = True
            
        #Forward 1 checkpoint
        elif(keyboard.is_pressed(keybind_3 + "+" + keybind_7) and not ccp >= lcp):
            if not was_pressed_3:
                ccp += 1
                print("Current Checkpoint: ▲ %s" % (ccp))
                was_pressed_3 = True
                invalidlap = True
                delta = time.time()-racetimer
                time.sleep(0.1)               
                try:
                    ccptimings[pcp] = delta
                except:
                    ccptimings = np.append(ccptimings, delta)
                
        #Forward 1 lap
        elif(keyboard.is_pressed(keybind_1 + "+" + keybind_7) and lap < maxlap):
            if not was_pressed_1:
                lap += 1
                print("Current Lap: ▲ %s" % (lap))
                was_pressed_1 = True        
      
        #Backwards 1 lap
        elif(keyboard.is_pressed(keybind_2 + "+" + keybind_7) and lap > 1):
            if not was_pressed_2:
                lap -= 1
                print("Current Lap: ▼ %s" % (lap))
                was_pressed_2 = True
                
        #Pause
        elif(keyboard.is_pressed(keybind_5 + "+" + keybind_6) and maxlap < 99):
            if not was_pressed_5:
                print("Paused!... press %s to resume" % (keybind_5))
                if(fullscreen):
                    d.stop()
                    del d
                was_pressed_5 = True
                while(True):
                    time.sleep(0.01)
                    if(keyboard.is_pressed(keybind_5)):
                        if not was_pressed_5:
                            was_pressed_5 = True
                            print("Unpaused! Go!")
                            if(fullscreen):
                                d = d3dshot.create(capture_output="numpy",frame_buffer_size=10)
                                d.capture(target_fps = 100)
                                time.sleep(.1)
                            break
                    else:
                        was_pressed_5 = False
            
        #Restart race
        elif(keyboard.is_pressed(keybind_5 + "+" + keybind_7) and maxlap < 99):
            if not was_pressed_5:
                was_pressed_5 = True
                print("Restart, back to beginning of script")
                if(fullscreen):
                    d.stop()
                    del d
                start = 2
                break                

            
        #Decrease max checkpoints
        elif(keyboard.is_pressed(keybind_4) and lcp > 1):
            if not was_pressed_4:
                lcp -= 1
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_4 = True
                
                if(lcp in (11, 21, 31, 41, 51, 61, 71, 81, 91)):
                    lcpendinone = True
                else:
                    lcpendinone = False
                    
                print("Max Checkpoints: ▼ %s" % (lcp))                
                    
        #Increase max checkpoints
        elif(keyboard.is_pressed(keybind_3) and lcp < 99):
            if not was_pressed_3:
                lcp += 1
                cursor = [cursorpos[lcp-1],cursor[1]]
                was_pressed_3 = True
                
                if(lcp in (11, 21, 31, 41, 51, 61, 71, 81, 91)):
                    lcpendinone = True
                else:
                    lcpendinone = False
                    
                print("Max Checkpoints: ▲ %s" % (lcp))

        #Respawn timer grace period
        elif(keyboard.is_pressed(keybind_8)):
            if not was_pressed_8:
                was_pressed_8 = True
                timerkey8 = time.time()
                
            if was_pressed_8:
                print("%s: %s" % (keybind_8,round(time.time()-timerkey8,1)))
                time.sleep(0.1)
                if(time.time()-timerkey8 > 2.5):
                    respawntimer = time.time()
                    print("You did it, you held it for 2.5 sec")
                    
        #Decrease max laps
        elif(keyboard.is_pressed(keybind_2)):
            if not was_pressed_2 and maxlap > 1:
                maxlap -= 1
                was_pressed_2 = True
                print("Max Lap: ▼ %s" % (maxlap))
                    
        #Increase max laps
        elif(keyboard.is_pressed(keybind_1) and maxlap < 99):
            if not was_pressed_1:
                maxlap += 1
                was_pressed_1 = True
                print("Max Lap: ▲ %s" % (maxlap))
        else:
            was_pressed_1 = False
            was_pressed_2 = False
            was_pressed_3 = False
            was_pressed_4 = False
            was_pressed_5 = False
            was_pressed_8 = False
            
        if(ccp == 0 and lap == maxlap):
            #dottieRGB = dc.GetPixel (1846,1051)

            dottieI = getintensity(1846,1051)

#----------------------------------------------------------------------------------------------
        #CHECKPOINT
            
            
        endindoneReady = True
        
        if(lcpendinone == True and ccp == 0 and lap != maxlap):
            #gets first digit in lcp
            onetcp = cp[int(str(lcp)[:1])]

            #RGBendinone = dc.GetPixel (cursor[0]+onetcp[0]-10,cursor[1]+onetcp[1])
            endinoneI = getintensity(cursor[0]+onetcp[0]-10,cursor[1]+onetcp[1])
            
            #print(cursor[0]+onetcp[0]-10,cursor[1]+onetcp[1])
            #print(endinoneI)
            if(endinoneI < 240):
                endindoneReady = True
            else:
                endindoneReady = False

        #after you respawn disables checkpoint reading for a while because of flashing screen
        if(time.time()-respawntimer < 2.5):
            print(round(2.5-(time.time()-respawntimer),1))
            time.sleep(.1)
        #Grace peroid at beginning of race before reading checkpoints    
        elif(time.time()-racetimer < graceperiod and lap == 1):
            time.sleep(0.01)  
            
        #Check if intensity of pixel is reached then do checkpoint    
        elif(240 <= Intensity <= 240 and not (ccp == 0 and lap == maxlap) and endindoneReady or dottieI < 235):
            #print(Intensity)
            #print(cursor[0]+tcp[0],cursor[1]+tcp[1])
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
                d.stop()
                del d
                start = 2
                break
            
        
        
        
        
        


            






