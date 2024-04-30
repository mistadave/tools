import re
import subprocess

def find_ch341():
    cmd = 'dmesg | grep "ch341-uart"'
    p_ATTACH = re.compile("(ch341-uart.*attached)", re.I)
    usb = []
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE )
        output, _o = p.communicate()
        if p.returncode == 1:
            print("nothing found")
        elif p.returncode == 0:
            for msg in output.decode("utf-8").split("\n"):
                if msg:
                    found = p_ATTACH.search(msg)
                    if (found):
                        res = re.search('(tty[A-Z])\w+', msg)
                        if res:
                            usb.append(res.group(0))
        if len(usb)>0:
            return usb[len(usb)- 1]     
    except Exception as err:
        print("whooops failed to read dmesg with grep")
        print(err)
    return None

def run_find():
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb")
    devices = []
    df = df.decode('utf-8')
    for i in df.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)

    print(devices)
