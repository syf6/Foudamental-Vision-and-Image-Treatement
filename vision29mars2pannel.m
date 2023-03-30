clc;clear;close all;

rgbImage = imread('D:\WorkFiles\panneaux.png');

% Extract color channels.
redChannel = rgbImage(:,:,1); % Red channel
greenChannel = rgbImage(:,:,2); % Green channel
blueChannel = rgbImage(:,:,3); % Blue channel

figure; imshow(redChannel)
figure; imhist(redChannel)
figure; imshow(greenChannel)
figure; imhist(greenChannel)
figure; imshow(blueChannel)
figure; imhist(blueChannel)

[rws,cls]=size(rgbImage(:,:,1));

for i = 1:rws 
for j = 1:cls
    if redChannel(i,j)<100 && greenChannel(i,j)<90 && blueChannel(i,j)>145
        res(i,j)=255;
    else
        res(i,j)=0;
    end
end
end

figure;
imagesc(res)
colormap gray

