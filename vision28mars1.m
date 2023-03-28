clc;clear;close all;
%I = imread('pout.tif');
I = imread('D:\WorkFiles\flower.jpg');
I = rgb2gray(I);
imshow(I)
figure;
imhist(I) %histogram

%normalization
maxI=max(max(I));
minI=min(min(I));
IN = (255*double((I-minI)))/double(maxI-minI);

figure;
%imshow(IN)
imagesc(IN);colormap gray
figure;
imhist(uint8(IN)) %it only accept 8 bit so we need to cast

%equalization
IE = histeq(I);
figure;
imshow(IE)
figure;
imhist(IE)