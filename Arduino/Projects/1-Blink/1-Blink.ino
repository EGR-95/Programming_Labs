const int x = 13;
const int t = 5000;

void setup() {
  pinMode(x, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(x, HIGH); 
  Serial.println("LED ON");
  delay(t);

  digitalWrite(x, LOW);
  Serial.println("LED OFF");
  delay(t);
}

