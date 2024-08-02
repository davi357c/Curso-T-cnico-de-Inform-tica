const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 11;
const int led_d1 = 10;
const int led_d2 = 9;
const int led_d3 = 8;
bool aux = 0;
bool state = 0;


void setup() {
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);
  pinMode(led_d1, OUTPUT);
  pinMode(led_d2, OUTPUT);
  pinMode(led_d3, OUTPUT);

}

void loop() {
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);

  if (i0 == 1) {
    if (aux == 0) {
      aux = 1;
      state = !state;
    }
  }  
  else {
    aux = 0;
  }
  digitalWrite(led_d0, state);
}