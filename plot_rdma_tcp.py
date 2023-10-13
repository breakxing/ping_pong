import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]
low  = [2] * int(len(Message_Size))

RDMA_THREAD_1 = np.round(np.array([354,598,928,1298,1769,2342,2680,2960,3064,3243,3293,3322,3333,3343,3351]) * 8 / 1000).astype(int)
RDMA_THREAD_2 = np.round(np.array([300,564,923,1480,2192,2992,3791,4420,4152,5011,5327,5462,5470,5480,5483]) * 8 / 1000).astype(int)
RDMA_THREAD_4 = np.round(np.array([344,627,1075,1757,2689,3859,4851,5466,5558,5514,5508,5504,5508,5507,5507]) * 8 / 1000).astype(int)
RDMA_THREAD_8 = np.round(np.array([590,1081,1901,3091,4383,5434,5591,5559,5574,5511,5502,5507,5508,5449,5504]) * 8 / 1000).astype(int)
top  = [50] * len(RDMA_THREAD_1)





fontSize = 16

h = 4
w = 7.5
scale = 1.3
plt.rcParams['font.size'] = fontSize
plt.rcParams["figure.figsize"] = (w * scale, h *scale)
# plt.yscale("log")
plt.ylim([2.4,48])

plt.plot(Message_Size, RDMA_THREAD_8, label = "8-THREAD", linewidth = 2, marker = '^', color='#F2CB05')
for a, b in zip(Message_Size, RDMA_THREAD_8):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_4, label = "4-THREAD", linewidth = 2, marker = 's', color='#F29F05')
for a, b in zip(Message_Size, RDMA_THREAD_4):
    if a == 18:
        plt.text(a, b - 3, b, ha="center", va="bottom", fontsize = fontSize)
    else:    
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_2, label = "2-THREAD", linewidth = 2, marker = 'v', color='#F28705')
for a, b in zip(Message_Size, RDMA_THREAD_2):
    if a == 20:
        plt.text(a, b - 3, b, ha="center", va="bottom", fontsize = fontSize)
    else:
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_1, label = "1-THREAD", linewidth = 2, marker = 'o', color='#F23030')
for a, b in zip(Message_Size, RDMA_THREAD_1):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)


plt.plot(Message_Size, top, linewidth = 0)
plt.plot(Message_Size, low, linewidth = 0)

plt.xlabel("Log Scale Message Size (Byte)", fontsize=fontSize,)
plt.ylabel("Bandwidth (Gbps)", fontsize=fontSize,)

plt.xticks(fontsize=fontSize,)
plt.yticks(fontsize=fontSize,)


plt.legend(fontsize = 15.3, loc="lower right")
plt.title("RDMA")
plt.show()
# plt.savefig("line_cpu.pdf", dpi = 200)#, bbox_inches="tight")
