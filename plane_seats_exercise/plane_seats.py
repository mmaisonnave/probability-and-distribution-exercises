import numpy as np


def plane_seatting_simulation(no_of_passangers: int, default_rng: np.random._generator.Generator):

    seats = set([seat_no for seat_no in range(1,no_of_passangers+1)])

    first_passanger_seat = default_rng.integers(low=1, high=no_of_passangers+1)

    # Sitting first passanger
    seats.remove(first_passanger_seat)


    # Sitting second to no_of_passangers-1 passangers
    for correct_passanger_seat in range(2, no_of_passangers):
        if correct_passanger_seat in seats:
            seats.remove(correct_passanger_seat)

        else:
            random_selected = default_rng.choice(list(seats), size=1)[0]
            seats.remove(random_selected)

    
    # Sitting last passanger
    assert len(seats)==1
    last_available = seats.pop()
    return no_of_passangers == last_available

def main():
    print('hello world!')
    default_rng = np.random.default_rng(seed=1)
    no_of_simulations=10000
    results=[]
    for _ in range(no_of_simulations):
        result = plane_seatting_simulation(
            no_of_passangers=100, 
            default_rng=default_rng)
        results.append(result)
    
    correct = len([_ for result in results if result==True])
    print(f'correct={correct}')
    print(f'Probability of last passanger sitting in their correct seat: {(correct/len(results)):.2%}')


if __name__ == '__main__':
    main()