import asyncio
import paho.mqtt.client as mqtt
import json

async def vacuum_cleaner():
    client = mqtt.Client('1')
    client.username_pw_set(username='i6bxQRCSMPcHW0bY0fQW', password="")
    broker_address="51.250.101.37"
    client.connect(host=broker_address, port=1883, keepalive=60)
    params_telemery = {
        'main-light': 'ON',
        'battery_power': 100
    }
    await asyncio.sleep(3)
    client.publish('v1/devices/me/telemetry', payload=json.dumps(params_telemery))
    client.disconnect()
    print(json.dumps(params_telemery))

async def bulb():
    client = mqtt.Client('2')
    client.username_pw_set(username='DKSaeTeizAgTMZM2Y7YI', password="")
    broker_address="51.250.101.37"
    client.connect(host=broker_address, port=1883, keepalive=60)
    params_telemery = {
        'main-light': 'ON',
        'power': 14
    }
    await asyncio.sleep(3)
    client.publish('v1/devices/me/telemetry', payload=json.dumps(params_telemery))
    client.disconnect()
    print(json.dumps(params_telemery))

async def teapot():
    client = mqtt.Client('3')
    client.username_pw_set(username='X7Ysmzk7jupWZkZ256kf', password="")
    broker_address="51.250.101.37"
    client.connect(host=broker_address, port=1883, keepalive=60)
    params_telemery = {
        'main-light': 'ON',
        'temperature-water': 20
    }
    for i in range(0, 10):
        await asyncio.sleep(3)
        client.publish('v1/devices/me/telemetry', payload=json.dumps(params_telemery))
        params_telemery['temperature-water'] += 6
    client.disconnect()
    print(json.dumps(params_telemery))

async def main():
    await asyncio.wait([
        loop.create_task(vacuum_cleaner()),
        loop.create_task(bulb()),
        loop.create_task(teapot())])

if __name__ =="__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
