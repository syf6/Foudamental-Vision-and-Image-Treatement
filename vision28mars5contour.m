clc;clear;close all;
t=[9 9];
I = imread('D:\WorkFiles\left.png');
I = rgb2gray(I);

figure;
imhist(I)

BW1 = edge(I,'sobel');
BW2 = edge(I,'canny'); %better

figure;
imshowpair(BW1,BW2,'montage')
