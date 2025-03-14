# light_simulation.py
import paho.mqtt.client as mqtt

# MQTT Configuration
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "/student_group/light_control"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("🌀 Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"⚠️ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        if payload == "ON":
            print("\n💡 CYBERLIGHT ACTIVATED [STATUS: LUMINESCENT]")
        elif payload == "OFF":
            print("\n🌑 DARKNESS PROTOCOL ENGAGED [STATUS: INACTIVE]")
    except Exception as e:
        print(f"🚨 Error processing message: {e}")

# Initialize Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect & Run
print("🚀 Starting CyberLight Simulation...")
try:
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🔴 Simulation terminated")
except Exception as e:
    print(f"🚨 Critical error: {e}")