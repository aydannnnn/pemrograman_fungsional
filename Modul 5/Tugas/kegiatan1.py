import matplotlib.pyplot as plt
from functools import reduce

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88,
                   92]

# TODO 1: Mencari Rata rata
average = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)
print(average)