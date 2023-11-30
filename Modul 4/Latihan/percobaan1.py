# Percobaan 1 (penerapan closure dengan currying):
# Tulis kembali kode diatas kemudian panggil(run) dengan dua cara:
# 1. HOF
# 2. currying

def perkalian(a):
    def dengan(b):
        return a*b
    return dengan


hasil_hof = perkalian(2)(3)
print("Hasil Currying:", hasil_hof)

hasil_curry = perkalian(2)
hasil_curry = hasil_curry(3)
print("Hasil Hof:", hasil_curry)
