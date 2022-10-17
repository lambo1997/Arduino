import json
from datetime import datetime
import time

dt = datetime.now()
ts = datetime.timestamp(dt)
print("start timestamp : ", ts)

data = {}
with open('data.txt') as f:
    lines = f.readlines()
nn = len(lines)
for i in range(1, nn):
    if lines[i].split()[1] == "604":
        line =  lines[i]
        values = line.split()[3:]
        values = "".join(values)
        bit_pos = int(32 / 4)
        length = int(8 / 4)
        factor = 1
        _min = 0
        offset = 0
        _max = 100
        unit = "%"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            print("BPI_Battery = ", res, unit)
            dt_604 = datetime.now()
            ts_604 = datetime.timestamp(dt_604)
            data["BPI_Battery"] = res, unit
    if lines[i].split()[1] == "100":
        line =  lines[i]
        values = line.split()[3:]
        values = "".join(values)
        bit_pos = int(20 / 4)
        length = int(16 / 4)
        factor = 0.01
        offset = -327.68
        _min = -327.68
        _max = 327.68
        unit = "Nm"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            print("Torque Sensor = ", res, unit)
            dt_100 = datetime.now()
            ts_100 = datetime.timestamp(dt_100)
            data["Torque Sensor"] = res, unit
    if lines[i].split()[1] == "101":
        line =  lines[i]
        values = line.split()[3:]
        values = "".join(values)
        bit_pos = int(8 / 4)
        length = int(8 / 4)
        factor = 1
        offset = 0
        _min = 0
        _max = 255
        unit = ""
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            print("Joystick = ", res, unit)
            dt_101 = datetime.now()
            ts_101 = datetime.timestamp(dt_101)
            data["Joystick"] = res, unit
    if lines[i].split()[1] == "614":
        line =  lines[i]
        values = line.split()[3:]
        values = "".join(values)
        bit_pos = int(32 / 4)
        length = int(8 / 4)
        factor = 1
        offset = 0
        _min = 0
        _max = 100
        unit = "%"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            print("RPI_Battery = ", res, unit)
            dt_614 = datetime.now()
            ts_614 = datetime.timestamp(dt_614)
            data["RPI_Battery"] = res, unit
    if lines[i].split()[1] == "510":
        line =  lines[i]
        values = line.split()[3:]
        values = "".join(values)
        bit_pos = int(48 / 4)
        length = int(16 / 4)
        factor = 0.01
        offset = 0
        _min = 0
        _max = 655.35
        unit = "W"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            print("Motor Control = ", res, unit)
            dt_510 = datetime.now()
            ts_510 = datetime.timestamp(dt_510)
            data["Motor Control"] = res, unit

json_object = json.dumps(data, indent = 5)
 
# Writing to sample.json
with open("result.json", "w") as outfile:
    outfile.write(json_object)