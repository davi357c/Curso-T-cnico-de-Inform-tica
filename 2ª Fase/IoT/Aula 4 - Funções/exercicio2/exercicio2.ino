#include <Ultrasonic.h>
Ultrasonic ultrasonic(12, 13);
float distancia;

#include <Servo.h>
Servo cancela;

int pinBotao = 8;
int pinServo = 9;
bool aux = 0;
unsigned long tempoAnterior = 0;

void setup() {
  pinMode(pinBotao, INPUT);
  cancela.attach(pinServo);
  Serial.begin(9600);
}

void loop() {
  distancia = ultrasonic.read();
  bool botao = digitalRead(pinBotao);
  if (distancia <= 8) {
    switch (aux) {
      case 0:
        Serial.println("Aperte o botão");
        aux = 1;
        break;
      case 1:
        if (botao == 1) {
          Serial.println("Sim");
          cancela.write(90);
          break;
        }
    }
  }
  else {
    if (millis() - tempoAnterior >= 1000 && aux == 1) {
      tempoAnterior = millis();
      cancela.write(0);
      aux = 0;
    }
  }
}
