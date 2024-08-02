const int button_00 = 2;
const int button_01 = 3;
const int led_00 = 8;
const int led_01 = 9;
const int led_02 = 10;
const int led_03 = 11;
const int intervalo_00 = 1000;
unsigned long ant_time = 0;
bool estado = 0;
unsigned long now_time = 0;

void setup() {
  pinMode(button_00, INPUT);
  pinMode(button_01, INPUT);
  pinMode(led_00, OUTPUT);
  pinMode(led_01, OUTPUT);
  pinMode(led_02, OUTPUT);
  pinMode(led_03, OUTPUT);

}

void loop() {
  bool b0 = digitalRead(button_00);
  bool b1 = digitalRead(button_01);
  now_time = millis();
  if (b0 == 1) {
    estado = 1;
  }
  if (b1 == 1) {
    estado = 0;
    digitalWrite(led_00, 0);
    digitalWrite(led_01, 0);
    digitalWrite(led_02, 0);
    digitalWrite(led_03, 0);
  }
  if (estado == 1) {
    if (now_time - ant_time >= 1000) {
      digitalWrite(led_00, estado);
      if (now_time - ant_time >= 1500) {
        digitalWrite(led_01, estado);
        if (now_time - ant_time >= 1750) {
          digitalWrite(led_02, estado);
          if (now_time - ant_time >= 2250) {
            digitalWrite(led_03, estado);
            if (now_time - ant_time >= 3250) {
              ant_time = now_time;
              digitalWrite(led_00, 0);
              digitalWrite(led_01, 0);
              digitalWrite(led_02, 0);
              digitalWrite(led_03, 0);
            }
          }
        }
      }
    }
  }
  else if (estado == 0) {
    ant_time = now_time;
  }
}
