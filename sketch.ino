#include <Servo-master/Servo-master/src/Servo.h>



Servo myservo;
Servo myservo2;
void setup(){
	myservo.attach(9);
  	myservo2.attach(8);
	myservo.read();
}
void loop(){
	myservo.write(90);
  	
  	delay(1000);
	myservo.write(360);
  	delay(1000);
  	myservo.write(90);
  	delay(1000);
  	myservo.write(0);
  	delay(1000);
  	myservo2.write(90);
  	
  	delay(1000);
	myservo2.write(360);
  	delay(1000);
  	myservo2.write(90);
  	delay(1000);
  	myservo2.write(0);
  	delay(1000);
}