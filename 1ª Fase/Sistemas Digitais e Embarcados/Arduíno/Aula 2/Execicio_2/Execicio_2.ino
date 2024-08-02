const int pin_botao = 6;
const int pin_led = 7;
bool botao = true;

void setup() {
  Serial.begin(9600);
  pinMode(pin_botao, INPUT);
  pinMode(pin_led, OUTPUT)

}

void loop() {
  botao = digitalRead(pin_botao);
  if(botao==true) {
    Serial.println("Botão pressionado!!!!!");
  }

}
