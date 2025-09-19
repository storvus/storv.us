import qrcode
from PIL import Image


# qr = qrcode.QRCode

# qrcode.make("http://localhost:63342/storv.us/quest107c2c93-3680-430d-be12-786dce7769d1.html?_ijt=291lt058hen75437pdogu0j7ni").save("qrcode.png")

url = "https://storvus.github.io/storv.us/squish.html"
qr = qrcode.QRCode(
    version=1,  # размер (1–40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # высокий уровень коррекции (чтобы не повредился при вставке лого)
    box_size=10,  # размер "квадратиков"
    border=4,     # рамка
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# # Добавим лого
# logo = Image.open("two.png")  # сюда можно свой файл
# logo_size = 80  # размер лого
#
# # Масштабируем логотип
# logo.thumbnail((logo_size, logo_size))
#
# # Координаты для вставки по центру
# pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
# img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

img.save("images/squish.png")
