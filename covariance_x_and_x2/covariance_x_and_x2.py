import matplotlib.pyplot as plt
import numpy as np

def plot_histograms(X, Y):
    plt.figure(figsize=(12, 6))

    # Plot histogram for X
    plt.subplot(1, 2, 1)
    plt.hist(X, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Distribution of X", fontsize=14)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)

    # Plot histogram for Y
    plt.subplot(1, 2, 2)
    plt.hist(Y, bins=50, color='salmon', edgecolor='black', alpha=0.7)
    plt.title("Distribution of Y", fontsize=14)
    plt.xlabel("Y", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)

    # Adjust layout
    plt.tight_layout()
    plt.show()

def main():
    print('hello world')

    rng = np.random.default_rng(seed=2124338382)
    X = rng.uniform(low=-1, high=1, size=7000)
    Y = X**2

    plot_histograms(X,Y)


if __name__ == '__main__':
    main()