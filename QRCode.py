# pyqrcode kütüphanesini import ediyoruz
# Bu kütüphane, QR kodları oluşturmak için kullanılır
import pyqrcode

# Kullanıcıdan QR kodunu oluşturmak istediği URL'yi alıyoruz
url = input("URL giriniz: ")

# QR kodunu oluşturuyoruz
# create() fonksiyonu verilen URL veya metni QR kod formatına çevirir
qrcode = pyqrcode.create(url)

# Oluşturulan QR kodunu SVG formatında kaydediyoruz
# 'qrcode.svg' → dosya adı
# scale=5 → QR kodunun büyüklüğü (her bir kare 5 birim büyüklüğünde)
qrcode.svg('qrcode.svg', scale=5)
