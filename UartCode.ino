#include <Servo.h>

Servo servos[5];
int pins[5] = {6, 5, 2, 12, 11};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    servos[i].attach(pins[i]);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int lastComma = -1;
    int index = 0;

    for (int i = 0; i < input.length(); i++) {
      if (input[i] == ',' || i == input.length() - 1) {
        String numStr = input.substring(lastComma + 1, i + 1);
        int angle = numStr.toInt() * 20;

        servos[index].write(angle); 
        index++;
        lastComma = i;
        if (index >= 5);
      }
    }
  }
}