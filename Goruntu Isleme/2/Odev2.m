clear all
close all
clc
fprintf('Kontrol edilmesi istenilen dosyayý giriniz.Örn:"normal.png"\n')
girdi=input('\n Kontrol edilecek dosya:','s');
veri=imread(girdi);
yeni=rgb2gray(veri);
[a b]=size(yeni);
for i=1:a
    for j=1:b
        cizgi1(i,j)=yeni(i,j)*255;
    end
end


cizgi1=255-cizgi1;
cizgi=im2bw(cizgi1);
concomp=bwconncomp(cizgi);
analiz=regionprops(concomp,'Area','Centroid');
centroids=round(cat(1,analiz.Centroid));
[M N]=size(centroids);
ov=1;
for j=N:-1:1
    cizgix(ov,1)=centroids(j,2);
    ov=ov+1;
end



sybyz1=im2bw(yeni);
se=strel('disk',15,0);


i=veri;
sybyz=imclose(sybyz1,se);
etiket_top=bwlabel(sybyz);
coni=bwconncomp(sybyz);
stats=regionprops(coni,'Area','Centroid');
centroid=round(cat(1,stats.Centroid));
[m n]=size(centroid);
for j=1:m
    toppikselleri(j,1)=centroid(j,2);
    toppikselleri(j,2)=centroid(j,1);
end
for j=1:m
    toplar(1,j)=i(toppikselleri(j,1),toppikselleri(j,2));
end
yesil1=find((toplar<200)&(toplar>100));
sari1=find(toplar>200);
yesil=length(yesil1);
sari=length(sari1);
[t z]=size(cizgix);
imshow(veri,[]);
for j=1:sari
    sarihata1(j,1)=toppikselleri(sari1(1,j),1);
    sarihata1(j,2)=toppikselleri(sari1(1,j),2);
end
sar=1;
sarhata=0;
for j=1:sari
    if sarihata1(j,1)>cizgix(1,1)
        sarihata(sar,1)=sarihata1(j,1);
        sarihata(sar,2)=sarihata1(j,2);
        sar=sar+1;
        sarhata=sarhata+1;
        hold on
        plot(sarihata(:,2),sarihata(:,1),'r*');
    end
end
for j=1:yesil
    yesilhata1(j,1)=toppikselleri(yesil1(1,j),1);
    yesilhata1(j,2)=toppikselleri(yesil1(1,j),2);
end
yes=1;
yeshata=0;
for j=1:yesil
    if yesilhata1(j,1)< cizgix(2,1)
        yesilhata(yes,1)=yesilhata1(j,1);
        yesilhata(yes,2)=yesilhata1(j,2);
        yes=yes+1;
        yeshata=yeshata+1;
        hold on
        plot(yesilhata(:,2),yesilhata(:,1),'b*');
    end
end
title(sprintf('Toplam Sarý Top Sayýsý=%i\nToplam Yeþil Top Sayýsý=%i\nHatalý Konumlanmýþ Sarý Top Sayýsý=%i\nHatalý Konumlanmýþ Yeþil Top Sayýsý=%i',sari,yesil,sarhata,yeshata));
hold off
figure;
imshow(i);
title('Girdi Görüntüsü:');
    




















