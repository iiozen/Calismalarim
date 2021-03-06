%Komut penceresindeki yaz?lar? workspacedeki girdileri ve a??k pencereleri
%kapat?yorum.
clear all
close all
clc

%fprintf ile kullan?c?ya bilgi veriyorum. Daha sonra
%input komutu ile kullan?c?dan girdi al?p onu foto?raf okumak i?in
%kullan?yorum.
fprintf('Kontrol edilmesi istenilen foto?raf dosyas?n? giriniz.?rn:"Foto1.png"\n')
girdi=input('\n Kontrol edilecek dosya:','s');
veri=imread(girdi);

%3 kanall? rgb foto?raf?m? tek kanall? gri foto?rafa d?n??t?r?yorum.
yeni=rgb2gray(veri);

%gri foto?raf? ise 2 bit siyah beyaz foto?rafa d?n??t?r?yorum.
renksiz=im2bw(yeni);

%?zerinde i?lem yapabilmek i?in siyah olan haplar?m? beyaz yap?yorum ve 
%arkaplan? ise siyah yap?yorum.
renksiz=1-renksiz;

%kontrol etmek i?in tam hap?n oldu?u foto?raf? okuyorum ve
%3 kanall rgb den griye daha sonra 2 bit siyah beyaz foto?rafa
%d?n??t?r?yorum. Ve hap?n ?zerinde i?lem yapabilmek i?in hap? beyaz
%arkaplan? ise siyah yap?yorum.
tamhap=imread('Tam.png');
tamhapgri=rgb2gray(tamhap);
tamhap2bit=im2bw(tamhapgri);
tamhap2bit=1-tamhap2bit;

%imclose komutuyla 2 foto?raftaki haplar?n i?indeki olabilecek baz? bo?luklar?
%kapat?yorum.
se=strel('disk',1);
tam=imclose(tamhap2bit,se);
renksiz=imclose(renksiz,se);

%Foto?raftaki haplar? ba?lant?l? bile?enlerine ayar?rak etiketliyorum ve
%alanlar?n? matrislere kaydediyorum.
hap=bwconncomp(tam);
tamhap_analiz=regionprops(hap,'Area');
tamhapalan=cat(1,tamhap_analiz.Area);
etiket_kontrol=bwlabel(renksiz);
kontroledilen=bwconncomp(renksiz);
kontrol_analiz=regionprops(kontroledilen,'Area');
alanlar=cat(1,kontrol_analiz.Area);

%Tam hap'?n alan?n? kontrol edece?im foto?raftaki haplar?n alanlar?nda
%ar?yorum. Bulduklar?m? etiket s?ras?na g?re matrise kaydediyorum.
index=find(tamhapalan==alanlar);

%Kontrol etti?im foto?raftaki tam olan haplar? siyaha boyuyorum. Ve farkl?
%ad ile kaydediyorum.
[m n]=size(index);
eksik=renksiz;
for j=1:m
    eksik(etiket_kontrol==index(j))=0;
end

%Kontrol etti?im foto?raftaki bir k?sm? eksik/k?r?k haplar? siyaha
%boyuyorum. Ve farkl? ad ile kaydediyorum.
tamlarin=renksiz-eksik;

%Toplam hatas?z hap, toplam hap, toplam bir k?sm? eksik/k?r?k haplar?n
%say?lar?n? kaydediyorum.
[toplamhap n]=size(alanlar);
[toplamtamhap n]=size(index);
toplameksikhap=toplamhap-toplamtamhap;

%Bir k?sm? eksik/k?r?k olan haplar? k?rm?z?ya boyuyorum.
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

%Hatas?z haplar? ye?ile boyuyorum.
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

%K?rm?z? ve Ye?ile boyad???m haplar? tek foto?rafta birle?tiriyorum. Ve
%arka plan? beyaza boyuyorum.
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

%Kontrol edilecek foto?raf? ba?l???yla birlikte ekrana veriyorum.
imshow(veri);
title('Kontrol Edilecek Foto?raf:');
figure;

%Kontrolden ge?mi? foto?raf? ba?l???yla birlikte ekrana veriyorum.
%Ba?l?ktaki yaz?lar?n renklerini Toplam hap say?s?n? mavi, hatas?z ve
%hatal? hap say?lar?n? ise boyal? olduklar? renkleri veriyorum.
imshow(renkli);
t1='{\color{blue}Toplam hap say?s?=';
t2=' {\color{red}Toplam bir k?sm? eksik/k?r?k hap say?s?= ';
t3=' {\color{green}Toplam hatas?z hap say?s?= ';
title([strcat(t1, int2str(toplamhap)),' adet.','}',strcat(t2,int2str(toplameksikhap)),' adet.','}',strcat(t3,int2str(toplamtamhap)),' adet.','}']);
