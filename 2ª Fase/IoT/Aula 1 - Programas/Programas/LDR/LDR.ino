int porta = A1;
int pinLed = 8;
int valor;
int claro = 350;

void setup() {
  Serial.begin(9600);
  pinMode(porta, INPUT);
  pinMode(pinLed, OUTPUT);
}

void loop() {
  valor = analogRead(porta);
  Serial.println(valor);
  if (valor < claro) {
    digitalWrite(pinLed, 1);
  }
  else {
    digitalWrite(pinLed, 0);
  }
}
