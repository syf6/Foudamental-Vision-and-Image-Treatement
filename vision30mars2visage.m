clc;clear;close all;
I = imread('D:\WorkFiles\visages.jpg');

figure; imshow(I)

% Create a cascade detector object.
faceDetector = vision.CascadeObjectDetector();

bbox = faceDetector(I); %bounding box of objects

% Draw the returned bounding box around the detected face.
I = insertShape(I, "rectangle", bbox);
figure; imshow(I); title("Detected face");