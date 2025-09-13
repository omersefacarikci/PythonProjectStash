# rembg kütüphanesini import ediyoruz
# Bu kütüphane, görüntülerdeki arka planı kaldırmak için kullanılır
from rembg import remove

# Girdi olarak kullanılacak resim dosyasının yolu
input_path = "image.jpeg"

# Arka planı kaldırıldıktan sonra kaydedilecek dosyanın yolu
# PNG formatı kullanıyoruz çünkü şeffaf arka plan destekliyor
output_path = "output.png"

# Girdi dosyasını 'rb' (read binary) modunda açıyoruz
with open(input_path, 'rb') as i:
    # Çıktı dosyasını 'wb' (write binary) modunda açıyoruz
    with open(output_path, 'wb') as o:
        # Girdi dosyasını okuyoruz (binary formatında)
        input_file = i.read()
        
        # rembg kütüphanesinin remove fonksiyonunu kullanarak
        # arka planı kaldırıyoruz
        output_file = remove(input_file)
        
        # Arka planı kaldırılmış veriyi çıktı dosyasına yazıyoruz
        o.write(output_file)
