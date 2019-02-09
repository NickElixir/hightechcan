int pwm;
unsigned long time_chash=0;
void setup() 
{
    Serial.begin(9600);
    pinMode(A2,INPUT);
    pinMode(9,OUTPUT);
}
void loop() 
{
    if(millis()-time_chash == 100)
    {
        time_chash=millis();
        pwm = analogRead(A2);
        pwm=map(pwm,0,1023,0,255);
        Serial.println(pwm);
        analogWrite(9,pwm);
    }
}
