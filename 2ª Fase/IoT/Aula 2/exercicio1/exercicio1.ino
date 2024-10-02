const int pinLed = 9;
int k;

void setup() {
  pinMode(pinLed, OUTPUT);
}

void loop() {
  for (k = 0; k <= 255; k++) {
    analogWrite(pinLed, k);
    delay(4);
  }
  for (k = 255; k >= 0; k--) {
    analogWrite(pinLed, k);
    delay(4);
  }
}

