import numpy as np
import matplotlib.pyplot as plt


def main():
    print('hello world!')
    rng = np.random.default_rng()
    X = rng.uniform(low=0, high=1, size=7000)
    Y = rng.uniform(low=0, high=1, size=7000)
    Z = X+Y

    fig, ax = plt.subplots(3, figsize=(4, 8))  # Adjust figure size for better visualization

    ax[0].hist(X, bins=50, color='blue', edgecolor='black')
    ax[0].set_title('Histogram of X')
    ax[1].hist(Y, bins=50, color='green', edgecolor='black')
    ax[1].set_title('Histogram of Y')
    ax[2].hist(Z, bins=50, color='orange', edgecolor='black')
    ax[2].set_title('Histogram of Z')

    plt.tight_layout()  # Adjust spacing to avoid overlap
    plt.show()          # Use plt.show() to render the plots



if __name__ == '__main__':
    main()
