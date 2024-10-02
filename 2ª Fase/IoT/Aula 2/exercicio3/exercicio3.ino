int valor;
int brilho;
int pinRed = 11;
int pinGreen = 10;
int pinBlue = 9;
int aux = 0;

void setup() {
  pinMode(pinRed, OUTPUT);
  pinMode(pinGreen, OUTPUT);
  pinMode(pinBlue, OUTPUT);
  Serial.begin(9600);
  Serial.println();
  Serial.println("Digite um valor entre 1 (brilho minimo) e 255 (brilho maximo):");
  Serial.println();
}

void loop() {
  valor = Serial.parseInt();
  if (Serial.available()>0) {
    Serial.print("Valor lido: ");
    Serial.println(valor);
    if (valor != 0) {
      if (aux == 0) {
        analogWrite(pinRed, valor);
        aux = 1;
      }
      else if (aux == 1) {
        analogWrite(pinGreen, valor);
        aux = 2;
      }
      else if (aux == 2) {
        analogWrite(pinBlue, valor);
        aux = 0;
      }
    }
  }
}
