#include <Servo.h>
#uključujemo biblioteku za upravljanje servo motorima

#deklariramo polje od 5 servo objekata
Servo servos[5];

#pinovi Arduina na koje su spojeni servo motori
int pins[5] = {6, 5, 2, 12, 11};


#pokrećemo serijsku komunikaciju i svaki servo objekt povezujemo sa pripadajućim pinom
void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    servos[i].attach(pins[i]);
  }
}

#provjeravamo ima li podataka koji su stigli preko serijske veze
void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int lastComma = -1;
    int index = 0;

    # parsiramo brojeve iz stringa (razdvojene zarezima), pretvaramo ih u kut (×20) i šaljemo na servo motore
    for (int i = 0; i < input.length(); i++) {
      if (input[i] == ',' || i == input.length() - 1) {
        String numStr = input.substring(lastComma + 1, i + 1);
        int angle = numStr.toInt() * 20;

        #šaljemo izračunati kut odgovarajućem servo motoru
        servos[index].write(angle); 
        index++;
        lastComma = i;
      }
    }
  }
}
