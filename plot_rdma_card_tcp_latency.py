import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]

SHOW_TEXT_1 = [11,17,18,28,30,61,87,129,197,332,537,858,1501,2834,5736]
SHOW_TEXT_2 = [41,52,54,80,79,114,132,162,365,516,848,1524,2873,5811,11414]
SHOW_TEXT_4 = [493,472,287,392,296,361,319,407,862,985,1547,2636,5295,10865,21494]
SHOW_TEXT_8 = [171,169,175,219,229,257,291,426,924,1439,2555,5258,10829,21831,43797]
print("Message_Size\t1 Thread\t2 Thread\t4 Thread\t8 Thread")
for i in range(len(SHOW_TEXT_1)):
    print(f"{i + 10}\t\t{SHOW_TEXT_1[i]}\t\t{SHOW_TEXT_2[i]}\t\t{SHOW_TEXT_4[i]}\t\t{SHOW_TEXT_8[i]}")


RDMA_THREAD_1 = np.round(np.log2([11,17,18,28,30,61,87,129,197,332,537,858,1501,2834,5736]).astype(int))
RDMA_THREAD_2 = np.round(np.log2([41,52,54,80,79,114,132,162,365,516,848,1524,2873,5811,11414]).astype(int))
RDMA_THREAD_4 = np.round(np.log2([493,472,287,392,296,361,319,407,862,985,1547,2636,5295,10865,21494]).astype(int))
RDMA_THREAD_8 = np.round(np.log2([171,169,175,219,229,257,291,426,924,1439,2555,5258,10829,21831,43797]).astype(int))
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
plt.title("RDMA Card TCP One Way Latency")
plt.show()
# plt.savefig("line_cpu.pdf", dpi = 200)#, bbox_inches="tight")
