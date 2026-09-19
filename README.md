# Kalman Filter Implementation for Drone Tracking

### What is Kalman Filter?
It is a model used to observe the system's behaviour over time-dynamic model.It uses two step predict and update to find the state of the system.It is first used in space shuttle trackig.But the question is why do we need it when we have GPS and LiDAR,RADAR.To answer this we should know the drawbacks of GPS such as: noisy measurements, inefficient during intentional jamming, bad weather. So to provide seamless services we integrate GPS and other systems like IMU with kalman filter to reduce noise.

### Drawbacks in IMU and GPS:
IMU contains gyroscope, accelerometer and magnetometer. 
Gyroscope- it drifts over time, this cannot be trusted for long timespan but it's quite precise for short span.
Accelerometer- it doesn't have drift but it's too unstable or we can say noisy during motion.
Magnetometer- it's disturbed by nearby metal.
GPS-it's inefficient during satellite drift,scattering,bad weather or intentional jamming and has noisy sensor measurements.
How to overcome this? We'll integrate Kalman Filter to reduce the sensor noise present in these.We are specially dealing with nonlinear kalman filter which is Extended Kalman Filter as it's more suitable for complex scenarios when compared to linear Kalman filter.

### How do we implement a Kalman Filter:
It has two main steps: prediction and Update.


