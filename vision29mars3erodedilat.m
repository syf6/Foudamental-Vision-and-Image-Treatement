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

figure;
imshow(I)
figure;
imhist(I)

%J = imdilate(I,SE);
%K = imerode(I,SE);
O = imopen(I,SE);
C = imclose(O,SE);

figure;
subplot(1,3,1);
imshow(I)
subplot(1,3,2);
imshow(O)
subplot(1,3,3);
imshow(C)


