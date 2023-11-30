# (nim ganjil) Diketahui sebuah sebuah titik A (3,4) dengan gradien 2

# ● pertama, translasi dengan tx = 2 dan ty = -3,
# ● kemudian rotasi sejajar sumbu x positif sebesar 60 derajat,
# ● dan perbesaran skala dengan faktor skala 1.5 pada sumbu x dan faktor skala 2 pada
# sumbu y.

def dilatasi(sx, sy):
    def transform(p):
        x, y = p
        return x * sx, y * sy
    return transform


def translasi(tx, ty):
    def transform(p):
        x, y = p
        return x + tx, y + ty
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


def line_equation_of(p1, M):
    x1, y1 = p1

    def hitung_konstanta(x):
        return M * (x - x1) + y1
    C = hitung_konstanta(0)
    return f"y = {M:.2f}x + {C:.2f}"


point_A = (3, 4)


# Translasi
count_translasi = translasi(2, -3)
final_translasi = count_translasi(point_A)
print(f"Koordinat setelah translasi: " + str(final_translasi))

# Rotasi
count_rotasi = rotasi(60)
final_rotasi = count_rotasi(final_translasi)
print(f"Koordinat setelah rotasi: " + str(final_rotasi))

# Dilatasi
count_dilatasi = dilatasi(1.5, 2)
final_dilatasi = count_dilatasi(final_rotasi)
print(f"Koordinat setelah dilatasi: " + str(final_dilatasi))

print("Persamaan garis yang melali titik (3, 4) dan bergradien 2:")
print(line_equation_of(point_A, 2))

print("Persamaan garis baru setelah transformasi:")
print(line_equation_of(final_dilatasi, 2))
