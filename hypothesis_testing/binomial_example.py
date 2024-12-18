import numpy as np

import sys
sys.path.append('..')

from utils import io

def binomial_experiment():
    print("Starting binomial experiment...")
    rng = np.random.default_rng(seed=3968225930)
    params = {
        'n':1000,
        'p': 0.5,
        'size': 10000
    }
    print(f'params={params}')
    binomial = rng.binomial(n=params['n'], p=params['p'], size=params['size'])

    io.describe_variable(variable=binomial, name='binomial')



def main():
    print('hello world!')
    binomial_experiment()


if __name__ == '__main__':
    main()