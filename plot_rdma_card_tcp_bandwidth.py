import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
Message_Size = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24]
#math = [ 3.0, 3.0, 3.1, 8.2, 10.9, 13.6, 15.2, 15.5, 15.3, 15.8, ]

SHOW_TEXT_1 = np.round(np.array([89,120,224,289,534,537,748,1009,1329,1577,1951,2444,2793,2960,2925]) * 8 / 1000).astype(int)
SHOW_TEXT_2 = np.round(np.array([49,79,151,205,412,574,992,1618,1434,2031,2472,2751,2919,2887,2940]) * 8 / 1000).astype(int)
SHOW_TEXT_4 = np.round(np.array([8,17,57,84,221,363,819,1287,1216,2128,2710,3182,3168,3088,3122]) * 8 / 1000).astype(int)
SHOW_TEXT_8 = np.round(np.array([48,96,186,299,570,1019,1798,2458,2267,2914,3282,3190,3098,3074,3064]) * 8 / 1000).astype(int)
print("Message_Size\t1 Thread\t2 Thread\t4 Thread\t8 Thread")
for i in range(len(SHOW_TEXT_1)):
    print(f"{i + 10}\t\t{SHOW_TEXT_1[i]}\t\t{SHOW_TEXT_2[i]}\t\t{SHOW_TEXT_4[i]}\t\t{SHOW_TEXT_8[i]}")


RDMA_THREAD_1 = np.round(np.array([89,120,224,289,534,537,748,1009,1329,1577,1951,2444,2793,2960,2925]) * 8 / 1000).astype(int)
RDMA_THREAD_2 = np.round(np.array([49,79,151,205,412,574,992,1618,1434,2031,2472,2751,2919,2887,2940]) * 8 / 1000).astype(int)
RDMA_THREAD_4 = np.round(np.array([8,17,57,84,221,363,819,1287,1216,2128,2710,3182,3168,3088,3122]) * 8 / 1000).astype(int)
RDMA_THREAD_8 = np.round(np.array([48,96,186,299,570,1019,1798,2458,2267,2914,3282,3190,3098,3074,3064]) * 8 / 1000).astype(int)
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
    if a == 18:
        plt.text(a, b - 2, b, ha="center", va="bottom", fontsize = fontSize)
    else:
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_4, label = "4-THREAD", linewidth = 2, marker = 's', color='#F29F05')
for a, b in zip(Message_Size, RDMA_THREAD_4):
    if a == 17:
        plt.text(a, b - 1, b, ha="center", va="bottom", fontsize = fontSize)
    else:
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_2, label = "2-THREAD", linewidth = 2, marker = 'v', color='#F28705')
for a, b in zip(Message_Size, RDMA_THREAD_2):
    if a == 22:
        plt.text(a, b - 1, b, ha="center", va="bottom", fontsize = fontSize)
    elif a == 23:
        plt.text(a, b - 1.5, b, ha="center", va="bottom", fontsize = fontSize)
    else:
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)

plt.plot(Message_Size, RDMA_THREAD_1, label = "1-THREAD", linewidth = 2, marker = 'o', color='#F23030')
for a, b in zip(Message_Size, RDMA_THREAD_1):
    if a == 16:
        plt.text(a, b - 1, b, ha="center", va="bottom", fontsize = fontSize)
    else:
        plt.text(a, b, b, ha="center", va="bottom", fontsize = fontSize)


plt.plot(Message_Size, top, linewidth = 0)
plt.plot(Message_Size, low, linewidth = 0)

plt.xlabel("Log Scale Message Size (Byte)", fontsize=fontSize,)
plt.ylabel("Bandwidth (Gbps)", fontsize=fontSize,)

plt.xticks(fontsize=fontSize,)
plt.yticks(fontsize=fontSize,)


plt.legend(fontsize = 15.3, loc="lower right")
plt.title("RDMA Card TCP Bandwidth")
plt.show()
# plt.savefig("line_cpu.pdf", dpi = 200)#, bbox_inches="tight")
