const int button_00 = 2;
const int led_00 = 8;
const int led_01 = 9;
bool estado = 0;
unsigned long ant_time = 0;
const long intervalo = 1000;
bool aux = 0;
unsigned long now_time = 0;

void setup() {
  pinMode(button_00, INPUT);
  pinMode(led_00, OUTPUT);
  pinMode(led_01, OUTPUT);
}

void loop() {
  bool b0 = digitalRead(button_00);
  if (b0 == 1) {
    if (aux == 0) {
      aux = 1;
      estado = !estado;
      if (estado == 1) {
        digitalWrite(led_00, 1);
        unsigned long now_time = millis();
        now_time = ant_time;
      }
    }
  }
  else {
    aux = 0;
    digitalWrite(led_00, 0);
    digitalWrite(led_01, 0);
  }
  if (now_time - ant_time >= intervalo) {
    digitalWrite(led_01, 1);
  }
}
