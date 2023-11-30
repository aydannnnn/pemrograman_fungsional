# Percobaan 4 (transformasi)

# Buatlah 3 fungsi untuk menghitung tranformasi secara tranlasi, dilatasi, dan rotasi. Dengan contoh kasus sebagai berikut:
# Sebuah titik P memiliki koordinat (3, 5).

# 1. Jika titik tersebut mengalami translasi dengan tx = 2 dan ty = -1, tentukan koordinat titik baru setelah translasi
# 2. Jika titik tersebut mengalami dilatasi dengan sx = 2 dan sy = -1, tentukan koordinat titik baru setelah dilatasi
# 3. Jika titik tersebut mengalami rotasi dengan sudut = 30 derajat, tentukan koordinat titik baru setelah rotasi.

# jangan lupa untuk ngoding secara fungsional ya
# kalian bisa memanfaatkan inner fucntion(bahkan fungsi lambda) dan closure disini

def translasi(tx, ty):
    def transform(p):
        x, y = p
        return x + tx, y + ty
    return transform


def dilatasi(sx, sy):
    def transform(p):
        x, y = p
        return x * sx, y * sy
    return transform


def rotasi(sudut):
    import math

    def transform(p):
        x, y = p
        new_x = x * math.cos(math.radians(sudut)) - y * \
            math.sin(math.radians(sudut))
        new_y = x * math.sin(math.radians(sudut)) + y * \
            math.cos(math.radians(sudut))
        return new_x, new_y
    return transform


point_P = (3, 5)

# Translasi
count_translasi = translasi(2, -1)
final_translasi = count_translasi(point_P)
print(f"Koordinat setelah translasi: " + str(final_translasi))

# Dilatasi
count_dilatasi = dilatasi(2, -1)
final_dilatasi = count_dilatasi(point_P)
print(f"Koordinat setelah dilatasi: " + str(final_dilatasi))

# Rotasi
count_rotasi = rotasi(30)
final_rotasi = count_rotasi(point_P)
print(f"Koordinat setelah rotasi: " + str(final_rotasi))

# contoh output:
