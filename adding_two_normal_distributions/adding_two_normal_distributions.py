import numpy as np
import matplotlib.pyplot as plt

def describe_variable(var, name):
    print(f'{name}:')
    print(f'mean={np.average(var):3.2f}')
    print(f'var= {np.var(var):3.2f}')
    print()

def main():
    print('hello world!')

    rng = np.random.default_rng(seed=1234)

    # Variables defined in the problem statement as: X~N(1,9) & Y~N(9,16)
    X = rng.normal(loc=1, scale=3, size=15000)
    Y = rng.normal(loc=9, scale=4, size=15000)

    describe_variable(var=X, name='X')
    describe_variable(var=Y, name='Y')

    Z = X+Y
    # VAR(Z) = VAR(X+Y) = VAR(X) + VAR(Y) = 16 + 9 = 25
    #  E(Z)  =  E(X+Y)  =  E(X)  +   E(Y) = 9 + 1  = 10
    describe_variable(var=Z, name='Z')

    # Plot X, Y, and Z distributions in subplots
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # X Distribution
    axes[0].hist(X, bins=50, color='skyblue', alpha=0.7, edgecolor='black')
    axes[0].set_title('X ~ N(1, 9)')
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Frequency')

    # Y Distribution
    axes[1].hist(Y, bins=50, color='lightgreen', alpha=0.7, edgecolor='black')
    axes[1].set_title('Y ~ N(9, 16)')
    axes[1].set_xlabel('Value')
    axes[1].set_ylabel('Frequency')

    # Z Distribution
    axes[2].hist(Z, bins=50, color='salmon', alpha=0.7, edgecolor='black')
    axes[2].set_title('Z = X + Y')
    axes[2].set_xlabel('Value')
    axes[2].set_ylabel('Frequency')

    plt.show()

if __name__ == '__main__':
    main()