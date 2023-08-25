import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot(results):
    # Extracted for simplicity from the results you provided
    inside_temps = [entry["inside_temp"] for entry in results]
    outside_temps = [entry["outside_temp"] for entry in results]
    is_heating = [entry["heating"] for entry in results]
    is_cooling = [entry["cooling"] for entry in results]
    timestamps = [entry["timestamp"] for entry in results]

    # Set up the figure and axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Ax1 settings for temperature visualization
    ax1.set_xlim(0, 12)
    ax1.set_ylim(0, 12)
    ax1.set_xticks([])
    ax1.set_yticks([])
    greenhouse_patch = plt.Rectangle((2, 2), 8, 8, color="grey")
    ax1.add_patch(greenhouse_patch)
    time_label = ax1.text(6, 11, "", ha="center")

    # Ax2 settings for temperature curves
    ax2.set_xlim(0, len(inside_temps))
    ax2.set_ylim(
        min(min(inside_temps), min(outside_temps)) - 5,
        max(max(inside_temps), max(outside_temps)) + 5,
    )
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Temperature (°F)")

    # Initial plots for the temperature curves
    (line1,) = ax2.plot([], [], "g", label="Inside Temp")
    (line2,) = ax2.plot([], [], "b", label="Outside Temp")
    ax2.legend(loc="upper right")

    def animate(i):
        # update greenhouse color based on inside temperature
        greenhouse_temp = inside_temps[i]
        greenhouse_patch.set_facecolor(
            (1, 1 - greenhouse_temp / 100, 1 - greenhouse_temp / 100)
        )

        # update background color based on outside temperature
        outside_temp = outside_temps[i]
        ax1.set_facecolor((1, 1 - outside_temp / 100, 1 - outside_temp / 100))

        # Update the temperature curves
        line1.set_data(range(i + 1), inside_temps[: i + 1])
        line2.set_data(range(i + 1), outside_temps[: i + 1])

        # Add a red star marker when heating
        if is_heating[i]:
            ax2.plot(i, inside_temps[i], "r*")

        elif is_cooling[i]:
            ax2.plot(i, inside_temps[i], "b+")

        # update time label
        time_label.set_text(timestamps[i])

        time.sleep(1)

    ani = FuncAnimation(fig, animate, frames=len(inside_temps))

    plt.tight_layout()
    plt.show()
