const int BP = 10;
const int BR = 9;
const int IR = 8;
const int botao_SNA = 4;
const int botao_SNB = 3;
const int botao_STP = 2;
bool aux_SNA = 0;
bool aux_SNB = 0;
bool aux_STP = 0;
bool estado_SNA = 1; 
bool estado_SNB = 1; 
bool estado_STP = 0;

void setup() {
  pinMode(BP, OUTPUT);
  pinMode(BR, OUTPUT);
  pinMode(IR, OUTPUT);
  pinMode(botao_SNA, INPUT);
  pinMode(botao_SNB, INPUT);
  pinMode(botao_STP, INPUT);

}

void loop() {
  bool SNA = digitalRead(botao_SNA);
  bool SNB = digitalRead(botao_SNB);
  bool STP = digitalRead(botao_STP);
  if (SNA == 1) {
    if (aux_SNA == 0) {
      aux_SNA = 1;
      estado_SNA = !estado_SNA;
    }
  }
  else {
    aux_SNA = 0;
  }
  if (SNB == 1) {
    if (aux_SNB == 0) {
      aux_SNB = 1;
      estado_SNB = !estado_SNB;
    }
  }
  else {
    aux_SNB = 0;
  }
  if (STP == 1) {
    if (aux_STP == 0) {
      aux_STP = 1;
      estado_STP = !estado_STP;
    }
  }
  else {
    aux_STP = 0;
  }
  if (estado_SNA == 1) {
    digitalWrite(BP, 0);
    digitalWrite(BR, 0);
    digitalWrite(IR, 0);
  }
  else if (estado_SNA == 0) {
    if (estado_STP == 1) {
      digitalWrite(BP, 1);
      digitalWrite(BR, 0);
      digitalWrite(IR, 0);
    }
    else {
      digitalWrite(BP, 0);
      digitalWrite(BR, 1);
      digitalWrite(IR, 1);
    }
  }

}
