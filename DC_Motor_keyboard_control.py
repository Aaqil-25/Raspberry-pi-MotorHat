#This code is written by Aaqil-25

from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import sys, tty, termios, time

mh = Raspi_MotorHAT(addr=0x6f)
m1 = mh.getMotor(1)
m2 = mh.getMotor(2)

#you have to choose the speed based on the each motor movement distance for a perticuler time
m1.setSpeed(80)
m2.setSpeed(100)

def forward(sec):
    m1.run(Raspi_MotorHAT.FORWARD);
    m2.run(Raspi_MotorHAT.FORWARD);
    time.sleep(sec);
    m1.run(Raspi_MotorHAT.RELEASE);
    m2.run(Raspi_MotorHAT.RELEASE);
def reverse(sec):
    m1.run(Raspi_MotorHAT.BACKWARD);
    m2.run(Raspi_MotorHAT.BACKWARD);
    time.sleep(sec);
    m1.run(Raspi_MotorHAT.RELEASE);
    m2.run(Raspi_MotorHAT.RELEASE);
def right_turn(sec):
    m1.run(Raspi_MotorHAT.FORWARD);
    m2.run(Raspi_MotorHAT.BACKWARD);
    time.sleep(sec);
    m1.run(Raspi_MotorHAT.RELEASE);
    m2.run(Raspi_MotorHAT.RELEASE);
def left_turn(sec):
    m1.run(Raspi_MotorHAT.BACKWARD);
    m2.run(Raspi_MotorHAT.FORWARD);
    time.sleep(sec);
    m1.run(Raspi_MotorHAT.RELEASE);
    m2.run(Raspi_MotorHAT.RELEASE);
def close(sec):
    m1.run(Raspi_MotorHAT.RELEASE);
    m2.run(Raspi_MotorHAT.RELEASE);
    
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
   
    char = getch()
    seconds= 0.15
# when letter  'w' pressed the  vehicle move Forward
    if(char == "w"):
        forward(seconds)

 # when letter  's' pressed the  vehicle move Reverse  
    if(char == "s"):
        reverse(seconds)
        
 # when letter  'a' pressed the  vehicle take Left-Turn  
    if(char == "a"):
        left_turn(seconds)

# when letter  'd' pressed the  vehicle take Right-Turn    
    if(char == "d"):
        right_turn(seconds)


# if 'x' is pressed the  code will stop running and motor will also stop the movement
    if(char == "x"):
        close(seconds)
        print("Program Ended")
        break

    
        char = ""