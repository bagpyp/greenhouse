import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot(results):
    # Extracted for simplicity from the results you provided
    inside_temps = [entry["inside_temp"] for entry in results]
    outside_temps = [entry["outside_temp"] for entry in results]
    timestamps = [entry["timestamp"] for entry in results]

    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add text label for time
    time_label = ax.text(6, 11, "", ha="center")

    # Draw greenhouse
    greenhouse_patch = plt.Rectangle((2, 2), 8, 8, color="grey")
    ax.add_patch(greenhouse_patch)

    def animate(i):
        # Update greenhouse color based on inside temperature
        greenhouse_temp = inside_temps[i]
        greenhouse_patch.set_facecolor(
            (1, 1 - greenhouse_temp / 100, 1 - greenhouse_temp / 100)
        )

        # Update background color of the plot based on outside temperature
        outside_temp = outside_temps[i]
        ax.set_facecolor((1, 1 - outside_temp / 100, 1 - outside_temp / 100))

        # Update time label
        time_label.set_text(timestamps[i])

    ani = FuncAnimation(fig, animate, frames=len(inside_temps), repeat=True)

    plt.show()
