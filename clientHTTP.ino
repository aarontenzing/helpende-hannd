#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


const char* ssid = "telenet-vc";
const char* password = "HE6d0tk93CZx";
const char* serverUrl = "http://192.168.0.229:5000/queue";
const int cid = 1;

const int buttonPin = 0; // GPIO0
const int ledPin = 2; // GPIO2

int ButtonState = 1;
int PrevButtonState = 1;

void setup() {

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // status van knop
  ButtonState = digitalRead(buttonPin);
  delay(10);
  if(ButtonState != PrevButtonState)
  {
      Serial.println("Button pressed!");
      sendData();
  }
  PrevButtonState = ButtonState;
}

void sendData() {

   // create a HTTP client object
    HTTPClient http;
    WiFiClient client;

    String postData = "cid=" + String(cid);
    http.begin(client,serverUrl); // maak verbinding met server
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    int responseCode = http.POST(postData);
    
    if (responseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(responseCode);
    }
    else 
    {
      Serial.print("Error code: ");
      Serial.println(responseCode);
    }
    http.end(); // beëindig de HTTP-verbinding
    delay(1000);
}

