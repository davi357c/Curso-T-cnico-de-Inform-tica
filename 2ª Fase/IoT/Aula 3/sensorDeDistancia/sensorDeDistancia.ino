#include <Ultrasonic.h>
Ultrasonic ultrasonic(12, 13);
const int ledRed = 10;
const int ledGreen = 8;
const int ledBlue = 9;
int distance;

void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledBlue, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  distance = ultrasonic.read();
  Serial.print("Distance in CM: ");
  Serial.println(distance);
  if (distance <= 10) {
    digitalWrite(ledRed, 1);
    digitalWrite(ledBlue, 0);
    digitalWrite(ledGreen, 0);
  }
  else if (distance > 10 && distance <= 50) {
    digitalWrite(ledRed, 0);
    digitalWrite(ledBlue, 1);
    digitalWrite(ledGreen, 0);
  }
  else {
    digitalWrite(ledRed, 0);
    digitalWrite(ledBlue, 0);
    digitalWrite(ledGreen, 1);
  }
}
