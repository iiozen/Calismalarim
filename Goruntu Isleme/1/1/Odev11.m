close all
clear all
clc
civata=imread('civatabw.bmp');

se=strel('disk',5);
civata=imclose(civata,se);
civata=imopen(civata,se);

con=bwconncomp(civata);
etiket_civata=bwlabel(civata);

analiz=regionprops(con,'Area','Centroid','Orientation');
alanlar=cat(1,analiz.Area);
[f d]=size(alanlar);
max_alan=max(alanlar);
aci=cat(1,analiz.Orientation);
aci1=-10>aci;
aci2=aci>10;
var=find(aci1|aci2);

index=find((max_alan-max_alan*0.25)>alanlar);

siyah=logical(zeros(size(civata)));
siyah2=logical(zeros(size(civata)));
if(sum(index)+sum(var)>0)
    [u c]=size(index);
    [h g]=size(var);
  for j=1:u
       siyah(etiket_civata==index(j))=1;
  end
    for v=1:h
          siyah2(etiket_civata==var(v))=1;
       end
    i2=civata.*siyah;
    i3=civata.*siyah2;
       irgb(:,:,3)=civata-i2-i3;
       irgb(:,:,2)=i3;
       irgb(:,:,1)=i2;
       imshow(irgb);
       title(sprintf('Toplam %d adet nesne mevcut. Açýsal hatalý: %d adet Boyut hatalý: %d adet.',f,h,u));
else
    imshow(civata);
    title('Nesnelerde hiç hata yok.');
end