# This is a sample Python script.

import redlab as rl
import math
import time
"""
print("------- einzelne Werte -------------------------")
print("16 Bit Value: " + str(rl.cbAIn(0, 0, 1)))
print("Voltage Value: " + str(rl.cbVIn(0, 0, 1)))
print("------- Messreihe -------------------------")
print("Messreihe: " + str(rl.cbAInScan(0, 0, 0, 300, 8000, 1)))
print("Messreihe: " + str(rl.cbVInScan(0, 0, 0, 300, 8000, 1)))
print("------- Ausgabe -------------------------")
lesen = input()
print("Voltage Value: " + str(rl.cbVOut(0, 0, 101, float(lesen))))



test = rl.cbInScanRate(0, 0,0, 101)
rl.cb
print(test)
"""

vals = rl.cbVInScan(0, 0, 0, 1000, 6000, 1)

with open("freq_2750.txt", "w") as f:
    f.write(str(vals))
