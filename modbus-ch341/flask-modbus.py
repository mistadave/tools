from datetime import datetime
import minimalmodbus
from flask import Flask, jsonify
from find_usb import find_ch341
import logging

# Temp
# python3 read_modbus_rtu.py 1 1 -f 4 -d /dev/ttyUSB0 -e 0

# Humidity
# python3 read_modbus_rtu.py 1 2 -f 4 -d /dev/ttyUSB0 -e 0

address = 1
stopbits = 1
baud = 9600
timeout = 1
echo = False
parity = 'N'
functioncode = 4
device = 'ttyUSB0'


def setup_instrument():
    uart = '/dev/{}'.format(device)
    logging.info('init device on usb {}'.format(uart))
    instrument = minimalmodbus.Instrument(uart, address)
    instrument.serial.parity = parity
    instrument.serial.stopbits = stopbits
    instrument.serial.baudrate = baud
    instrument.serial.timeout = timeout
    instrument.handle_local_echo = echo
    return instrument


def read_temp(i: minimalmodbus.Instrument) -> float:
    register = 1
    value = 0
    try:
        value = i.read_register(register, 0, functioncode, False)
    except Exception as e:
        print('failed to read')
    return value / 10


def read_humiditiy(i: minimalmodbus.Instrument) -> float:
    register = 2
    value = 0
    try:
        value = i.read_register(register, 0, functioncode, False)
    except Exception as e:
        print('failed to read')
    return value / 10


app = Flask(__name__)
instr = setup_instrument()


@app.route('/temperature', methods=['GET'])
def get_temp():
    return str(read_temp(instr))


@app.route('/humidity', methods=['GET'])
def get_hum():
    return str(read_humiditiy(instr))


@app.route('/all', methods=['GET'])
def get_sensors():
    hum = read_humiditiy(instr)
    temp = read_temp(instr)
    return jsonify({"humidity": hum, "temperature": temp, "ts": int(datetime.now().timestamp()*1000)})


if __name__ == "__main__":
    new_device = find_ch341()
    if new_device:
        device = new_device
    app.run('0.0.0.0', port=5050, debug=False)

# if __name__ == "__main__":

#     temp = read_temp(instr)
#     humidity = read_humiditiy(instr)
#     print("{} {}".format(temp, 'C'))
#     print("{} {}".format(humidity, '%RH'))
