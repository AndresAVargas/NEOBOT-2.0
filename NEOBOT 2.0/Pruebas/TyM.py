import curses
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the motor pins
IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
ENA = 32
ENB = 33

# Set the motor pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Create a PWM object for controlling the motor speed
pwm_1 = GPIO.PWM(ENA, 1000)
pwm_2 = GPIO.PWM(ENB, 1000)

# Start the PWM with a duty cycle of 50%
pwm_1.start(100)
pwm_2.start(100)
# Set the motor direction (clockwise or counterclockwise) delante

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(IN1, GPIO.HIGH)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.HIGH)
                GPIO.output(IN4, GPIO.LOW)
            elif char == curses.KEY_DOWN:
               GPIO.output(IN1, GPIO.LOW)
               GPIO.output(IN2, GPIO.HIGH)
               GPIO.output(IN3, GPIO.LOW)
               GPIO.output(IN4, GPIO.HIGH)
            elif char == curses.KEY_RIGHT:
                GPIO.output(IN1, GPIO.HIGH)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.LOW)
                GPIO.output(IN4, GPIO.LOW)
            elif char == curses.KEY_LEFT:
                GPIO.output(IN1, GPIO.LOW)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.HIGH)
                GPIO.output(IN4, GPIO.LOW)
            elif char == 10:
                GPIO.output(IN1,GPIO.LOW)
                GPIO.output(IN2,GPIO.LOW)
                GPIO.output(IN3,GPIO.LOW)
                GPIO.output(IN4,GPIO.LOW)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()