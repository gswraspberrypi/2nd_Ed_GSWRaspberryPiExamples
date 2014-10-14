
void setup() {
 Serial.begin(9600);
}

void loop() {
 for (int n = 0; n < 1024; n++)
   Serial.println(n, DEC); 
   delay(50);
  }
}