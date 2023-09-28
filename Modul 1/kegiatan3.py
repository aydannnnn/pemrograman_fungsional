# Sistem penilaian mahasiswa

# Tambahkan fungsi untuk menghitung nilai akhir
def menghitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

# Tambahkan fungsi untuk menghitung semua nilai akhir
def semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai
        nilai_akhir = menghitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        "Naruto": (30, 40),
        "Luffy": (70, 50),
        "Goku": (90, 100),
    }

    data_nilai_akhir =  semua_nilai_akhir(data_mahasiswa) # Menghitung nilai akhir semua mahasiswa
    tampilkan_nilai_akhir(data_nilai_akhir) 

if __name__ == "__main__":
    main()