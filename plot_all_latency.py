import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]

SHOW_TEXT_1 = [269,277,380,587,799,1193,2248,4492,18390,36359,72354,144090,287758,575027,1149513]
SHOW_TEXT_2 = [171,169,175,219,229,257,291,426,924,1439,2555,5258,10829,21831,43797]
SHOW_TEXT_3 = [13,13,16,19,28,47,93,188,377,760,1524,3048,6094,12306,24384]
print("Message_Size\tNORMAL_CARD_TCP_THREAD_8\tRDMA_CARD_TCP_THREAD_8\tRDMA_CARD_RDMA_THREAD_8")
for i in range(len(SHOW_TEXT_1)):
    print(f"{i + 10}\t\t{SHOW_TEXT_1[i]}\t\t\t\t{SHOW_TEXT_2[i]}\t\t\t{SHOW_TEXT_3[i]}")
NORMAL_CARD_TCP_THREAD_8    = np.round(np.log2([269,277,380,587,799,1193,2248,4492,18390,36359,72354,144090,287758,575027,1149513]).astype(int))
RDMA_CARD_TCP_THREAD_8      = np.round(np.log2([171,169,175,219,229,257,291,426,924,1439,2555,5258,10829,21831,43797]).astype(int))
RDMA_CARD_RDMA_THREAD_8     = np.round(np.log2([13,13,16,19,28,47,93,188,377,760,1524,3048,6094,12306,24384]).astype(int))
m1 = min(NORMAL_CARD_TCP_THREAD_8)
m2 = min(RDMA_CARD_TCP_THREAD_8)
m3 = min(RDMA_CARD_RDMA_THREAD_8)
M1 = max(NORMAL_CARD_TCP_THREAD_8)
M2 = max(RDMA_CARD_TCP_THREAD_8)
M3 = max(RDMA_CARD_RDMA_THREAD_8)
low  = [min(m1,m2,m3)] * int(len(Message_Size))
top  = [min(M1,M2,M3)] * len(RDMA_CARD_RDMA_THREAD_8)





fontSize = 16

h = 4
w = 7.5
scale = 1.3
plt.rcParams['font.size'] = fontSize
plt.rcParams["figure.figsize"] = (w * scale, h *scale)
# plt.yscale("log")

plt.plot(Message_Size, RDMA_CARD_RDMA_THREAD_8, label = "RDMA_CARD_RDMA_THREAD_8", linewidth = 2, marker = '^', color='#F2CB05')
for a, b in zip(Message_Size, RDMA_CARD_RDMA_THREAD_8):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_CARD_TCP_THREAD_8, label = "RDMA_CARD_TCP_THREAD_8", linewidth = 2, marker = 's', color='#F29F05')
for a, b in zip(Message_Size, RDMA_CARD_TCP_THREAD_8):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, NORMAL_CARD_TCP_THREAD_8, label = "NORMAL_CARD_TCP_THREAD_8", linewidth = 2, marker = 'v', color='#F28705')
for a, b in zip(Message_Size, NORMAL_CARD_TCP_THREAD_8):
    plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)


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
