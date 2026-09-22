from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__)

# A "deque" is just a list with a maximum size -- once it's full, adding a
# new item automatically drops the oldest one. This keeps the last 500
# readings in memory without growing forever.
buffer = deque(maxlen=500)

# We remember the most recent accelerometer AND gyroscope values here,
# because Sensor Logger sends them as SEPARATE entries, not one combined
# reading. Every time either one updates, we save a merged snapshot.
latest = {"t": 0, "ax": 0, "ay": 0, "az": 0, "gx": 0, "gy": 0, "gz": 0}

@app.route("/data", methods=["POST"])
def data():
    try:
        for entry in request.json["payload"]:
            name = entry.get("name")
            v = entry.get("values", {})
            t = entry.get("time", 0) / 1e9  # convert nanoseconds -> seconds

            if name == "accelerometer" and "x" in v:
                latest["t"], latest["ax"], latest["ay"], latest["az"] = t, v["x"], v["y"], v["z"]
                buffer.append(dict(latest))   # save a COPY of the current snapshot
            elif name == "gyroscope" and "x" in v:
                latest["t"], latest["gx"], latest["gy"], latest["gz"] = t, v["x"], v["y"], v["z"]
                buffer.append(dict(latest))
            # any other sensor type (location, battery, etc.) is just skipped
    except Exception as e:
        # Print the problem but DON'T crash the server -- one weird packet
        # from the phone shouldn't take down the whole connection.
        print(f"Skipped a bad packet: {e}")

    return "ok"

# NEW: a second route. When live_plot.py asks for /latest, hand back
# whatever is currently in the buffer, converted to a plain list.
@app.route("/latest")
def get_latest():
    return jsonify(list(buffer))

app.run(host="0.0.0.0", port=8000)