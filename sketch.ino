#define R 2
#define Y 4
#define G 6
#define B 8
#define W 10

#define COUNT 5

const byte LEDS[COUNT] = {R, Y, G, B, W};
byte i, led, action;
String command;

void setup() {
  Serial.begin(9600);
  for (i = 0; i < COUNT; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  while (!Serial.available()) {}
  command = String(Serial.parseInt());
  led = command.charAt(0) - '0';
  action = command.charAt(1) - '0';

  if (isValidLed(led) && isValidAction(action)) {
    digitalWrite(LEDS[led - 1], action);
  }
}

boolean isValidLed(byte led) {
  return led >= 1 && led <= COUNT;
}

boolean isValidAction(byte action) {
  return action == 0 || action == 1;
}
