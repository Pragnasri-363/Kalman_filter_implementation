# Filtering IMU, GPS with Kalman filter for SAR Drone Tracking
A deep dive into how technology can be a boon to mankind. 

### Motivation behind this project?
My time as a content writer in my colleges techno-environmental club made me understand how our actions are causing natural calamities, and that we are not able to rescue people on time due to physical limitations(not being able to reach on time), so in cases like this we can use the technology for our advantage where the immediate first aid or identification of causalities can be done by SAR drones, but they need to be highly accurate, so we need to reduce the noise as much as possible which can be done with filter like a Kalman filter which showed great results in space missions.

### Let's get started with what is Kalman Filter?
It is a model used to observe the system's behavior over time-dynamic model. It uses two step predict and update to find the state of the system.It is first used in space shuttle trackig.But the question is why do we need it when we have GPS and LiDAR, RADAR.To answer this we should know the drawbacks of GPS such as: noisy measurements, inefficient during intentional jamming, bad weather. So to provide seamless services we integrate GPS and other systems like IMU with kalman filter to reduce noise for tracking of SAR drones.

### Drawbacks in IMU and GPS:
IMU contains gyroscope, accelerometer and magnetometer. 
Gyroscope- it drifts over time, this cannot be trusted for long timespan but it's quite precise for short span.
Accelerometer- it doesn't have drift but it's too unstable or we can say noisy during motion.
Magnetometer- it's disturbed by nearby metal.
GPS-it's inefficient during satellite drift,scattering,bad weather or intentional jamming and has noisy sensor measurements.
How to overcome this? We'll integrate Kalman Filter to reduce the sensor noise present in these.We are specially dealing with nonlinear kalman filter which is Extended Kalman Filter as it's more suitable for complex scenarios when compared to linear Kalman filter.

### How do we implement a Kalman Filter:
In the Kalman filter there are linear and non linear types, non linear include extended and unscented kalman filter. But for now we'll discuss only linear kalman filter and in the later discussion we'll move forward to non-linear kalman filter.
Kalman filter has two main steps: prediction and Update
Let's discuss what happens in the prediction step:
Let the state of the vehicle be represented using a linear motion model(not ideal for real life scenario) subject to Gaussian noise, where xk and xk−1 are the
state vectors at time k and k − 1. And uk represents the control variables (external effects such as acceleration, thrust,and gravity) and wk is the gaussian noise.
The state equation of the Kalman filter is defined as the following:
xk = Axk−1 + Buk + wk ---------(1)
The linear measurement model with gaussian noise or the observation equation is :
zk = Hxk + vk ---------(2)
To compute the uncertainty in the prediction, we evaluate the covariance of the prediction residual, where A represents the motion model matrix and Pk−1 is the covariance of initial state and Q is the process gaussian noise.
P−k = APk−1AT + Q -----------(3)
After making a prediction(using mathematical equation) and obtaining a measurement (from GPS), we compute the error yk, which is the difference between measurement zk and prediction Hx−k to find how uncertain we are with the prediction made. The uncertainty in measurement might be due to SNR, time on target.
yk = zk − Hx−k------------------(4)
And compute the residual covariance Sk, which tells us how much uncertain is the error, which helps understand how much correction is to be made in error. Uncertainty in error can be caused due to prediction uncertainty and GPS noise.
Sk = HP −k HT + R --------------(5)
After this Kalman gain is estimated to know how much to trust the prediction vs measurement or we can say how much to correct. If Kk approaches 1, the filter trusts the measurement more, whereas if Kk approaches 0, the filter relies more on prediction.
Kk = P−k HT(HP −k HT + R)−1 ------------------(6)
Now comes the second phase of the Kalman filter which is update, we update the state by multiplying the Kalman gain Kk and the error yk and add the predicted output x−k to get the estimate of the new position.
xk = x−k + Kkyk ------------(7)
<p align="center">
  <img width="80%" height="398" alt="Screenshot 2026-10-09 105131" src="https://github.com/user-attachments/assets/d927a844-0855-49ce-9065-138e3095b7ce" />
</p>

But we cannot use the linear kalman filter for real-life scenarios so we introduce non-linear kalman filter here.
The non lineaar Kalman fliter has 2 steps in the 1st step the orientation of the object is estimated and in the 2nd stage Kalman filter uses the estimates angles from the 1st step to compute the position of the object.

So how do we get the orientation of an object? It's found using the IMU sensor. IMU means Inertial Measurement Unit consisting of an accelerometer, gyroscope and the magnetometer.

