const int pinLed = 9;
const int pinPotenciometro = A0;
int x;

void setup() {
  pinMode(pinPotenciometro, INPUT);
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  x = analogRead(pinPotenciometro);
  x = map(x, 0, 1023, 0, 255);
  analogWrite(pinLed, x);

}
