import sys
import time
import board
import adafruit_dht


# Parse command line parameters.
sensor_args = {"11": adafruit_dht.DHT11, "22": adafruit_dht.DHT22}

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    pin = sys.argv[2]
    device = sensor_args[sys.argv[1]](getattr(board, 'D{}'.format(pin)))
else:
    sys.exit(1)

count = 0
max_count = 10
for count in range(max_count):
    try:
        temperature = device.temperature
        humidity = device.humidity
        if temperature is None or humidity is None:
            time.sleep(0.5)
            continue
    except RuntimeError:
        time.sleep(0.5)
    else:
        break

if humidity is not None and temperature is not None:
    print("{0:0.1f} | {1:0.1f}".format(temperature, humidity))
else:
    print("-1 | -1")

sys.exit(1)
