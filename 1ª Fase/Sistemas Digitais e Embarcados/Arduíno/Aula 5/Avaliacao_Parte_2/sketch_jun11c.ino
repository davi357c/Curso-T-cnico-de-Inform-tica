const int V_entrada = 11;
const int V_saida = 10;
const int H = 9;
const int A = 8;
const int botao_Lh = 5;
const int botao_Ll = 4;
const int botao_Th = 3;
const int botao_Tc = 2;

void setup() {
  pinMode(V_entrada, OUTPUT);
  pinMode(V_saida, OUTPUT);
  pinMode(H, OUTPUT);
  pinMode(A, OUTPUT);
  pinMode(botao_Ll, INPUT);
  pinMode(botao_Lh, INPUT);
  pinMode(botao_Th, INPUT);
  pinMode(botao_Tc, INPUT);

}

void loop() {
  bool Ll = digitalRead(botao_Ll);
  bool Lh = digitalRead(botao_Lh);
  bool Th = digitalRead(botao_Th);
  bool Tc = digitalRead(botao_Tc);
  if (Lh == 1) {
    digitalWrite(V_entrada, 0);
  }
  else {
    digitalWrite(V_entrada, 1);
  }
  if (Ll == 1 and Th == 0 and Tc == 0) {
    digitalWrite(V_saida, 1);
  }
  else {
    digitalWrite(V_saida, 0);
  }
  if (Tc == 1 and Th == 1) {
    digitalWrite(H, 0);
  }
  else if (Tc == 1) {
    digitalWrite(H, 1);
  }
  else {
    digitalWrite(H, 0);
  }
  if (Lh == 1 and Ll == 0) {
    digitalWrite(A, 1);
  }
  else if (Th == 1) {
    digitalWrite(A, 1);
  }
  else {
    digitalWrite(A, 0);
  }
}
