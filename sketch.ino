#include <string.h>

#define R 3
#define G 5
#define B 6

#define COUNT 3

const byte RGB[COUNT] = {R, G, B};
const char DELIMITER = ',';
byte i;

void setup() {
  Serial.begin(9600);
  for (i = 0; i < COUNT; i++) {
    pinMode(RGB[i], OUTPUT);
    analogWrite(RGB[i], 255);
  }
}

void loop() {
  if (Serial.available()) {
    String color = Serial.readStringUntil('\n');
    color.trim();

    int values[COUNT];
    int total = parseColor(color, values);

    for (i = 0; i < total; i++) {
      analogWrite(RGB[i], 255 - values[i]);
    }
  }
}

int parseColor(const String& input, int* output) {
  char str[input.length() + 1];
  strcpy(str, input.c_str());

  char* token = strtok(str, &DELIMITER);
  int count = 0;

  while (token != NULL && count < COUNT) {
    output[count] = atoi(token);
    count++;

    token = strtok(NULL, &DELIMITER);
  }

  return count;
}
