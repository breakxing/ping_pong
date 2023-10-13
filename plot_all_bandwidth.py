import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]

SHOW_TEXT_1 = np.round(np.array([30,59,86,111,164,220,233,233,114,115,116,116,117,117,117]) * 8 / 1000).astype(int)
SHOW_TEXT_2 = np.round(np.array([48,96,186,299,570,1019,1798,2458,2267,2914,3282,3190,3098,3074,3064]) * 8 / 1000).astype(int)
SHOW_TEXT_3 = np.round(np.array([622,1183,2027,3304,4576,5489,5621,5560,5553,5512,5502,5503,5505,5453,5504]) * 8 / 1000).astype(int)
print("Message_Size\tNORMAL_CARD_TCP_THREAD_8\tRDMA_CARD_TCP_THREAD_8\tRDMA_CARD_RDMA_THREAD_8")
for i in range(len(SHOW_TEXT_1)):
    print(f"{i + 10}\t\t{SHOW_TEXT_1[i]}\t\t\t\t{SHOW_TEXT_2[i]}\t\t\t{SHOW_TEXT_3[i]}")


NORMAL_CARD_TCP_THREAD_8 = np.round(np.array([30,59,86,111,164,220,233,233,114,115,116,116,117,117,117]) * 8 / 1000).astype(int)
RDMA_CARD_TCP_THREAD_8   = np.round(np.array([48,96,186,299,570,1019,1798,2458,2267,2914,3282,3190,3098,3074,3064]) * 8 / 1000).astype(int)
RDMA_CARD_RDMA_THREAD_8  = np.round(np.array([622,1183,2027,3304,4576,5489,5621,5560,5553,5512,5502,5503,5505,5453,5504]) * 8 / 1000).astype(int)
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
plt.ylabel("Bandwidth (Gbps)", fontsize=fontSize,)

plt.xticks(fontsize=fontSize,)
plt.yticks(fontsize=fontSize,)


plt.legend(fontsize = 10, loc="best")
plt.title("RDMA Bandwidth")
plt.show()
# plt.savefig("line_cpu.pdf", dpi = 200)#, bbox_inches="tight")
