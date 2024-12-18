import numpy as np



def play_one_game(rng):
    
    player_A = rng.integers(low=0, high=2, size=3)
    player_B = rng.integers(low=0, high=2, size=3)

    assert all([coin==0 or coin==1 for coin in player_A])
    assert all([coin==0 or coin==1 for coin in player_B])

    return 'lose' if np.sum(player_A)==np.sum(player_B) else 'win'

def main():
    print('hello world')
    rng = np.random.default_rng()

    repetitions = 300000

    accumulated=0

    for _ in range(repetitions):
        result = play_one_game(rng)
        if result =='win':
            accumulated += 1
        else:
            accumulated -= 2
        
    # Expected winnings = $625
    print(f'Expected winnings: {0.0625*repetitions}')
    print(f'Winnings: {accumulated}')
    

if __name__ == '__main__':
    main()