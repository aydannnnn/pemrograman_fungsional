# TODO 0 : Import library lain yang dibutuhkan
from PIL import ImageDraw, ImageFont, Image


# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('D:\ROSYDAN\Couple pink.jpg')


# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')


# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("D:\ROSYDAN\Font\Arcane Nine.otf", 24)
text = "Rosydan, 249"
text_width = draw.textlength(text, font)
text_height = font.size
text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill="white")


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('percobaan1.jpg')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
