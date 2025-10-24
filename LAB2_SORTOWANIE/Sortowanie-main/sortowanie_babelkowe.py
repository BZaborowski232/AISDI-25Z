import sys
import time
import gc
import matplotlib.pyplot as plt

try:
    n = int(sys.argv[1])
except:
    n = 100
text_file = sys.argv[2]

with open(text_file, "r", encoding="utf-8") as f:
    list_of_words = f.read().split()

list_of_words = list_of_words[:n]
for i, v in enumerate(list_of_words):
    list_of_words[i] = v.lower()

def bubble_sort(list_of_words):
    list_len = len(list_of_words)
    iteration = 0

    for i in range(list_len):
        for j in range(list_len - iteration - 1):
            if list_of_words[j] > list_of_words[j + 1]:
                a = list_of_words[j + 1]
                list_of_words[j + 1] = list_of_words[j]
                list_of_words[j] = a
        iteration += 1

    return list_of_words

list_lengths = list()
times = list()

for length in range(100, 5001, 100):
    lst = list_of_words[:length]
    gc_old = gc.isenabled
    gc.disable()
    start_time = time.time()
    bubble_sort(lst)
    end_time = time.time()
    if gc_old:
        gc.enable()

    list_lengths.append(length)
    times.append(end_time - start_time)

plt.plot(list_lengths, times, marker='o', color='b', linestyle='-')
plt.xlabel("Length of List")
plt.ylabel("Time Taken (seconds)")
plt.title("Time Complexity")
plt.grid(True)
plt.savefig("babelkowe.png")