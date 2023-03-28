clc;clear;close all;
t=[9 9];
I = imread('D:\WorkFiles\lenna.bmp');
I = rgb2gray(I);

Ib = imnoise(I,"salt & pepper");

figure;
subplot(1,4,1);
imagesc(Ib);
colormap gray
title('add noise');

%average filter
subplot(1,4,2);
H1 = fspecial('average',t);
img1 = imfilter(Ib,H1);
imagesc(img1);
colormap gray


%gaussain gaussian
subplot(1,4,3);
H2 = fspecial('gaussian',t,1);
img2 = imfilter(Ib,H2);
imagesc(img2);
colormap gray


%median non linear
subplot(1,4,4);
img3=medfilt2(Ib);
imshow(img3);
