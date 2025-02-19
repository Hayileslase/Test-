import numpy as np
import matplotlib.pyplot as plt

# Lengder på leddene
l1 = 1.0  # Lengde på første lenke
l2 = 1.0  # Lengde på andre lenke
l3 = 0.5  # Lengde på tredje lenke

def inverse_kinematics(x, y):
    """
    Beregner invers kinematikk for en 3DOF robotarm
    """
    # Beregn theta3 ved hjelp av cosinusloven
    c3 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    if np.abs(c3) > 1:
        raise ValueError("Posisjon utenfor rekkevidde")
    theta3 = np.arccos(c3)

    # Beregn theta2
    k1 = l1 + l2 * np.cos(theta3)
    k2 = l2 * np.sin(theta3)
    theta2 = np.arctan2(y, x) - np.arctan2(k2, k1)

    # Beregn theta1
    theta1 = np.arctan2(y, x) - theta2

    return np.degrees(theta1), np.degrees(theta2), np.degrees(theta3)

def plot_robot(theta1, theta2, theta3):
    """
    Plotter robotarmen basert på vinkler
    """
    # Konverter til radianer
    theta1 = np.radians(theta1)
    theta2 = np.radians(theta2)
    theta3 = np.radians(theta3)

    # Beregn leddposisjoner
    x0, y0 = 0, 0
    x1, y1 = l1 * np.cos(theta1), l1 * np.sin(theta1)
    x2, y2 = x1 + l2 * np.cos(theta1 + theta2), y1 + l2 * np.sin(theta1 + theta2)
    x3, y3 = x2 + l3 * np.cos(theta1 + theta2 + theta3), y2 + l3 * np.sin(theta1 + theta2 + theta3)

    # Plott robotarmen
    plt.figure(figsize=(5,5))
    plt.plot([x0, x1], [y0, y1], 'ro-', lw=5, label="Ledd 1")
    plt.plot([x1, x2], [y1, y2], 'go-', lw=5, label="Ledd 2")
    plt.plot([x2, x3], [y2, y3], 'bo-', lw=5, label="Ledd 3")
    plt.scatter([x0, x1, x2, x3], [y0, y1, y2, y3], color='black', s=100)  # Leddposisjoner
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid()
    plt.legend()
    plt.title("3-DOF Robotarm")
    plt.show()

# Test invers kinematikk og plotting
try:
    x_target, y_target = 1.0, 1.0  # Ønsket posisjon
    theta1, theta2, theta3 = inverse_kinematics(x_target, y_target)
    print(f"Theta1: {theta1:.2f}, Theta2: {theta2:.2f}, Theta3: {theta3:.2f}")
    plot_robot(theta1, theta2, theta3)
except ValueError as e:
    print(e)



hejejn
bjnjde
knedke

