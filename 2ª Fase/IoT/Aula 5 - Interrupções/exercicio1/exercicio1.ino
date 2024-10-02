const byte ledPin = 13;
const byte interruptPin = 2;
volatile byte state = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, RISING); // CHANGE, RISING, FALLING, LOW
}

void loop() {
  digitalWrite(ledPin, state);
}

void blink() {
  state = !state;
}
