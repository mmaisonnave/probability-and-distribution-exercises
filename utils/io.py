import numpy as np

def describe_variable(variable, name):
    print(f'{name}:')
    print(f'mean=     {np.average(variable):3.2f}')
    print(f'variable= {np.var(variable):3.2f}')
    print()