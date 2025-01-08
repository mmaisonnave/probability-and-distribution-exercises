import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    print('hello world')
    
    rng = np.random.default_rng(seed=103101587)

    X = rng.uniform(-10, 10, size=7000).reshape(-1, 1)  # Reshape X for fitting
    Y = 1 + 3 * X.flatten() + rng.normal(loc=0, scale=0.00001, size=7000)


    print(X.shape)
    print(Y.shape)

    model = LinearRegression()
    model.fit(X, Y)
    # Print the coefficients
    print('Y~X')

    print(f'Intercept: {model.intercept_}')
    print(f'Coefficient: {model.coef_[0]}')
    print()

    print('X~Y')
    model = LinearRegression()
    model.fit(Y.reshape(-1, 1), X)  # Reshaping Y to match the expected input format for X
    # Print the coefficients
    print(f'Intercept: {model.intercept_}')
    print(f'Coefficient: {model.coef_[0]}')


if __name__=='__main__':
    main()