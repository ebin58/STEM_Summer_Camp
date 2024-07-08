
#include <SPI.h>
#include <WiFiNINA.h>
#include <WiFiUdp.h>

// Code created by Natalie Leveque on June 3rd, 2024

int status = WL_IDLE_STATUS; 

//my_ip = "192.168.0.178"

char ssid[] = "OAL_wireless";        // your network SSID (name)
char pass[] = "83792151";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen for UDP packets


const int NTP_PACKET_SIZE = 48; // NTP time stamp is in the first 48 bytes of the message

byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets

// A UDP instance to let us send and receive packets over UDP

WiFiUDP Udp;

void setup() {

  // Open serial communications and wait for port to open:

  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the WiFi module:

  if (WiFi.status() == WL_NO_MODULE) {

    Serial.println("Communication with WiFi module failed!");

    // don't continue

    while (true);

  }

  String fv = WiFi.firmwareVersion();

  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {

    Serial.println("Please upgrade the firmware");

  }

  // attempt to connect to Wifi network:

  while (status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  Serial.println("Connected to wifi");

  printWifiStatus();

  Serial.println("\nStarting connection to server...");

  Udp.begin(localPort);
}

void loop() {


  

  if (Udp.parsePacket()) {

    Serial.println("\npacket received");

    // We've received a packet, read the data from it

    int n = Udp.read(packetBuffer, NTP_PACKET_SIZE); // read the packet into the buffer
    String mess = "";
    packetBuffer[n] = 0;
    
    for(int i = 0; i < n; i++){
      Serial.print(char(packetBuffer[i]));
      mess += char(packetBuffer[i]);
    }

    // Serial.println("\nPrinting mess var");
    // Serial.println(mess);
    // Serial.println("");

    mess.toUpperCase();
    // If the message is on, then the builtin LED turns on 
    if(mess.compareTo("ON") == 0){
      digitalWrite(LED_BUILTIN, HIGH);
    }

    // If the message is off, then the builtin LED turns off
    if(mess.compareTo("OFF") == 0){
      digitalWrite(LED_BUILTIN, LOW);
    }
    


  // wait ten seconds before asking for the time again
  delay(1000);
  

}
}

void printWifiStatus() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print your board's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.print(rssi);

  Serial.println(" dBm");
}