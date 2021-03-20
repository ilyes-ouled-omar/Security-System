int pin1=2; //vers 36 de la carte raspberry
int pin2=3; //vers 38
int pin3=4; //vers 40
int tempCapture = A0;
int LIGHT = A1;
int GasPin = A2;
float tmprVal = 0;
unsigned long tepTimer;
void setup(void) {
Serial.begin(9600); 
pinMode(pin1, OUTPUT); 
pinMode(pin2, OUTPUT);
pinMode(pin3, OUTPUT);
digitalWrite(pin1,0);
digitalWrite(pin2,0);
digitalWrite(pin3,0);
}
void loop(void) {
int valT = analogRead(tempCapture);
int valL = analogRead(LIGHT);
int valG = analogRead(GasPin);
tmprVal = (float) valT * (5 / 10.24); 
if (tmprVal > 37) { 
digitalWrite(pin1,1);
digitalWrite(pin2,0);
digitalWrite(pin3,0);
delay(2);
}

if(tmprVal < 37) { 
digitalWrite(pin1,0);
digitalWrite(pin2,0);
digitalWrite(pin3,0);
delay(2);
}
if (millis() - tepTimer > 50) { 
tepTimer = millis();
Serial.print("temperature: ");
Serial.print(tmprVal);
Serial.println("C");
delay(500);
}

if (valL < 700) { 
digitalWrite(pin1,0);
digitalWrite(pin2,0);
digitalWrite(pin3,0);
delay(10);
}
if (valL > 700) {
digitalWrite(pin1,0);
digitalWrite(pin2,1);
digitalWrite(pin3,0);
delay(10);
}
if (valG<800){
digitalWrite(pin1,0);
digitalWrite(pin2,0);
digitalWrite(pin3,0);  
delay(20);
}
if (valG>800){
digitalWrite(pin1,0);
digitalWrite(pin2,0);
digitalWrite(pin3,1);
delay(20);
}
if ((tmprVal > 37)&&(valL > 700)&&(valG > 800)){
  digitalWrite(pin1,1);
digitalWrite(pin2,1);
digitalWrite(pin3,1);
}
if ((tmprVal > 37)&&(valL < 700)&&(valG > 800)){
  digitalWrite(pin1,1);
digitalWrite(pin2,0);
digitalWrite(pin3,1);
}
if ((tmprVal < 37)&&(valL > 700)&&(valG > 800)){
  digitalWrite(pin1,0);
digitalWrite(pin2,1);
digitalWrite(pin3,1);
}
if ((tmprVal > 37)&&(valL > 700)&&(valG < 800)){
  digitalWrite(pin1,1);
digitalWrite(pin2,1);
digitalWrite(pin3,0);
}

delay(50);  
}

