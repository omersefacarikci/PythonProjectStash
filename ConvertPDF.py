# pdf2docx kütüphanesinden Converter sınıfını import ediyoruz
# Bu kütüphane, PDF dosyalarını Word (DOCX) formatına çevirmek için kullanılır
from pdf2docx import Converter

# Girdi olarak kullanılacak PDF dosyasının yolu
pdf_file = "enter path"  # Örn: "document.pdf"

# Çıktı olarak oluşturulacak DOCX dosyasının yolu
docx_file = "sampla.docx"  # Örn: "document.docx"

# Converter sınıfı ile PDF dosyasını açıyoruz
cv = Converter(pdf_file)

# PDF içeriğini DOCX formatına çeviriyoruz
cv.convert(docx_file)

# İşlem tamamlandıktan sonra Converter nesnesini kapatıyoruz
# Bu adım dosya kaynaklarını serbest bırakmak için önemlidir
cv.close()
