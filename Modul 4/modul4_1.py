# (nim ganjil) Diketahui sebuah sebuah titik A (3,4) dengan gradien 2

# ● pertama, translasi dengan tx = 2 dan ty = -3,
# ● kemudian rotasi sejajar sumbu x positif sebesar 60 derajat,
# ● dan perbesaran skala dengan faktor skala 1.5 pada sumbu x dan faktor skala 2 pada
# sumbu y.

import math


def translasi(tx, ty):
    def transform(p):
        x, y = p
        return x + tx, y + ty
    return transform


def rotasi(sudut):
    def transform(p):
        x, y = p
        new_x = x * math.cos(math.radians(sudut)) - y * \
            math.sin(math.radians(sudut))
        new_y = x * math.sin(math.radians(sudut)) + y * \
            math.cos(math.radians(sudut))
        return new_x, new_y
    return transform


def dilatasi(sx, sy):
    def transform(p):
        x, y = p
        return x * sx, y * sy
    return transform


def line_equation_of(p1, M):
    x1, y1 = p1

    def hitung_konstanta(x):
        return M * (x - x1) + y1
    C = hitung_konstanta(0)
    return f"y = {M:.2f}x + {C:.2f}"


def transformasi_gabungan(*transforms):
    def decorator(func):
        def wrapper(p):
            result = p
            for transform in transforms:
                result = transform(result)
            return func(result)
        return wrapper
    return decorator


# Input dari pengguna
user_x = float(input("Masukkan nilai x untuk titik A: "))
user_y = float(input("Masukkan nilai y untuk titik A: "))
user_gradient = float(input("Masukkan nilai gradien (M): "))
user_tx = float(input("Masukkan nilai tx untuk translasi: "))
user_yx = float(input("Masukkan nilai tx untuk translasi: "))
user_p = float(input("Masukkan nilai p untuk rotasi: "))
user_sx = float(input("Masukkan nilai sx untuk dilatasi: "))
user_sy = float(input("Masukkan nilai sy untuk dilatasi: "))
point_A = (user_x, user_y)

print("Koordinat awal:")
print(point_A)

print(
    f"Persamaan garis yang melalui titik {point_A} dan bergradien {user_gradient}:")
print(line_equation_of(point_A, user_gradient))


@transformasi_gabungan(translasi(user_tx, user_yx), rotasi(user_p), dilatasi(user_sx, user_sy))
def transformasi_gabungan_line_equation(p):
    return p


print("Persamaan garis baru setelah transformasi:")
print(line_equation_of(transformasi_gabungan_line_equation(point_A), user_gradient))
