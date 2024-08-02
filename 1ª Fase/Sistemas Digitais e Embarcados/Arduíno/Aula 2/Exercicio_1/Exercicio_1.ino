const int led_red = 7;
const int led_green = 6;
const int led_blue = 5;
char value;

void setup() {
  Serial.begin(9600);
  pinMode(led_red, OUTPUT);
  pinMode(led_green, OUTPUT);
  pinMode(led_blue, OUTPUT);

}

void loop() {
  if(Serial.available()) {
    value = Serial.read();
    switch(value) {
      case 'R':
        digitalWrite(led_red, 1);
        break;
      case 'r':
        digitalWrite(led_red, 0);
        break;
      case 'G':
        digitalWrite(led_green, 1);
        break;
      case 'g':
        digitalWrite(led_green, 0);
        break;
      case 'B':
        digitalWrite(led_blue, 1);
        break;
      case 'b':
        digitalWrite(led_blue, 0);
        break;
      default:
        Serial.print("Invalid value");
        break;
    }
  }

}
