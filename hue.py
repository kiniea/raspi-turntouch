import json
from qhue import Bridge, create_new_username
import requests

class HueController:

    def __init__(self):
        try:
            with open('.hueusername') as f:
                bridge_data = json.loads(f.read())
        except:
            print("Bridge not authorised, need to press the button!")
            bridge_data = json.loads(
                requests.get('https://www.meethue.com/api/nupnp').text)[0]
            bridge_data['username'] = create_new_username(
                    bridge_data['internalipaddress'])
            with open('.hueusername', 'w') as f:
                f.write(json.dumps(bridge_data))
        self.bridge = Bridge(bridge_data['internalipaddress'], bridge_data['username'])
        print("Successfully connected to Hue Bridge {}".format(bridge_data['internalipaddress']))

    def print_all_lights(self):
        rooms = self.bridge.groups()
        for id, light in self.bridge.lights().items():
            room = [r for r in rooms.values() if id in r['lights']]
            print("[{}]: {} ({}){}".format(
                id, light['name'], light['type'], 
                " in {}".format(room[0]['name']) if room else ""))

    def set_light(self, id, *args, **kwargs):
        self.bridge.lights[id].state(**kwargs)
            

if __name__ == '__main__':
    c = HueController()
    c.print_all_lights()