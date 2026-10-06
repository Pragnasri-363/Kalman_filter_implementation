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
It has two main steps: prediction and Update.
Step1: We are going to make a prediction of the position of the drone using the mathematical formulae.
Step2: We'll estimate the uncertainity of our estimation to know how much our estimation can be trusted.
Step3: Now we'll take reading from GPS, IMU


