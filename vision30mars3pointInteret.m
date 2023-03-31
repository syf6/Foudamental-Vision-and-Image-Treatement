clc;?imread('D:\WorkFiles\c1Left.png');
I2 = rgb2gray(I);

%Detect corners using Harris–Stephens algorithm and return cornerPoints object
corners = detectHarrisFeatures(I2);
figure;
imshow(I2); hold on;
plot(corners.selectStrongest(500));

%Detect SURF features and return SURFPoints object
points = detectSURFFeatures(I2);
figure;
imshow(I2); hold on;
plot(points.selectStrongest(500)); % change here number of interesting points