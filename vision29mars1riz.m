clc;clear;close all;

I = imread('D:\WorkFiles\rice.png');


figure;
imshow(I)
figure;
imhist(I)

[rws,cls]=size(I);

mag = zeros(rws,cls);

for i = 1:rws - 1
for j = 1:cls -1
    if I(i,j)>120
        I(i,j)=255;
    elseif I(i,j)<120
        I(i,j)=0;
    end
end
end

figure;
imagesc(I)
colormap gray

figure;
img3=medfilt2(I);
imshow(img3);


