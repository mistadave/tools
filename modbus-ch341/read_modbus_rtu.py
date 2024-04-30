#!/usr/bin/env python3
import sys
import minimalmodbus
import argparse
from inspect import getmembers, isfunction
import traceback

parser = argparse.ArgumentParser(description='modbus read test')
parser.add_argument('address', type=int, help='modbus slace address (0-254)')
parser.add_argument('register', type=int, help='modbus register')
parser.add_argument('-b', '--baud', type=int, default=9600,
                    help='serial baudrate (default: 9600)')
parser.add_argument('-p', '--parity', type=str, default='N', choices={
                    "O", "E", "N"}, help='checksum parity (N for None, E for Even, O for Odd. default: None')
parser.add_argument('-s', '--stopbits', type=int, default=1,
                    help='number of stopbits. default is 1')
parser.add_argument('-t', '--timeout', type=int, default=1,
                    help='timeout in seconds. default is 1')
parser.add_argument('-f', '--functioncode', type=int, default=3, choices={
                    1, 3, 4}, help='modbus function code. 4 for input registers (register 30000-39999, 3 for holding registers(register 40000-49999), 1 for coils. default is 3')
parser.add_argument('-d', '--device', type=str, default='/dev/ttyO2',
                    help='Choose which attached device is used (/dev/ttyO2)')
parser.add_argument('-e', '--echo', type=int, default=1, choices={1, 0},
                    help='Set local echo true(1) or false(0)')
args = parser.parse_args()

# print(args.address)
address = args.address
register = args.register
baud = args.baud
parity = args.parity
stopbits = args.stopbits
timeout = args.timeout
functioncode = args.functioncode
device = args.device
if args.echo == 1:
    echo = True
else:
    echo = False

print("Try to read register {}, functioncode {} from modbus device at address {} using {}, baud rate {}, parity {} and {} stopbit(s)".format(
    register, functioncode, address, device, baud, parity, stopbits))

instrument = minimalmodbus.Instrument(device, address)
instrument.serial.parity = parity
instrument.serial.stopbits = stopbits
instrument.serial.baudrate = baud
instrument.serial.timeout = timeout
instrument.handle_local_echo = echo
print(instrument)


if functioncode == 1:
    try:
        value = instrument.read_bit(register, 1)
    except minimalmodbus.NoResponseError as e:
        print(e)
        sys.exit(0)
    except Exception:
        value = traceback.format_exc()
    print("result : {}".format(value))
else:

    # iterate over different byteorders
    try:
        value = instrument.read_registers(register, 1)
    except minimalmodbus.NoResponseError as e:
        print(e)
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        value = traceback.format_exc()
    print("result as register: {}".format(value))

    try:
        value = instrument.read_register(
            register, 0, functioncode, False)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        value = traceback.format_exc()
    print("result as u16: {}".format(value))

    try:
        value = instrument.read_register(
            register, 0, functioncode, True)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        value = traceback.format_exc()
    print("result as i16: {}".format(value))

    for member in sorted(getmembers(minimalmodbus)):
        byteorder_name = member[0]
        byteorder = member[1]
        if (member[0].startswith("BYTEORDER_")):
            print("=================================")
            print("Try to read using Byteorder {}".format(member[0]))
            print("=================================")

            try:
                value = instrument.read_long(
                    register, functioncode, False, byteorder)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception:
                value = traceback.format_exc()
            print("result as u32: {}".format(value))

            try:
                value = instrument.read_long(
                    register, functioncode, True, byteorder)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception:
                value = traceback.format_exc()
            print("result as i32: {}".format(value))

            try:
                value = instrument.read_float(
                    register, functioncode, 2, byteorder)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception:
                value = traceback.format_exc()
            print("result as f32: {}".format(value))

            try:
                value = instrument.read_float(
                    register, functioncode, 4, byteorder)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception:
                value = traceback.format_exc()
            print("result as f64: {}".format(value))

