# Split Timer GTA5
---
## What is it?
Split timer GTA5 is a python script that output split timings, your last lap times and best lap time for GTA5 races. 

Link to video of it in action: [https://www.youtube.com/watch?v=FFvwj7o-fw4](https://www.youtube.com/watch?v=FFvwj7o-fw4)

Download latest verions here(follow instructions bellow): [SplitTimer.zip](https://drive.google.com/u/0/uc?export=download&id=1PghXbmV3eSt5vVFN0ZCdl-KXdKVZZJVV)


It does this by checking for a pixel in the checkpoint number and when it changes it knows it hit a check point and records the time of that checkpoint. It counts them and and with user input knows how many checkpoints there are in total to know when a lap has been completed. 

If a is the fastest lap has been achieved it writes out the timing for that lap and sets the split timings accordingly. 

It outputs the time data into text files which can then be read by Play Claw and displayed on screen.

## Controls

Load up the script while in the car selection phase or in the loading screen before the race so that you are tabbed in and the script is ready to detect the race has started.
You want the programs max laps and max checkpoints to match the ingame max laps and max checkpoints so it know when you have lapped and completed the race. Set this as fast as possible in the race before you go past checkpoint #2.
Start GTA 5, Start Play Claw, and last while in game start Split Timer(as admin)

**Before the race has started:**

I = Increase max laps

U = Decrease max laps

H = Force start race (if the script was started after the race had started)

**While the race is going on:**

I = Increase max laps

U = Decrease max laps

O+I = Checkpoint Row +1

O+U = Checkpoint Row -1

**Checkpoint row:**
Changes what row in the bottom right in game that it reads pixels from, counting from the bottom row 4 is on most maps with more than 1 lap, but it can change

K = Increase max checkpoints +1

J = Decrease max checkpoints -1

O+K = Increase max checkpoints +10

O+J = Decrease max checkpoints -10

H = Start Race

O+H = Pause script, also reloads pixel reading if you tab in our out

L+H = Restart Script

**Cheats/Bugmode if something fucks up:**

L+I = Forward 1 lap

L+U = Backwards 1 Lap

L+K = Increase current checkpoint +1 (if you started race late and need the script to catch up to the in game checkpoint)

L+J = Decrease current checkpoint -1 (if you need to adjust what checkpoint the script thinks you are on)

## Installing

0. Download from Releases to the right
1. Install Play Claw and run it once and then close it. (so folders will be created)
2. Run "Programdata-PlayClaw5.exe" and export the files into C:\ProgramData\PlayClaw5plus
3. Run "Programfiles-x86-PlayClaw5.exe" and export the files into C:\Program Files (x86)\PlayClaw 5 Plus
4. Start GTA V, Play Claw and Splittimer(as admin)

## Shoutout to D3DShot

[https://github.com/SerpentAI/D3DShot](https://github.com/SerpentAI/D3DShot)
Allows to grab pixels from fullscreen game super fast

