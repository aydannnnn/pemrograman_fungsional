# Percobaan 5 (mencari persamaan garis melalui 2 titik)

# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GANJIL

def point(x, y):
    return x, y


def line_equation_of(p1, p2):
    # TODO 1: gunakan inner function dan closure untuk menghitung nilai M
    x1, y1 = p1
    x2, y2 = p2

    # TODO 2: panggil fungsi inner untuk mendapatkan nilai M
    M = (y2 - y1) / (x2 - x1)
    C = y1 - M * x1  # TODO 3: tulis rumus untuk mendapatkan nilai C disini
    return f"y = {M:.2f}x + {C:.2f}"


print("Persamaan garis yang melalui titik A dan B:")
# ubah nilai input dengan 4 digit nim akhir kalian
print(line_equation_of(point(1, 2), point(4, 9)))
# dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
# untuk membuktikan bahwa output sudah benar
