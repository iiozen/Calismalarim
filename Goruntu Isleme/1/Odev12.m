clear all
close all
clc
se=strel('disk',15);
gercek=imread('PCBbw.bmp');
kontrol=imread('PCBcont.bmp');
fark=gercek-kontrol;
concomp=bwconncomp(fark,8);
analiz=regionprops(concomp,'Centroid');
centroids=round(cat(1,analiz.Centroid))
[M N]=size(centroids);
[K L]=size(fark);
for p=1:K
    for g=1:L
        A(p,g)=0;
    end
end
for i=1:M
   A(centroids(i,2),centroids(i,1))=1;
end
%imshow(fark);
%figure;
A=imdilate(A,se);
A=bwmorph(A,'remove');
%imshow(A);

red_mask=xor(A,kontrol);
red_mask=A-red_mask;

Result=uint8((kontrol|A)*255);
Result(:,:,2)=uint8((kontrol-red_mask)*255);
Result(:,:,3)=uint8((kontrol-red_mask)*255);
imshow(Result);
title('Hatalý yerler kýrmýzý yuvarlak sembollerle vurgulanmýþtýr.');




 
