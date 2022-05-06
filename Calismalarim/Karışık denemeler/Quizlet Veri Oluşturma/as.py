from textbirlestirme import DosyaBirlestir
# İngilizce Kelimelerin bulunduğu konum
kelimeler = ""
# Türkçe Kelimelerin bulunduğu konum
words = ""
yazdirilanisim = 'kelime2'
# Çıktının yazdıralacağı konum
yazdirmakonum = ''
yazdirma = [yazdirmakonum,yazdirilanisim]
birlestir = DosyaBirlestir(
    words=words,
    kelimeler=kelimeler,
    yazdirma=yazdirma,
    ayirac=',',
    kelimelimit=50,
    kelimeminlimit=30,
    ayirac2=';'
    )


