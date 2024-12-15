import numpy as np
import matplotlib.pyplot as plt

inputCSV_path = "./MessungenVersuch3/Versuch_1_Ton-0001/Versuch_1_Ton-0001_06.csv"

with open(inputCSV_path, "r") as f:
    lines = f.read().splitlines()[5005:7000]

temp = []
for x in lines:
    temp.append([float(y.replace(",", ".")) for y in x.split(";")])
lines = temp.copy()

ms = []
mv = []
for x in lines:
    ms.append(x[0])
    mv.append(x[1])

plt.plot(ms, mv)
plt.xlabel("ms")
plt.ylabel("mv")
plt.show()

a = [1, 2, 4]

b = max(a, key=lambda)