from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#############################################################
# Deklarationen
#############################################################

hub = PrimeHub()

#left motor - port F
#right motor - port B
#left usbl motor 1 - port E 
#right usbl motor 2 - port A
#color sensor - port C

left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
left_tool_motor = Motor(Port.E)
right_tool_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.C)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=95)

drive_base.use_gyro(True)
counter =  0
Klammer_Fahrt = 0 



#############################################################
# Funktionen
#############################################################

'''
Liftgabel aufwärts rotieren
''' 

def lift_up(x):
    left_tool_motor.run_angle(500,x)

'''
Liftgabel abwärts rotieren
''' 

def lift_down(x):
    left_tool_motor.run_angle(500,x)

'''
 warten bis ein knopf gedrückt wird
'''

def warten():
    while not any(hub.buttons.pressed()):
        None

'''
die Greifarme Öffnen
'''
def grap_open(oe):
    right_tool_motor.run_angle(300, oe,wait=False)
    left_tool_motor.run_angle(300, -oe)

'''
die Greifarme Schliessen
'''
def grap_close(schl):
    left_tool_motor.run_angle(300, -schl,wait=False)
    right_tool_motor.run_angle(300, schl)

#############################################################
# Fahrten
#############################################################

'''
das U-bot Lösen
'''
def UBot():
    #in richtung U-Bot drehen
    drive_base.straight(300)
    drive_base.turn(55)
    drive_base.settings(300,150,150,90)
    #die flagge runter machen
    lift_down(-65)
    drive_base.straight(120)
    lift_up(65)
    drive_base.settings(700,300,150,90)
    drive_base.straight(-120)
    drive_base.turn(-55)
    

'''
den gelben Balken in das Wrack schieben
'''  
def flip_anglerfisch():
    drive_base.straight(360)
    drive_base.turn(50)



            
'''
Losfahren in der Base
Plankton Probe herausziehen
'''            
def pull_plankton():
    drive_base.use_gyro(True)
    left_tool_motor.run_until_stalled(300,duty_limit=30)
    drive_base.settings(700,300,150,90)
    #aus der base losfahren
    drive_base.straight(400)
    drive_base.turn(-25)
    drive_base.straight(360)
    drive_base.settings(400,150,100,50)
    #in richtung der probe drehen
    drive_base.turn(114)
    drive_base.settings(700,300,150,90)
    drive_base.straight(50)
    drive_base.turn(-8)
    #die probe ziehen
    lift_down(-130)
    drive_base.straight(-100)
    lift_up(130)
    drive_base.straight(90)
    #in richtung spielfeld inneres drehen
    drive_base.turn(-172)
    drive_base.straight(60)

'''
aus der base losfahren und die einzelnen teile einsammeln
'''
def Sammeln1():
    left_tool_motor.run_until_stalled(200,duty_limit=40)
    right_tool_motor.run_until_stalled(-200,duty_limit=40)
    #kalibriert die Liftgabel
    drive_base.curve(245,45)
    drive_base.straight(105)
    drive_base.curve(250,-45)
    # S - Kurve
    drive_base.straight(100)
    grap_close(135)
    # Alles eingesammelt
    drive_base.turn(35)
    drive_base.use_gyro(False)
    drive_base.straight(-750)

'''
Den Hai Schiff und das Korallenriff lösen
'''
def Hai():
    #kalibriert die Liftgabel
    drive_base.use_gyro(True)
    left_tool_motor.run_until_stalled(-300,duty_limit=30)
    right_tool_motor.run_until_stalled(300,duty_limit=30)
    # S - Kurve
    drive_base.curve(245,45)
    drive_base.straight(105)
    drive_base.curve(250,-45)
    drive_base.straight(100)
    #Den Masst stellen
    drive_base.turn(38)
    drive_base.curve(200,45)
    # Korallen aufstellen
    drive_base.curve(-800,-15)
    drive_base.straight(-300)
    # Hai auslösen
    drive_base.straight(30)
    drive_base.turn(60)
    drive_base.settings(950, 1000)
    drive_base.straight(-250)
    #zurück in die Base
    drive_base.straight(250)
    drive_base.turn(25)
    drive_base.use_gyro(False)
    drive_base.curve(500, 55)
    drive_base.stop()


