random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_data = {}  # Dictionary untuk menyimpan nilai integer
float_data = ()  # Tuple untuk menyimpan nilai float
str_data = []  # List untuk menyimpan nilai string

for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka satuan, puluhan, dan ratusan
        ratusan = item // 100
        puluhan = (item % 100) // 10
        satuan = item % 10
        int_data[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        float_data += (item,)  # Tambahkan nilai float ke tuple
    elif isinstance(item, str):
        str_data.append(item)  # Tambahkan nilai string ke list

# Cetak hasil
print("Data Integer:")
for key, value in int_data.items():
    print(f"{key}: {value}")

print("\nData Float:")
print(float_data)

print("\nData String:")
print(str_data)