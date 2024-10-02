int aux = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Fazer mutiplicação!!!");
}

void loop() {
  int n1;
  int n2;
  Serial.print("Digite seu primeiro número: ");
  while(1) {
    if (Serial.available() > 0) {
      n1 = Serial.parseInt();
      Serial.println(n1);
      break;
    }
  }
  Serial.print("Digite seu segundo número: ");
  while(1) {
    if (Serial.available() > 0) {
      n2 = Serial.parseInt();
      Serial.println(n2);
      break;
    }
  }
  Serial.print("O resultado é: ");
  Serial.println(multiplicacao(n1, n2));
}

int multiplicacao(int x, int y) {
  int resultado = 0;
  for (int v = 0; v < y; v++) {
    resultado += x;
  }
  return resultado;
}