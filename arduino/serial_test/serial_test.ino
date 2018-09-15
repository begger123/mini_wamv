void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("start");
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int n = Serial.read();
    Serial.println(n);
  }
}
