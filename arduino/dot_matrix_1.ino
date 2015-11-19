
#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>

byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xE1 };

IPAddress ip(172, 168, 1, 41 );
//const char* mqtt_server = "test.mosquitto.org";
IPAddress local_server(192, 168, 10, 1 );

char mTopicIn[]="topic-15-1119A/device-1/matrix-1";
const int mRelay_pin=7;
int mMaxMatrix=20;
long mRetry=1;

//
void send_matrix(String src){
  int iStr =src.length();
  String buff_1="";
  String buff_2="";
  String sHd="011";
  String sCRLF="\r\n";
  String src20=src;
  if(iStr > mMaxMatrix){
    src20=src.substring(0,21);
  }
  if(iStr < 1){ return; }
  if(iStr > 10){
    buff_1=src20.substring(0,10);
    Serial.print(sHd+buff_1);
    delay(100);
    buff_2=src20.substring(10);
    Serial.print(buff_2+sCRLF);
  }else{
    buff_1=src20;
    Serial.print(sHd+buff_1+sCRLF);
  }
}


//
void callback(char* topic, byte* payload, unsigned int length) {
  //Serial.print("Message arrived [");
 // Serial.print(topic);
  //Serial.print("] ");
  String sTopi=String( mTopicIn );
  String sTopi_in =String( topic );
  String sLine="";
  if( sTopi.equals( sTopi_in ) ){
    for (int i=0;i<length;i++) {
      String sPay= String( (char)payload[i] );
      sLine +=sPay;
    }
    send_matrix(sLine);
   }
  Serial.println();
}

EthernetClient ethClient;
PubSubClient client(ethClient);

void reconnect(long retry) {
  while (!client.connected()) {
    if(retry <2){
      Serial.print("Attempting MQTT connection...");
    }
    if (client.connect("arduinoClient")) {
      if(retry <2){
        Serial.println("connected");
      }
      client.subscribe( mTopicIn );
    } else {
      if(retry <2){
          Serial.print("failed, rc=");
          Serial.print(client.state());
          Serial.println(" try again in 5 seconds");
      }
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

//
void setup()
{
  Serial.begin( 9600);
  pinMode(mRelay_pin, OUTPUT);
  Serial.println("# Start-mqtt_basic");
  
  client.setServer(local_server, 1883);
  client.setCallback(callback);

  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    Ethernet.begin(mac, ip);
  }  
  // Allow the hardware to sort itself out
  delay(1500);
}

void loop()
{
  if (!client.connected()) {
    reconnect(mRetry);
    mRetry++;
  }
  client.loop();
  
}



