from env import create_standard_grid

def main():

    gw = create_standard_grid()
    policy = {
        (0, 0): 'up', (0, 1): 'right', (0, 2): 'left', (0, 3): 'up',
        (1, 0): 'up', (1, 1): '', (1, 2): 'right', (1, 3): '',
        (2, 0): 'right', (2, 1): 'right', (2, 2): 'right', (2, 3): ''
    }

    gw.print_values()
    gw.print_policy(policy)

if __name__ == "__main__":
    main()
