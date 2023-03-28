clc;clear;close all;

core = 1/9 * [1 1 1;1 1 1;1 1 1];
I = imread('D:\WorkFiles\lennapoivreetsel.jpg');
I = rgb2gray(I);

[rws,cls]=size(I);

mag = zeros(rws,cls);

for i = 1:rws - 2
for j = 1:cls -2
    S1 = sum(sum(core.*double(I(i:i+2, j:j+2))));
    mag(i+1, j+1)=S1;
end
end
imshow(I);
figure;
imagesc(mag);
colormap gray

figure;
mag2=conv2(core,I);
imagesc(mag2);
colormap gray
