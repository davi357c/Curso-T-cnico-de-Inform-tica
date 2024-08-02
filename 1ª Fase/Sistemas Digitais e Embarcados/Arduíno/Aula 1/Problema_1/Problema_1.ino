int valor = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Digite um número: ");
}

void loop() {
  if(Serial.available()) {
    valor = Serial.read();
    Serial.print("O número digitado foi: ");
    Serial.write(valor);
    Serial.println();
    delay(2000);
  }
}