def fahrt1():
     
    warten()
    Sammeln1()
    warten()
    Hai()
    drive_base.settings(700,300,150,90)
    
    drive_base.use_gyro(False)
    

            #plankton
           # pull_plankton()

            #plankton
        #    pull_plankton()
            

            #Fahrt zum Anglersfisch-Wrack - S Kurve
         ##   flip_anglerfisch()
            #fahrt zum bumenbet
        #    Blumenbet()
            #Lösung des U-Botes
         #   UBot()
            #Ausrichten zur Meeresbodenprobe
          #  pull_meeresbodenprobe()
           # Back_to_Base1()
         
         
def fahrt2():
    warten()
    left_tool_motor.run_until_stalled(-300,duty_limit=30)
    right_tool_motor.run_until_stalled(300,duty_limit=30)
    drive_base.use_gyro(True)
    drive_base.curve(200,90)
    drive_base.straight(1000)
    drive_base.use_gyro(False)
    drive_base.straight(450)
    drive_base.stop()
        
def fahrt3():
    warten()
    drive_base.use_gyro(True)
    left_tool_motor.run_until_stalled(-300,duty_limit=30)
    right_tool_motor.run_until_stalled(300,duty_limit=30)
    drive_base.settings(400,300,150,90)
    drive_base.straight(420)
    wait(150)
    drive_base.settings(700,300,150,90)
    drive_base.use_gyro(False)
    drive_base.straight(-500)

def fahrt4():
    drive_base.use_gyro(True)
    warten()
    left_tool_motor.run_until_stalled(300,duty_limit=30)
    right_tool_motor.run_until_stalled(-300,duty_limit=30)
    drive_base.curve(700,-30)
    drive_base.curve(280,30)
    drive_base.straight(100)
    grap_close(135)
    drive_base.straight(-300)
    drive_base.turn(-45)
    drive_base.straight(-350)
    drive_base.stop()


def fahrt5():
    pull_plankton()
    #flip_anglerfisch()
    UBot()
    #pull_meeresbodenprobe()

def fahrt6():
    warten()
    drive_base.use_gyro(True)
    left_motor.run_until_stalled(100, duty_limit=30)
    drive_base.settings(200,200,120,90)
    drive_base.straight(80)
    drive_base.curve(300,-45)
    drive_base.curve(300, 89)
    drive_base.straight(140)
    left_tool_motor.run_angle(-100, 100)
    left_tool_motor.run_angle(100, 100)
    left_tool_motor.run_angle(-100, 100)
    left_tool_motor.run_angle(100, 100)
    drive_base.straight(-130)
    drive_base.curve(-250, 89)
    drive_base.curve(-300,-45)
    drive_base.turn(-45)
    drive_base.use_gyro(False)
    drive_base.straight(-400)
    
def fahrt7():
    drive_base.settings(100,50,50,50)
    drive_base.use_gyro(False)
    drive_base.straight(90)
    drive_base.straight(-150)


#############################################################
# Main
#############################################################

Klammer_Fahrt = 0
def old():
    while True:
        print(hub.battery.voltage())
        print(color_sensor.color())
        if(Klammer_Fahrt == 0):
            fahrt1()
            Klammer_Fahrt = 1
        elif(color_sensor.color() == Color.BLUE and Klammer_Fahrt == 1):
            fahrt2()
            Klammer_Fahrt = 2
        elif(color_sensor.color() == Color.BLUE and Klammer_Fahrt == 2):
            fahrt3()
            Klammer_Fahrt = 3
        elif(color_sensor.color() == Color.BLUE and Klammer_Fahrt == 3):
            fahrt4()
            Klammer_Fahrt = 4
        elif(color_sensor.color() == Color.RED):
            warten()
            fahrt5()
        elif(color_sensor.color() == Color.GREEN):
            fahrt6()
        elif(color_sensor.color() == Color.WHITE):
            warten()
            fahrt7()
    
while True:
        print(hub.battery.voltage())
        print(color_sensor.color())
        
        fahrt1()   
        fahrt2()
        fahrt3()
        fahrt4()
        fahrt6()
        warten()
        fahrt7() 
        warten()
        fahrt5()




