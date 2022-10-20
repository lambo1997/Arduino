import json
from datetime import datetime
import time

dt = datetime.now()


data = []
with open('0000146.txt') as f:
    lines = f.readlines()
nn = len(lines)
print(lines[1].split(";"))
for i in range(1, nn):
    if lines[i].split(";")[2] == "604":
        line =  lines[i]
        values = line.split(";")[3]
        bit_pos = int(32 / 4)
        length = int(8 / 4)
        factor = 1
        _min = 0
        offset = 0
        _max = 100
        unit = "%"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            dt_604 = datetime.now()
            print(dt_604, "BPI_Battery = ", res, unit)
            ddd = {}
            ddd["BPI_Battery"] = res, unit
            data.append(ddd)
    if lines[i].split(";")[2] == "100":
        line =  lines[i]
        values = line.split(";")[3]
        bit_pos = int(20 / 4)
        length = int(16 / 4)
        factor = 0.01
        offset = -327.68
        _min = -327.68
        _max = 327.68
        unit = "Nm"
        res = int(values[bit_pos:bit_pos + length], 16) * factor + offset
        if res >= _min and res <= _max:
            dt_100 = datetime.now()
            print(dt_100, "Torque Sensor = ", res, unit)
            ddd = {}
            ddd["Torque Sensor"] = res, unit
            data.append(ddd)
    if lines[i].split(";")[2] == "101":
        line =  lines[i]
        values = line.split(";")[3]
        bit_pos = int(8 / 4)
        length = int(8 / 4)
        factor = 1
        offset = 0
        _min = 0
        _max = 255
        unit = ""
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            dt_101 = datetime.now()
            print(dt_101, "Joystick = ", res, unit)
            ddd = {}
            ddd["Joystick"] = res, unit
            data.append(ddd)
    if lines[i].split(";")[2] == "614":
        line =  lines[i]
        values = line.split(";")[3]
        bit_pos = int(32 / 4)
        length = int(8 / 4)
        factor = 1
        offset = 0
        _min = 0
        _max = 100
        unit = "%"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            dt_614 = datetime.now()
            print(dt_614, "RPI_Battery = ", res, unit)
            ddd = {}
            ddd["RPI_Battery"] = res, unit
            data.append(ddd)
    if lines[i].split(";")[2] == "510":
        line =  lines[i]
        values = line.split(";")[3]
        bit_pos = int(48 / 4)
        length = int(16 / 4)
        factor = 0.01
        offset = 0
        _min = 0
        _max = 655.35
        unit = "W"
        res = int(values[bit_pos:bit_pos + length], 16) * factor
        if res >= _min and res <= _max:
            dt_510 = datetime.now()
            print(dt_510, "Motor Control = ", res, unit)
            ddd = {}
            ddd["Motor Control"] = res, unit
            data.append(ddd)

json_object = json.dumps(data, indent=5)
print("data = ", data)
# Writing to sample.json
with open("result_txt.json", "w") as outfile:
    outfile.write(json_object)