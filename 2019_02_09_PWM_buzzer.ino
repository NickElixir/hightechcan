int pwm;
void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  pwm = analogRead(A2);
  pwm=map(pwm,0,1023,0,255);
  Serial.println(pwm);
  analogWrite(10,pwm);
  delay(100);
}
