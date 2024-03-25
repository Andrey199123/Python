import time
import os

start = time.time()
for i in range(1000):
    file = open("/Users/yuryvasiliev/Downloads/hello" + str(i) + ".png", "w+")
for i in range(1000):
    os.remove("/Users/yuryvasiliev/Downloads/hello" + str(i) + ".png")
print("Completed in", round(1000 * (time.time() - start)), "milliseconds.")
# 1675, 191, 191, 181 for txt
# 612, 254, 180, 374 for jpg
# 468, 188, 284, 366 for png
