#define WIFI_SSID "" 
#define WIFI_PASS ""
#define BLYNK_TEMPLATE_ID ""
#define BLYNK_TEMPLATE_NAME ""
#define BLYNK_AUTH_TOKEN ""
#include <GyverHTU21D.h> //установить
#include <BlynkSimpleEsp8266.h>
GyverHTU21D htu;
void updata(){
    if (htu.readTick()) {
      float temp=htu.getTemperature();
      Blynk.virtualWrite(V0, temp);
      float water=htu.getHumidity();
      Blynk.virtualWrite(V1, water);
      delay(5000);
    }
}

void setup(){
  Serial.begin(115200);
  Blynk.begin(BLYNK_AUTH_TOKEN,WIFI_SSID,WIFI_PASS);
  htu.begin();
}
void loop(){
  Blynk.run();
  updata();
}
