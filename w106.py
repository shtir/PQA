#! /usr/bin/env python
# sudo pip install pyModbusTCP
from pyModbusTCP.client import ModbusClient
import datetime
from influxdb import InfluxDBClient
from env import *


time = datetime.datetime.utcnow()


class W106:

    def __init__(self, address, port, counter=False):
        c = ModbusClient()
        c.host(address)
        c.port(port)
        c.unit_id(1)
        c.open()
        voltAmper = c.read_holding_registers(0, 50)
        if voltAmper:
            self.v1 = (voltAmper[0] << 16 | voltAmper[1])/10
            self.v2 = (voltAmper[2] << 16 | voltAmper[3])/10
            self.v3 = (voltAmper[4] << 16 | voltAmper[5])/10
            self.vavg = (voltAmper[6] << 16 | voltAmper[7])/10
            self.vun = (voltAmper[8] << 16 | voltAmper[9])/10

            self.v12 = (voltAmper[10] << 16 | voltAmper[11])/10
            self.v23 = (voltAmper[12] << 16 | voltAmper[13])/10
            self.v31 = (voltAmper[14] << 16 | voltAmper[15])/10

            self.i1 = (voltAmper[16] << 16 | voltAmper[17])/10
            self.i2 = (voltAmper[18] << 16 | voltAmper[19])/10
            self.i3 = (voltAmper[20] << 16 | voltAmper[21])/10
            self.iavg = (voltAmper[22] << 16 | voltAmper[23])/10
            self.inut = (voltAmper[24] << 16 | voltAmper[25])/10

            self.ptot = (voltAmper[44] << 16 | voltAmper[45])/10
            self.qtot = (voltAmper[46] << 16 | voltAmper[47])/10
            self.stot = (voltAmper[48] << 16 | voltAmper[49])/10

        else:
            print("Read Vol And Amper ERROR")

        if (counter):
            Counter = c.read_holding_registers(70, 36)
            c.close()
            if Counter:
                self.peakA1 = (Counter[0] << 32 |
                               Counter[1] << 16 | Counter[2])
                self.peakP1 = (Counter[3] << 32 |
                               Counter[4] << 16 | Counter[5])
                self.peakA2 = (Counter[6] << 32 |
                               Counter[7] << 16 | Counter[8])
                self.peakP2 = (Counter[9] << 32 |
                               Counter[10] << 16 | Counter[11])

                self.normalA1 = (Counter[12] << 32 |
                                 Counter[13] << 16 | Counter[14])
                self.normalP1 = (Counter[15] << 32 |
                                 Counter[16] << 16 | Counter[17])
                self.normalA2 = (Counter[18] << 32 |
                                 Counter[19] << 16 | Counter[20])
                self.normalP2 = (Counter[21] << 32 |
                                 Counter[22] << 16 | Counter[23])

                self.lowA1 = (Counter[24] << 32 |
                              Counter[25] << 16 | Counter[26])
                self.lowP1 = (Counter[27] << 32 |
                              Counter[28] << 16 | Counter[29])
                self.lowA2 = (Counter[30] << 32 |
                              Counter[31] << 16 | Counter[32])
                self.lowP2 = (Counter[33] << 32 |
                              Counter[34] << 16 | Counter[35])

                self.CounterA1 = self.peakA1 + self.normalA1 + self.lowA1
                self.CounterP1 = self.peakP1 + self.normalP1 + self.lowP1
                self.CounterA2 = self.peakA2 + self.normalA2 + self.lowA2
                self.CounterP2 = self.peakP2 + self.normalP2 + self.lowP2

            else:
                print("Read Counter ERROR")


w106_1 = W106("192.168.88.12", 502, True)
measurement_name = "W106-1"
# format the data as a single measurement for influx
body = [
    {
        "measurement": measurement_name,
        "time": time,
        "fields": {
            "V1": w106_1.v1,
            "V2": w106_1.v2,
            "V3": w106_1.v3,
            "Vavg": w106_1.vavg,
            "I1": w106_1.i1,
            "I2": w106_1.i2,
            "I3": w106_1.i3,
            "Iavg": w106_1.iavg,
            "Ptot": w106_1.ptot,
            "Qtot": w106_1.qtot,
            "Stot": w106_1.stot,
        }
    }
]

# connect to influx
ifclient = InfluxDBClient(ifhost, ifport, ifuser, ifpass, ifdb)

# write the measurement
ifclient.write_points(body)


w106_1 = W106("192.168.88.12", 502, True)
measurement_name = "W106-1-counter"
# format the data as a single measurement for influx
body = [
    {
        "measurement": measurement_name,
        "time": time,
        "fields": {
            "A+": w106_1.CounterA1,
            "P+": w106_1.CounterP1,
            "A-": w106_1.CounterA2,
            "P-": w106_1.CounterP2,
        }
    }
]

ifclient = InfluxDBClient(ifhost, ifport, ifuser, ifpass, ifdb)
ifclient.write_points(body)
