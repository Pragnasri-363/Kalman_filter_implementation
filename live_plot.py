import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Two charts stacked on top of each other, sharing the same x-axis (time)
fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

def update(frame):
    # Ask our imu_data.py server for whatever readings it has right now.
    # Wrapped in try/except so ONE bad response doesn't kill the whole plot.
    try:
        response = requests.get("http://localhost:8000/latest", timeout=1)
        readings = response.json()
    except Exception as e:
        print(f"Could not get data from server: {e}")
        print("  -> Is imu_data.py still running in its own terminal?")
        return

    if len(readings) == 0:
        return  # nothing to plot yet

    # Pull out each column into its own list
    t = [r["t"] for r in readings]
    t0 = t[0]
    t = [x - t0 for x in t]  # start the time axis at 0 instead of a huge number

    ax_ = [r["ax"] for r in readings]
    ay_ = [r["ay"] for r in readings]
    az_ = [r["az"] for r in readings]
    gx_ = [r["gx"] for r in readings]
    gy_ = [r["gy"] for r in readings]
    gz_ = [r["gz"] for r in readings]

    # Clear the old lines and redraw fresh ones
    ax_top.clear()
    ax_top.plot(t, ax_, label="x")
    ax_top.plot(t, ay_, label="y")
    ax_top.plot(t, az_, label="z")
    ax_top.set_title("Accelerometer (m/s^2)")
    ax_top.legend()
    ax_top.grid(True, alpha=0.3)

    ax_bottom.clear()
    ax_bottom.plot(t, gx_, label="x")
    ax_bottom.plot(t, gy_, label="y")
    ax_bottom.plot(t, gz_, label="z")
    ax_bottom.set_title("Gyroscope (deg/s)")
    ax_bottom.set_xlabel("Time (s)")
    ax_bottom.legend()
    ax_bottom.grid(True, alpha=0.3)

# This is the key line: call update() every 200 milliseconds, forever,
# which is what makes the plot window "live" instead of a single static image.
ani = animation.FuncAnimation(fig, update, interval=200, cache_frame_data=False)

plt.tight_layout()
plt.show()