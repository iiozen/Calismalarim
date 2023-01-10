
## NLP DOSYASI

NLP dosyasında verisetinden aldığımız csvleri düzenleme, veri ön işleme, eğitim ve
modeli kaydetme ve main.py altında çalışan girilen metnin
konularını bulup google'dan arama yaparak cevap veren ve
bu işlemleri sqllite 3 üzerinden robot.db'e kaydeden fonksiyonlar vardır.

-main.py ile mülakatta istenilen konu bulan sql'e yazdıran ve google üzerinden arayıp cevap
veren işlemler yapılır.
-robot.py tüm işlemlerin yapıldığı sınıf dosyasıdır.
-onisleme.py türkçe metinlerin ön işlemesinin yapılması için yazılmış fonksiyonları barındırır.
-trkarakter.py onisleme'de kullanılan türkçe karakterler için oluşturulmuştur.
-egitimehazirla.py verisetinden gelen csv dosyasını onisleme.py ile işleyerek düzenler.
-egitim.py veriler ile eğitim yapar ve sonucu olan .joblib uzantılı
modelleri export eder ve bunları robot.py de import edebilmemizi ve kullanmamızı sağlar.
-etkisizKelimeler.py stopwords olarak geçen etkisizkelimelerin onislemede kullanılabilmesi için vardır.
-requirements.txt dosyalardaki python kodlarında kullanılan tüm kütüphaneleri listeler.

## Veriseti Dosyası

Veriseti dosyasında habertürk sitesinden alınan kategorize haber başlık ve linklerini içerir.
-requirements.txt bu dosyadaki tüm python kodlarında kullanılan kütüphaneleri listeler.
-verisetiDict.py linklerin bulunduğu dosya konumlarını ve adlarını içerir.
-Linktoplama klasörünün altındaki tüm python dosyaları sitelerden link toplama ve txt uzantılarına yazmayı üstlenir.
-veriDondurme.py Linktoplama altındaki txt dosyalarındaki linkleri verisetiDict üzerinden bulur ve
linklerdeki başlık, alt_başlık ve içerik metinlerini toplar.
-veritoplama.py veriDondurme.py dosyasındaki fonksiyonlarla toplanan verileri indexleyerek csv halinde veriyi oluşturur.
