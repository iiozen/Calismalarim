%Komut penceresindeki yazýlarý workspacedeki girdileri ve açýk pencereleri
%kapatýyorum.
clear all
close all
clc

%fprintf ile kullanýcýya bilgi veriyorum. Daha sonra
%input komutu ile kullanýcýdan girdi alýp onu fotoðraf okumak için
%kullanýyorum.
fprintf('Kontrol edilmesi istenilen fotoðraf dosyasýný giriniz.Örn:"Foto1.png"\n')
girdi=input('\n Kontrol edilecek dosya:','s');
veri=imread(girdi);

%3 kanallý rgb fotoðrafýmý tek kanallý gri fotoðrafa dönüþtürüyorum.
yeni=rgb2gray(veri);

%gri fotoðrafý ise 2 bit siyah beyaz fotoðrafa dönüþtürüyorum.
renksiz=im2bw(yeni);

%üzerinde iþlem yapabilmek için siyah olan haplarýmý beyaz yapýyorum ve 
%arkaplaný ise siyah yapýyorum.
renksiz=1-renksiz;

%kontrol etmek için tam hapýn olduðu fotoðrafý okuyorum ve
%3 kanall rgb den griye daha sonra 2 bit siyah beyaz fotoðrafa
%dönüþtürüyorum. Ve hapýn üzerinde iþlem yapabilmek için hapý beyaz
%arkaplaný ise siyah yapýyorum.
tamhap=imread('Tam.png');
tamhapgri=rgb2gray(tamhap);
tamhap2bit=im2bw(tamhapgri);
tamhap2bit=1-tamhap2bit;

%imclose komutuyla 2 fotoðraftaki haplarýn içindeki olabilecek bazý boþluklarý
%kapatýyorum.
se=strel('disk',1);
tam=imclose(tamhap2bit,se);
renksiz=imclose(renksiz,se);

%Fotoðraftaki haplarý baðlantýlý bileþenlerine ayarýrak etiketliyorum ve
%alanlarýný matrislere kaydediyorum.
hap=bwconncomp(tam);
tamhap_analiz=regionprops(hap,'Area');
tamhapalan=cat(1,tamhap_analiz.Area);
etiket_kontrol=bwlabel(renksiz);
kontroledilen=bwconncomp(renksiz);
kontrol_analiz=regionprops(kontroledilen,'Area');
alanlar=cat(1,kontrol_analiz.Area);

%Tam hap'ýn alanýný kontrol edeceðim fotoðraftaki haplarýn alanlarýnda
%arýyorum. Bulduklarýmý etiket sýrasýna göre matrise kaydediyorum.
index=find(tamhapalan==alanlar);

%Kontrol ettiðim fotoðraftaki tam olan haplarý siyaha boyuyorum. Ve farklý
%ad ile kaydediyorum.
[m n]=size(index);
eksik=renksiz;
for j=1:m
    eksik(etiket_kontrol==index(j))=0;
end

%Kontrol ettiðim fotoðraftaki bir kýsmý eksik/kýrýk haplarý siyaha
%boyuyorum. Ve farklý ad ile kaydediyorum.
tamlarin=renksiz-eksik;

%Toplam hatasýz hap, toplam hap, toplam bir kýsmý eksik/kýrýk haplarýn
%sayýlarýný kaydediyorum.
[toplamhap n]=size(alanlar);
[toplamtamhap n]=size(index);
toplameksikhap=toplamhap-toplamtamhap;

%Bir kýsmý eksik/kýrýk olan haplarý kýrmýzýya boyuyorum.
[m n]= size(eksik);
for j=1:m
    for k=1:n
        if eksik(j,k)==1;
            eksik(j,k,1)=200;
            eksik(j,k,2)=0;
            eksik(j,k,3)=0;
        else
            eksik(j,k,1)=0;
            eksik(j,k,2)=0;
            eksik(j,k,3)=0;
        end
    end
end

%Hatasýz haplarý yeþile boyuyorum.
for j=1:m
    for k=1:n
        if tamlarin(j,k)==1;
            tamlarin(j,k,1)=0;
            tamlarin(j,k,2)=200;
            tamlarin(j,k,3)=0;
        else
            tamlarin(j,k,1)=0;
            tamlarin(j,k,2)=0;
            tamlarin(j,k,3)=0;
        end
    end
end

%Kýrmýzý ve Yeþile boyadýðým haplarý tek fotoðrafta birleþtiriyorum. Ve
%arka planý beyaza boyuyorum.
renkli=tamlarin+eksik;
for j=1:m
    for k=1:n
        if (renkli(j,k,1)+renkli(j,k,2)==0)
            renkli(j,k,1)=255;
            renkli(j,k,2)=255;
            renkli(j,k,3)=255;
        end
    end
end

%Kontrol edilecek fotoðrafý baþlýðýyla birlikte ekrana veriyorum.
imshow(veri);
title('Kontrol Edilecek Fotoðraf:');
figure;

%Kontrolden geçmiþ fotoðrafý baþlýðýyla birlikte ekrana veriyorum.
%Baþlýktaki yazýlarýn renklerini Toplam hap sayýsýný mavi, hatasýz ve
%hatalý hap sayýlarýný ise boyalý olduklarý renkleri veriyorum.
imshow(renkli);
t1='{\color{blue}Toplam hap sayýsý=';
t2=' {\color{red}Toplam bir kýsmý eksik/kýrýk hap sayýsý= ';
t3=' {\color{green}Toplam hatasýz hap sayýsý= ';
title([strcat(t1, int2str(toplamhap)),' adet.','}',strcat(t2,int2str(toplameksikhap)),' adet.','}',strcat(t3,int2str(toplamtamhap)),' adet.','}']);
