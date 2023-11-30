# Percobaan 6 (mencari persamaan garis melalui 1 titik)
# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GANJIL

def point(x, y):
    return x, y


def line_equation_of(p1, M):
    x1, y1 = p1

    def hitung_konstanta(x):
        return M * (x - x1) + y1
    # TODO 1: tulis rumus untuk mendapatkan nilai C disini
    C = hitung_konstanta(0)
    return f"y = {M:.2f}x + {C:.2f}"


print("Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
# ubah nilai input dengan 3 digit nim akhir kalian
print(line_equation_of(point(2, 4), 9))
# dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
# untuk membuktikan bahwa output sudah benar
