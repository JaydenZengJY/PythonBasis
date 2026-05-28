import matplotlib.pyplot as plt
from robot import Robot


def run_simulation():
    width = 100
    height = 100
    steps = 200

    robot = Robot(
        x=50,
        y=50,
        speed=3,
        direction=35,
        width=width,
        height=height
    )

    for _ in range(steps):
        robot.move()

    path = robot.get_path()

    x_points = []
    y_points = []

    for x, y in path:
        x_points.append(x)
        y_points.append(y)

    plt.figure(figsize=(8, 8))

    plt.plot(x_points, y_points, color="blue", linewidth=2, label="Robot path")

    plt.scatter(x_points[0], y_points[0], color="green", s=100, label="Start")
    plt.scatter(x_points[-1], y_points[-1], color="red", s=100, label="End")

    plt.xlim(0, width)
    plt.ylim(0, height)

    plt.title("Robot Movement Path")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_simulation()