import os
import sys
import time
from grid import grid

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main(grid_size: int):
    grid_object = grid()
    grid_object.generate_grid(grid_size)
    reveal_flag = False
    corrected_positions = []
    actual_guesses = 0
    count_uncovered_positions = 0

    while True:
        clear()
        print("""--------------------\n|    PEEK-A-BOO    |\n--------------------\n""")

        grid_object.display_grid(corrected_positions, reveal_flag)

        if len(corrected_positions) == grid_size * grid_size and count_uncovered_positions != grid_size * grid_size:
            print("\nOh Happy Day. You've won!! Your score is:", grid_object.calculate_score(grid_size, actual_guesses))
        elif count_uncovered_positions == grid_size * grid_size:
            print("\nYou cheated - Loser!. Your score is 0!")

        print("""\n1. Let me select two elements\n2. Uncover one element for me\n3. I give up - reveal the grid\n4. New game\n5. Exit\n""")
        choice = input("Select: ")

        if choice == '1':
            if len(corrected_positions) == grid_size * grid_size or count_uncovered_positions == grid_size * grid_size or reveal_flag:
                print("Game is over. Press 4 to start a new game or 5 to exit!")
                time.sleep(2)
                continue

            incorrect_coordinate_flag = True
            while incorrect_coordinate_flag:
                coord1 = input("\nEnter cell coordinates (e.g., a0): ")
                converted_coord1 = grid_object.get_coordinates(coord1, grid_size)
                if converted_coord1 is not None:
                    incorrect_coordinate_flag = False

            incorrect_coordinate_flag = True
            while incorrect_coordinate_flag:
                coord2 = input("\nEnter cell coordinates (e.g., a0): ")
                converted_coord2 = grid_object.get_coordinates(coord2, grid_size)
                if converted_coord2 is not None:
                    if converted_coord2 != converted_coord1:
                        incorrect_coordinate_flag = False
                    else:
                        print("Input error: cell coordinate cannot be the same as entered previously. Please try again.")

            corrected_positions.append((converted_coord1))
            corrected_positions.append((converted_coord2))

            clear()
            print("""--------------------\n|    PEEK-A-BOO    |\n--------------------\n""")
            grid_object.display_grid(corrected_positions)
            print("""\n1. Let me select two elements\n2. Uncover one element for me\n3. I give up - reveal the grid\n4. New game\n5. Exit\n\nSelect:""")
            if grid_object.game_grid[converted_coord1[0]][converted_coord1[1]] != grid_object.game_grid[converted_coord2[0]][converted_coord2[1]]:
                time.sleep(2)
                reveal_flag = False
                corrected_positions.remove((converted_coord1))
                corrected_positions.remove((converted_coord2))

            corrected_positions = list(set(corrected_positions))
            actual_guesses += 1

        elif choice == '2':
            if len(corrected_positions) == grid_size * grid_size or count_uncovered_positions == grid_size * grid_size or reveal_flag:
                print("Game is over. Press 4 to start a new game or 5 to exit!")
                time.sleep(2)
                continue

            incorrect_coordinate_flag = True
            while incorrect_coordinate_flag:
                coord1 = input("\nEnter cell coordinates (e.g., a0): ")
                converted_coord1 = grid_object.get_coordinates(coord1, grid_size)
                if converted_coord1 is not None:
                    incorrect_coordinate_flag = False

            if not ((converted_coord1) in corrected_positions):
                corrected_positions.append((converted_coord1))
                count_uncovered_positions += 1

            actual_guesses += 2
            
        elif choice == '3':
            if len(corrected_positions) == grid_size * grid_size or count_uncovered_positions == grid_size * grid_size or reveal_flag:
                print("Game is over. Press 4 to start a new game or 5 to exit!")
                time.sleep(2)
                continue

            reveal_flag = True

        elif choice == '4':
            grid_object.generate_grid(grid_size)
            reveal_flag = False
            corrected_positions = []
            actual_guesses = 0
            count_uncovered_positions = 0

        elif choice == '5':
            clear()
            break

        else:
            print("Invalid choice! Please enter choice again.\n")
            time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and int(sys.argv[1]) in [2, 4, 6]:
        display_main(int(sys.argv[1]))
    else:
        print("Invalid grid size! Only 2, 4 or 6 size grid is allowed. Program Aborted.")