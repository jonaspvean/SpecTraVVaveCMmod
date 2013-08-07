function testWh(c,vini,NN,dt,num);
% testWh(speed, initial data, NN, dt, number of periods)


% *************************************************************************** %
% u_t + 2 uu_x + K_h*u_x = 0 = 0   on 0 < x < L
%
%
%
% solved here via Adams-Bashforth-Crank-Nicholson (not optimal)
%
% Adams-Bashforth for nonlinear term
%
% Crank-Nicholson for linear term
%
% 
% ************** Define grid  **************
% 

hh  = 2*pi/NN;
xx = (0:hh:2*pi-hh);


%
% ************************************************ %
% 
% ************** Define operators  **************
%
 

k=[(1:NN/2)';(1-NN/2:-1)'];
whitha  = i*k.*sqrt(tanh(k)./k);
whitham =[0;whitha];                              % lim (whitha) xi -> 0 = 0
whitham(NN/2+1)=0;                                % avoid aliasing due to asym. FFT


k=[(0:NN/2-1)';0;(1-NN/2:-1)'];


m=0.5*dt*whitham;
d1=(1-m)./(1+m);      
d2= -0.5*i*dt*k./(1+m);

d1(NN/2+1)=0;                                      % avoid aliasing due to asym. FFT

%
% ************ Graphics **************************
%
%
 sol = plot(xx,xx,'Erasemode','background');
 axis([0 2*pi  -1 1]); zoom; 
 title('KdV: Error'); drawnow;


%
% ************* Initialize functions *************
%
 u = vini;
%
% ************** Time loop **************************
%

 T = 2*pi/c; 
 eps=1e-10;
 t=dt;
 %tic;
 it=0;
 while t < num*T;                        % number of periods * T 
     fftu=fft(u); 
%      fftuu=fft(u.^2);      %square
   fftuu=fft(2*(u+1).^(3/2)-3*u-2);     %square root
%    fftuu=fft(u.^3);       %cubic
     v=real(ifft(d1.*fftu +d2.*fftuu));
     w=real(ifft(d1.*fftu +2*d2.*fftuu));
     w_old=w;
     err=1;
     while err > eps
         it = it+1;
%          if it > 5000;
%              break;
%          end;
       w=v+real(ifft(d2.*fft(2*(w_old+1).^(3/2)-3*w_old-2)));   %square root
%        w=v+real(ifft(d2.*fft(w_old.^3)));         %cubic
         err=norm(w-w_old,2);
         w_old=w;
     end; 
         u=w;
         t=t+dt;
         set(sol,'ydata',u);       
 end;
%toc;

Error = sqrt(trapz(xx,(abs(u-vini)).^2))
MaxError = abs(max(vini)-max(u))  
Norm = norm(u-vini,inf)

plot(xx,vini,xx,u,'--')
axis([0 2*pi  -1 1]); zoom on; 





