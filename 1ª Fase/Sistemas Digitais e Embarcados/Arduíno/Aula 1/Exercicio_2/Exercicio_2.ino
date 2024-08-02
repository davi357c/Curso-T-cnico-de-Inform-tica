void setup() { 
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);

}

void loop() {
  digitalWrite(7, 1);
  delay(1000);
  digitalWrite(7, 0);
  digitalWrite(6, 1);
  delay(1000);
  digitalWrite(6, 0);
  digitalWrite(5, 1);
  delay(1000);
  digitalWrite(5, 0);

}
