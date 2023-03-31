clc;clear;close all;
I = imread('D:\WorkFiles\rice.png');

SE = strel("disk",1);

[rws,cls]=size(I);

mag = zeros(rws,cls);

for i = 1:rws - 1
for j = 1:cls -1
    if I(i,j)>115
        I(i,j)=255;
    elseif I(i,j)<115
        I(i,j)=0;
    end
end
end

O = imopen(I,SE);
C = imclose(O,SE);

I2= bwperim(C);
figure;imshow(I2)

J = imclearborder(I2);
figure;imshow(J)

