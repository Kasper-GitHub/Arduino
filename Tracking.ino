void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(12,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int x=digitalRead(12);
  Serial.println(x);
  delay(100);
}
