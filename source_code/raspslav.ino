#include <Adafruit_PWMServoDriver.h>
#include <Wire.h>

//sudo chmod a+rw /dev/ttyACM0 
Adafruit_PWMServoDriver driver = Adafruit_PWMServoDriver();
#define gripMin 125
#define gripMax 550 //resting
#define wristMin 300
#define wristMax 670 //resting
#define elbowMin 125
#define elbowMax 630
#define shoulderLMin 125 //resting
#define shoulderLMax 500
#define shoulderRMin 200
#define shoulderRMax 600 //resting

int gripServo = 15;
int wristRotServo = 3;
int wristServo = 4;
int elbowServo = 2;
int shoulderLServo = 0;
int shoulderRServo = 1;



const int lpwm = 9 ; //initializing pin 2 as pwm
const int lin_1 = 10 ;
const int lin_2 = 11 ;
//Serial.begin(9600);   
const int rpwm = 5 ; //initializing pin 4 as pwm
const int rin_1 = 6 ;
const int rin_2 = 7 ;

const int pininput1  = 2; 
const int pininput2  = 3; 
const int pininput3 = 4;

int input1 ;
int input2 ;
int input3 ;

void forward();
void stop();
void right();
void left();
void backward();

void resting_pos();
void gripping();
void wristForward();
void elbowForward();
void picking_pos();

void setup() {
  // put your setup code here, to run once:
   pinMode(lpwm,OUTPUT) ; //we have to set PWM pin as output
   pinMode(lin_1,OUTPUT) ; //Logic pins are also set as output
   pinMode(lin_2,OUTPUT) ;
   pinMode(rpwm,OUTPUT) ; //we have to set PWM pin as output
   pinMode(rin_1,OUTPUT) ; //Logic pins are also set as output
   pinMode(rin_2,OUTPUT) ;
   pinMode(pininput1,INPUT) ; 
   pinMode(pininput2,INPUT) ;
   pinMode(pininput3,INPUT) ;
   driver.begin();
   driver.setPWMFreq(60); 
   Serial.begin(9600);
}

void loop() {
  input1=LOW;
  input2=LOW;
  input3 = HIGH;
  analogWrite(lpwm,255);
  analogWrite(rpwm,255);
//  input1 = digitalRead(pininput1);
//  input2 = digitalRead(pininput2);
//  input3 = digitalRead(pininput3);
  Serial.println(input1);
  Serial.println(input2);
  analogWrite(lpwm,255) ;
  analogWrite(rpwm,255) ;

  picking_pos();
    
  if(input1 == HIGH && input2 == HIGH && input3 == HIGH){
      forward();
    }
  else if(input1 == HIGH && input2 == HIGH && input3 == LOW){
      backward();
    }
    
  else if(input1 == HIGH && input2 == LOW && input3 == HIGH){
      left();
    }
   else if(input1 == LOW && input2 == HIGH && input3 == HIGH){
      right();
    }
  else if(input1 == LOW && input2 == LOW && input3 == HIGH) {
      stop();
    }
  else if(input1 == HIGH && input2 == LOW && input3 == LOW) {
      picking_pos();
    }
    
}

void shoulderForward(){
  int pulse1 = 300;
  int pulse2 = 400;
  driver.setPWM(shoulderLServo, 0, pulse1);
  driver.setPWM(shoulderRServo, 0, pulse2);
}

void picking_pos(){
  int shoulderL_pos = 200;
  int shoulderR_pos = 500;
  int shoulderL_pos2 = 150;
  int shoulderR_pos2 = 550;
  int elbow_pos = 120;
  int wrist_pos = wristMax;
  int gripper_pos = gripMax;

  
  driver.setPWM(shoulderLServo, 0, shoulderLMin);
  delay(300);
  driver.setPWM(shoulderRServo, 0, shoulderRMax);
  delay(300);
  driver.setPWM(elbowServo, 0, elbowMax);
  delay(300);
  driver.setPWM(wristServo, 0, wristMax+50);
  delay(300);
  driver.setPWM(gripServo, 0, gripMin);
  delay(300);
  
  //Standing up
  driver.setPWM(shoulderLServo, 0, shoulderL_pos);
  driver.setPWM(shoulderRServo, 0, shoulderR_pos);
  delay(300);
  
  for(int pulse=wristMin; pulse<(wristMax-180); pulse+=5){
  driver.setPWM(wristServo, 0, pulse);
  delay(200);
  }

  delay(300);
  //driver.setPWM(shoulderLServo, 0, shoulderLMin);
  //driver.setPWM(shoulderRServo, 0, shoulderRMax);
  
  delay(300);
  for(int pulse=elbowMax; pulse>elbowMin; pulse-=5){
  driver.setPWM(elbowServo, 0, pulse);
  delay(200);

  }
  
  
  delay(300);
     driver.setPWM(15, 0, gripMax);
    delay(2000);
    driver.setPWM(15, 0, gripMin);
  delay(5000);
   
  
  driver.setPWM(shoulderLServo, 0, shoulderLMin);
  delay(300);
  driver.setPWM(shoulderRServo, 0, shoulderRMax);
  delay(300);
  driver.setPWM(elbowServo, 0, elbowMax);
  delay(300);
  driver.setPWM(wristServo, 0, wristMax+50);
  delay(300);
  driver.setPWM(gripServo, 0, gripMin);
  delay(300);
    
  
}

void elbowForward(){
  int pulse = elbowMin;
  driver.setPWM(elbowServo, 0, pulse);
}


void wristForward(){
  int pulse = wristMin;
  driver.setPWM(wristServo, 0, pulse);
}

void gripping(){
    int pulse;
    driver.setPWM(15, 0, 125);
    delay(500);
    for(pulse = gripMin; pulse < gripMax; pulse++){
      driver.setPWM(15, 0, pulse);
    }
    delay(100);
  
  }

void backward(){
   digitalWrite(lin_1,HIGH) ;
   digitalWrite(lin_2,LOW) ;

   digitalWrite(rin_1,HIGH) ;
   digitalWrite(rin_2,LOW) ;
  
 }

 void forward(){
   digitalWrite(lin_2,HIGH) ;
   digitalWrite(lin_1,LOW) ;

   digitalWrite(rin_2,HIGH) ;
   digitalWrite(rin_1,LOW) ;
  
 }


 void stop(){
   digitalWrite(lin_1,LOW) ;
   digitalWrite(lin_2,LOW) ;
 
   digitalWrite(rin_1,LOW) ;
   digitalWrite(rin_2,LOW) ;

 }
 void left(){
   digitalWrite(lin_1,LOW) ;
   digitalWrite(lin_2,HIGH) ;
  
   digitalWrite(rin_1,HIGH) ;
   digitalWrite(rin_2,LOW) ;
 
 }
 void right(){
   digitalWrite(lin_1,HIGH) ;
   digitalWrite(lin_2,LOW) ;
 
   digitalWrite(rin_1,LOW) ;
   digitalWrite(rin_2,HIGH) ;

 }

 void resting_pos(){
  driver.setPWM(wristServo, 0, wristMax);
  delay(300);
  driver.setPWM(gripServo, 0, gripMax);
  delay(300);
  driver.setPWM(shoulderLServo, 0, shoulderLMin);
  delay(300);
  driver.setPWM(shoulderRServo, 0, shoulderRMax);
  delay(300);
  driver.setPWM(elbowServo, 0, elbowMax);
  delay(300);
 }
