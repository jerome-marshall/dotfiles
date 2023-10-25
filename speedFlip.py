import time
import keyboard
import mouse
 
multiplier = 0.85  # increasing or decreasing this value will adjust the timing
hotKey = ';'  # this will trigger the script to perform a speed flip
hotKey2 = "'"
RMB = "right"  # jump key
right = "d"
left = "a"
airRollRight = "e"
airRollLeft = "q"
 
randomizerChange = 0.00  # how much the "randomizer" will change the delays
randomizer = False  # starts off
randomizerPlus = 0
 
 
def PrintBanner(endTime=0.0):
    print(
        f"""
(">": Increase, "<": Decrease)  Delays multiplier:     {multiplier}
(Speed flip time)               Speed flip time:       {str(endTime)[0:5]}
(Less sus toggle: "/")          "Randomizer":          {randomizer}
    """)
 
 
def UpdateDelays(print=True):
    global delay1, delay2, delay3, delay4, delay5, delay6
    delay1 = round(0.007 * multiplier, 4)
    delay2 = round(0.06 * multiplier, 4)
    delay3 = round(0.012 * multiplier, 4)
    delay4 = round(0.6 * multiplier, 4)
    delay5 = round(0.15 * multiplier, 4)
    delay6 = round(0.1 * multiplier, 4)
    if print:
        PrintBanner()
 
 
UpdateDelays()
 
 
def Increase(x):
    global multiplier
    if x == 'False':
        multiplier = round(multiplier + randomizerChange, 4)
        UpdateDelays(print=False)
    else:
        if randomizer: ToggleRandomizer('x')
        multiplier = round(multiplier + 0.025, 4)
        UpdateDelays()
 
 
def Decrease(x):
    global multiplier
 
    if x == 'False':
        multiplier = round(multiplier - randomizerChange, 4)
        if (multiplier < 0): multiplier = 0
        UpdateDelays(print=False)
    else:
        if randomizer: ToggleRandomizer('x')
        multiplier = round(multiplier - 0.025, 4)
        if (multiplier < 0): multiplier = 0
        UpdateDelays()
 
 
i = 1
 
 
def UpdateI():
    global i, randomizerPlus
    if randomizer:
        if i == 1:
            Increase('False')
            i = 2
            randomizerPlus = randomizerChange
        elif i == 2:
            Decrease('False')
            i = 3
            randomizerPlus = 0
        elif i == 3:
            Decrease('False')
            i = 4
            randomizerPlus = -randomizerChange
        elif i == 4:
            Increase('False')
            i = 1
            randomizerPlus = 0


def DoSpeedFlip(mainKey, airRollKey):
    UpdateI()
    start = time.time()
 
    lastW = keyboard.is_pressed('w')
 
    mouse.press(RMB)
    time.sleep(delay2)
    mouse.release(RMB)
    time.sleep(delay3)
    keyboard.press(mainKey)
    keyboard.press('w')
    time.sleep(delay1)
    mouse.press(RMB)
    time.sleep(delay3)
    mouse.release(RMB)
    time.sleep(delay3)
    keyboard.release('w')
    keyboard.release(mainKey)
    time.sleep(delay3)
    keyboard.press('s')
    keyboard.press(airRollKey)
    time.sleep(delay4)
    keyboard.press(mainKey)
    time.sleep(delay5)
    keyboard.release(mainKey)
    keyboard.release('s')
    time.sleep(delay6)
    keyboard.release(airRollKey)
 
    if lastW:
        keyboard.press('w')
 
    keyboard.release(hotKey)
 
    end = time.time() - start
    PrintBanner(endTime=end)

def diagonalKickOff(type):
    turnTime = 0.17

    if type == "left":
        keyboard.press('w')
        time.sleep(0.4)
        keyboard.press('a')
        time.sleep(turnTime)
        keyboard.release('a')
        time.sleep(0.0)
        DoSpeedFlip(right, airRollRight)
        keyboard.release('w')
        keyboard.press('d')
        time.sleep(0.3)
        keyboard.release('d')
    elif type == "right":
        keyboard.press('w')
        time.sleep(0.4)
        keyboard.press('d')
        time.sleep(turnTime)
        keyboard.release('d')
        time.sleep(0.0)
        DoSpeedFlip(left, airRollLeft)
        keyboard.release('w')
        keyboard.press('a')
        time.sleep(0.3)
        keyboard.release('a')

def sideKickOff(type):
    turnPressTime = 0.15
    turnPressTime2 = 0.05
    turnTime = 0.25
    straightTime = 0.3

    if type == "left":
        keyboard.press('w')
        time.sleep(straightTime)
        keyboard.press('d')
        time.sleep(turnPressTime)
        keyboard.release('d')
        time.sleep(turnTime)
        keyboard.press('a')
        time.sleep(turnPressTime2)
        keyboard.release('a')
        DoSpeedFlip(left, airRollLeft)
        keyboard.release('w')
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
    elif type == "right":
        keyboard.press('w')
        time.sleep(straightTime)
        keyboard.press('a')
        time.sleep(turnPressTime)
        keyboard.release('a')
        time.sleep(turnTime)
        keyboard.press('d')
        time.sleep(turnPressTime2)
        keyboard.release('d')        
        DoSpeedFlip(right, airRollRight)
        keyboard.release('w')
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
        
def straightKickOff():
    keyboard.press('w')
    time.sleep(0.6)
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')
    DoSpeedFlip(left, airRollLeft)
    keyboard.press('a')
    time.sleep(0.25)
    keyboard.release('a')
    time.sleep(0.2)

def ManageSpeedFlip(x):
    if keyboard.is_pressed('d'):
        DoSpeedFlip(right, airRollRight)
        time.sleep(0.3)
    elif keyboard.is_pressed('a'):
        DoSpeedFlip(left, airRollLeft)
        time.sleep(0.3)

def WallDash():
   time1 = 0.01
   for i in range(0, 15):
       mouse.press(RMB)
       time.sleep(time1)
       mouse.release(RMB)
       time.sleep(time1)
    

 
def ToggleRandomizer(x):
    global randomizer
    if randomizer == True:
        while i != 1:
            UpdateI()
        randomizer = False
    elif randomizer == False:
        randomizer = True
    PrintBanner()
 
 
keyboard.on_press_key(">", Increase)
keyboard.on_press_key("<", Decrease)
keyboard.on_press_key("/", ToggleRandomizer)
# keyboard.on_press_key(hotKey, ManageSpeedFlip)
 
while True:
    time.sleep(0.005)
    # if keyboard.is_pressed(hotKey2):
        # DoSpeedFlip(right, airRollRight)
        # time.sleep(0.3)
    # elif keyboard.is_pressed(hotKey):
        # DoSpeedFlip(left, airRollLeft)
        # time.sleep(0.3)
    if keyboard.is_pressed("8"):
        diagonalKickOff("left")
    if keyboard.is_pressed("9"):
        diagonalKickOff("right")
    if keyboard.is_pressed("5"):
        sideKickOff("left")
    if keyboard.is_pressed("6"):
        sideKickOff("right")
    if keyboard.is_pressed("+"):
        straightKickOff()
    if keyboard.is_pressed("/"):
        WallDash()

    