h=fspecial("gaussian",[200 200],50); %sigma is variance
imagesc(h)
figure;
mesh(h)
