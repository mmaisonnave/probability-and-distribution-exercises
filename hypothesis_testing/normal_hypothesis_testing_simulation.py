import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats



def test_null_hypothesis_on_sample(population, variance, rng, sample_size):

    h0_mu = 3

    sample = rng.choice(
        a=population, 
        size=sample_size,
        replace=False
        )

    # print(f'H0: \mu_0 = {h0_mu}')
    # print(f'Ha: \mu_0 > {h0_mu}')
    # print('-------------')

    # print(f'Population mean       = {np.average(sample)}')
    # print(f'Population variance   = {np.var(sample)}')
    # print(f'Standard deviation    = {np.std(sample)}')

    standard_error = np.sqrt(variance)/np.sqrt(sample_size)
    z_statistic = (np.average(sample)-h0_mu)/standard_error
    p_value = 1 - stats.norm.cdf(z_statistic)  


    # print(f'Standard Error (SE)    = {standard_error:4.3f}')
    # print(f'z-statistic            = {z_statistic:4.3f}')
    # print(f'p-value                = {p_value}')
    # print(f"Hypothesis test result = {'Reject' if p_value>0.05 else 'Accept'}")

    return 'Reject' if p_value < 0.05 else 'Accept'


def main():
    print('hello world')
    params = {
        'mean': 4,
        'variance': 9,
        'population_size': 50000
        }

    rng = np.random.default_rng(seed=2582417555)
    
    population = rng.normal(
        loc=params['mean'],
        scale=np.sqrt(params['variance']), # Standard deviation
        size=params['population_size'],
    )

    repetitions_per_sample_size=2000

    for sample_size in [5, 10, 20, 50, 100,]:
        results=[]
        for _ in range(repetitions_per_sample_size):
            result = test_null_hypothesis_on_sample(
                population=population,
                variance=params['variance'],
                rng=rng,
                sample_size=sample_size
            )
            results.append(result)
        accepted_count = len([result for result in results if result=='Accept'])
        print(f'For sample_size={sample_size}, probability of acceptance = {accepted_count/repetitions_per_sample_size:.2%}')

    plt.hist(population, bins=50, edgecolor='black', alpha=0.7)
    plt.title(f'Histogram of N({params["mean"]}, {params["variance"]})')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()





if __name__ == '__main__':
    main() 