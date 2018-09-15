int receiveInt = 0;

int value = 0;
int direc = 0;
int wheel = 0;

void setup() {
  Serial.begin(9600);

  //output pin
  pinMode(4, OUTPUT); //left digital(direction)
  pinMode(5, OUTPUT); //left analog(speed)
  pinMode(6, OUTPUT);  //right digital
  pinMode(9, OUTPUT);  //right analog
}

void loop() {
  if(Serial.available() > 0){
    //read the incoming byte
    receiveInt = Serial.read();

    //print what you got
    Serial.println(receiveInt, BIN);

    //speed 0~5
    value = receiveInt & B11111100;
    //direction 6
    direc = receiveInt & B00000010;
    //left, right 7
    wheel = receiveInt & B00000001;
    
    if(wheel){
      //right wheel
      //set speed
      analogWrite(9, value);
      if(direc){
        //HIGH
        digitalWrite(6, HIGH);
      }
      else{
        //LOW
        digitalWrite(6, LOW);
      }
    }
    else{
      //left wheel
      //set speed
      analogWrite(5, value);
      if(direc){
        //HIGH
        digitalWrite(4, HIGH);
      }
      else{
        //LOW
        digitalWrite(4, LOW);
      }
    }
  }
}
