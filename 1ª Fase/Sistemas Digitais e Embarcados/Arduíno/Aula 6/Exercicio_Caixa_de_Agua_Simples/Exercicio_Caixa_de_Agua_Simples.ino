const int pin_STP = 4;
const int pin_STA = 3;
const int pin_STB = 2;
const int pin_IR = 10;
const int pin_M1 = 9;
const int pin_M2 = 8;

void setup() {
  pinMode(pin_STP, INPUT);
  pinMode(pin_STA, INPUT);
  pinMode(pin_STB, INPUT);
  pinMode(pin_IR, OUTPUT);
  pinMode(pin_M1, OUTPUT);
  pinMode(pin_M2, OUTPUT);
}

void loop() {
  bool STP = digitalRead(pin_STP);
  bool STA = digitalRead(pin_STA);
  if (STP == 0) {
    digitalWrite(pin_IR, 1);
  }
  else  {
    digitalWrite(pin_IR, 0);
  }
  if (STP == 1 and STA == 0) {
    digitalWrite(pin_M1, 1);
  }
  else  {
    digitalWrite(pin_M1, 0);
  }
  if (STP == 0 and STA == 0) {
    digitalWrite(pin_M2, 1);
  }
  else  {
    digitalWrite(pin_M2, 0);
  }

}
