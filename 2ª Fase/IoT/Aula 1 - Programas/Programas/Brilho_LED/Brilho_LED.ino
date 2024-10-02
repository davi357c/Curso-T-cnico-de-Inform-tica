int valor;
int brilho;
int porta = 11;

void setup() {
  pinMode(porta, OUTPUT);
  Serial.begin(9600);
  Serial.println("Digite um valor entre 0 (brilho minimo) e 255 (brilho maximo):");
  Serial.println();
}

void loop() {
  if (Serial.available() > 0) {
    valor = Serial.parseInt();
    Serial.print("Valor lido: ");
    Serial.println(valor);
    analogWrite(porta, valor);
  }
}
