from patchbay import create_remote_patch, Trigger, Slider

def trigger_func():
        value = float(frequency.value) * 10
        print(value)

patch = create_remote_patch(use_udp=False)

patch.bind(channel=1, event_handler=Trigger(trigger_func))
frequency = patch.bind(channel = 2, event_handler=Slider())

while True:
        patch.route_events()

