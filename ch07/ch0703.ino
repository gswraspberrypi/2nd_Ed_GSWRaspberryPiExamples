void setup() {
 Serial.begin(9600);
}

void loop() {
  int n = analogRead(0);
  Serial.println(n, DEC); 
  delay(100);
}