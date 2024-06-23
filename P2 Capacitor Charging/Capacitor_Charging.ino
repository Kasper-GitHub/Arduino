int SensorVal = 0;
int powerLED = 13;
int statusLED = 8;
float voltage = 0.0;

long unsigned now = 0.0;
long unsigned then = 0.0;
long unsigned elapsed = 0.0;

void setup()
{
  Serial.begin(9600);
  pinMode(powerLED, OUTPUT);
  pinMode(statusLED, OUTPUT);
  digitalWrite(powerLED, LOW);
  digitalWrite(statusLED, LOW);
  delay(10000);
  digitalWrite(powerLED, HIGH);
  then = millis();
}

void loop()
{
  while(voltage != 5.0)  {
    SensorVal = analogRead(A0);
    now = millis();
    voltage = (5.0/1023.0)*SensorVal;
    elapsed = now - then;
    Serial.print(elapsed);
    Serial.print("\t");
    Serial.println(voltage);
  }

  digitalWrite(powerLED, LOW);
  digitalWrite(statusLED, HIGH);
}