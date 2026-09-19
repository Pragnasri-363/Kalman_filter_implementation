# Kalman Filter Implementation for Drone Tracking

### What is Kalman Filter?
It is a model used to observe the system's behaviour over time-dynamic model.It uses two step predict and update to find the state of the system.It is first used in space shuttle trackig.But the question is why do we need it when we have GPS and LiDAR,RADAR.To answer this we should know the drawbacks of GPS such as: noisy measurements, inefficient during intentional jamming, bad weather. So to provide seamless services we integrate GPS and other systems like IMU with kalman filter to reduce noise.
