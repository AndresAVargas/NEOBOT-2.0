// Adafruit Motor shield library
#include <AFMotor.h>

// Define motor on channel 3
AF_DCMotor motor(3);

const int greenLed = 30; 
const int redLed = 32;
int incomingData;      

void setup() {
  // initialize serial communication
  Serial.begin(9600);
  // initialize the LED pin as an output
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);

  // speed - Valid values for 'speed' are between 0 and 255 with 0 being off and 255 as full throttle
  motor.setSpeed(200);
  // RELEASE - Stop the motor. This removes power from the motor and is equivalent to setSpeed(0)
  motor.run(RELEASE);
}

void loop() {
  // see if there's incoming serial data
  if (Serial.available() > 0) {
    
    incomingData = Serial.read();
    
    if (incomingData == 'F') {
      motor.run(FORWARD);
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
    }

    if (incomingData == 'R') {
      motor.run(BACKWARD);
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
    }
    
    if (incomingData == 'Q') {
      motor.run(RELEASE);
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, LOW);
    }
  }
}
