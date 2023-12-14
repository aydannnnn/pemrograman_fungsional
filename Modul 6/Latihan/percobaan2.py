# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import ImageDraw, ImageFont, Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('D:\ROSYDAN\Couple pink.jpg')
overlay_image = Image.open('D:\ROSYDAN\Couple pink.jpg')

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.copy()
overlay_image = overlay_image.convert('RGB')


# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
overlay_image = overlay_image.resize((int(overlay_image.width * 0.5), int(overlay_image.height * 0.5)))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = int((background_image.width - overlay_image.width) / 2)
y_center = int((background_image.height - overlay_image.height) / 2)


# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))


# TODO 5 : Simpan gambar hasil edit
background_image.save('percobaan2.jpg')

# TODO 6 : Tampilkan
background_image.show()
