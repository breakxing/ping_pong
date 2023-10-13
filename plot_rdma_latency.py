import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]

SHOW_TEXT_1 = [2,3,4,6,9,13,24,44,83,162,318,631,1259,2512,5017]
SHOW_TEXT_2 = [10,8,10,13,26,32,46,76,145,231,454,814,1604,3069,6135]
SHOW_TEXT_4 = [14,13,19,23,28,36,56,97,188,380,761,1524,3045,6093,12186]
SHOW_TEXT_8 = [13,13,16,19,28,47,93,188,377,760,1524,3048,6094,12306,24384]
print("Message_Size\t1 Thread\t2 Thread\t4 Thread\t8 Thread")
for i in range(len(SHOW_TEXT_1)):
    print(f"{i + 10}\t\t{SHOW_TEXT_1[i]}\t\t{SHOW_TEXT_2[i]}\t\t{SHOW_TEXT_4[i]}\t\t{SHOW_TEXT_8[i]}")
RDMA_THREAD_1 = np.round(np.log2([2,3,4,6,9,13,24,44,83,162,318,631,1259,2512,5017]).astype(int))
RDMA_THREAD_2 = np.round(np.log2([10,8,10,13,26,32,46,76,145,231,454,814,1604,3069,6135]).astype(int))
RDMA_THREAD_4 = np.round(np.log2([14,13,19,23,28,36,56,97,188,380,761,1524,3045,6093,12186]).astype(int))
RDMA_THREAD_8 = np.round(np.log2([13,13,16,19,28,47,93,188,377,760,1524,3048,6094,12306,24384]).astype(int))
m1 = min(RDMA_THREAD_1)
m2 = min(RDMA_THREAD_2)
m3 = min(RDMA_THREAD_4)
m4 = min(RDMA_THREAD_8)
M1 = max(RDMA_THREAD_1)
M2 = max(RDMA_THREAD_2)
M3 = max(RDMA_THREAD_4)
M4 = max(RDMA_THREAD_8)
low  = [min(m1,m2,m3,m4)] * int(len(Message_Size))
top  = [min(M1,M2,M3,M4)] * len(RDMA_THREAD_1)





fontSize = 16

h = 4
w = 7.5
scale = 1.3
plt.rcParams['font.size'] = fontSize
plt.rcParams["figure.figsize"] = (w * scale, h *scale)
# plt.yscale("log")

plt.plot(Message_Size, RDMA_THREAD_8, label = "8-THREAD", linewidth = 2, marker = '^', color='#F2CB05')
for a, b in zip(Message_Size, RDMA_THREAD_8):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_4, label = "4-THREAD", linewidth = 2, marker = 's', color='#F29F05')
for a, b in zip(Message_Size, RDMA_THREAD_4):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_2, label = "2-THREAD", linewidth = 2, marker = 'v', color='#F28705')
for a, b in zip(Message_Size, RDMA_THREAD_2):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_1, label = "1-THREAD", linewidth = 2, marker = 'o', color='#F23030')
for a, b in zip(Message_Size, RDMA_THREAD_1):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

print(RDMA_THREAD_8)
print(RDMA_THREAD_4)
print(RDMA_THREAD_2)
print(RDMA_THREAD_1)
plt.plot(Message_Size, top, linewidth = 0)
plt.plot(Message_Size, low, linewidth = 0)

plt.xlabel("Log Scale Message Size (Byte)", fontsize=fontSize,)
plt.ylabel("Log Scale One Way Latency (us)", fontsize=fontSize,)

plt.xticks(fontsize=fontSize,)
plt.yticks(fontsize=fontSize,)


plt.legend(fontsize = 15.3, loc="best")
plt.title("RDMA One Way Latency")
plt.show()
# plt.savefig("line_cpu.pdf", dpi = 200)#, bbox_inches="tight")
