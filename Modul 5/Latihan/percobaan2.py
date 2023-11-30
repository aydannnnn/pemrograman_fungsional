import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
ypoints = np.array([3, 5, 5, 7, 1, 4, 6, 10, 10, 9, 2, 12])

plt.figure(figsize=(10, 5))
plt.title('Grafik Penjualan Baso Boraks Tahun 2020')
plt.plot(xpoints, ypoints, color='red', marker='o')
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.xticks(xpoints, labels=["Jan", "Feb", "Mar", "Apr",
           "Mei", "Jun", "Jul", "Agt", "Sep", "Okt", "Nov", "Des"])
plt.xlabel('Bulan', fontsize=15)
plt.ylabel('Total Bill', fontsize=15)
plt.show()
