const int botao_i0 = 2;
const int botao_i1 = 3;
const int led_d0 = 11;
const int led_d1 = 10;
const int led_d2 = 9;
const int led_d3 = 8;
bool aux1 = 0;
bool aux2 = 0;
unsigned char counter = 0;

void setup() {
  pinMode(botao_i0, INPUT);
  pinMode(botao_i1, INPUT);
  pinMode(led_d0, OUTPUT);
  pinMode(led_d1, OUTPUT);
  pinMode(led_d2, OUTPUT);
  pinMode(led_d3, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  bool i0 = digitalRead(botao_i0);
  bool i1 = digitalRead(botao_i1);
  if (i0 == 1) {
    if (aux1 == 0) {
      aux1 = 1;
      counter+=1;
      if (counter>15) {
        counter = 0;
      }
      Serial.println(counter);
    }
  }
  else {
    aux1 = 0;
  }
  if (i1 == 1) {
    if (aux2 == 0) {
      aux2 = 1;
      counter-=1;
      if (counter>15) {
        counter = 15;
      }
      Serial.println(counter);
    }
  }
  else {
    aux2 = 0;
  }
}