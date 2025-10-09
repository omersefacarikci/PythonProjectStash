import pytube  # pytube kütüphanesini import ediyoruz, YouTube videolarını indirmek için kullanılır

# Kullanıcıdan indirmek istediği YouTube videosunun URL'sini alıyoruz
url = input("URL giriniz: ")

# Video indirileceği klasör yolu (boş bırakılırsa mevcut klasöre indirilir)
path = ""

# YouTube nesnesi oluşturuyoruz
yt = pytube.YouTube(url)

# En düşük çözünürlükteki video streamini seçiyoruz
# Örneğin 144p veya 240p gibi küçük boyutlu videoları indirir
# Avantaj: Küçük boyutlu ve hızlı indirilir
# Dezavantaj: Görüntü kalitesi düşüktür
video_low = yt.streams.get_lowest_resolution()

# Videoyu indiriyoruz
video_low.download(path)

# -------------------------
# Eğer en yüksek çözünürlükte indirmek istersek:
# video_high = yt.streams.get_highest_resolution()
# video_high.download(path)
# Bu metot 1080p, 4K gibi yüksek çözünürlüklü videoları indirir
# Avantaj: Görüntü kalitesi yüksek
# Dezavantaj: Dosya boyutu büyük ve indirme süresi uzun
