const int pin_entrada = A0;
const int pinLed = 8;
int valor;
float tensao;

void setup() {
  Serial.begin(9600);
  pinMode(pin_entrada, INPUT);
  pinMode(pinLed, OUTPUT);
}

void loop() {
  valor = analogRead(pin_entrada);
  tensao = float(valor)*5/1023;
  Serial.print("Tensao = ");
  Serial.print(tensao);
  Serial.println(" V");
  if (tensao > 2.5) {
      digitalWrite(pinLed, 1);
  }
  else {
    digitalWrite(pinLed, 0);
  }
}
