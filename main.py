from collections import defaultdict

from monster import Monster
from Searching_Algorithums.bfs import BFS
from Searching_Algorithums.binary_search import BinarySearch
from Searching_Algorithums.dfs import DFS
from Soring_Algorithums.bubble_sort import BubbleSort
from Soring_Algorithums.merge_sort import MergeSort
from Soring_Algorithums.player import Player
from Soring_Algorithums.quick_sort import QuickSort
from Soring_Algorithums.selection_sort import SelectionSort


def sorting():
    print("\n==== SORTING TYPE ===== ")
    try:
        choice = int(
            input("""
1. Selection Sort
2. Bubble Sort
3. Merge Sort
4. Quick Sort

Enter your choice: """)
        )
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return 0

    print(f"\nChoice {choice}\n")
    if choice == 1:
        sorting_algo = SelectionSort()
    elif choice == 2:
        sorting_algo = BubbleSort()
    elif choice == 3:
        sorting_algo = MergeSort()
    elif choice == 4:
        sorting_algo = QuickSort()
    else:
        print("That's not a valid option.")
        return 0

    players = [
        Player("Arjun", 450),
        Player("Riya", 720),
        Player("Kabir", 310),
        Player("Neha", 890),
        Player("Aman", 560),
    ]

    sorting_algo.sort(players)

    print("Leaderboard:")
    for player in players:
        print(player)

    return players[-1].score


def treasure_scanner():
    print("\n===== TREASURE SCANNER ===== ")
    treasures_id = [105, 118, 129, 145, 167, 189, 205, 221, 250]
    try:
        target = int(input("Enter Treasure ID : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

    searching_algo = BinarySearch()
    index = searching_algo.search(treasures_id, target)

    if index == -1:
        print("Treasure Not Found!")
        return 0
    else:
        print("Treasure Found!")
        print(f"Index : {index}")
        return 100


def shortest_route():
    print("\n===== FASTEST ROUTE ===== ")
    try:
        n = int(input("Enter number of roads: "))
    except ValueError:
        print("That doesn't look like a number.")
        return

    edges = []
    print("Enter the roads (start end):")
    for _ in range(n):
        try:
            u, v = input().split()
            edges.append([u, v])
        except ValueError:
            print("Input format should be: start end")
            return

    src = input("Enter Start : ")
    destination = input("Enter Destination: ")

    path_finder = BFS()
    path, steps = path_finder.shortestPath(edges, src, destination)

    if steps != -1:
        print("\nShortest Route:")
        print(" -> ".join(path))
        print("\nSteps:", steps)
    else:
        print("No Route Found!")


def kingdom_explore():
    print("\n======= KINGDOM EXPLORE ======= ")
    try:
        m = int(input("Enter number of roads: "))
    except ValueError:
        print("You need to enter a valid number.")
        return 0

    graph = defaultdict(list)
    print("Enter the roads (location1 location2):")
    for _ in range(m):
        try:
            u, v = input().split()
            graph[u].append(v)
            graph[v].append(u)
        except ValueError:
            print("Format error. Each road should be two names separated by a space.")
            return 0

    start = input("Enter starting location: ")

    visited = set()
    result = []
    dfs = DFS()

    dfs.explore(graph, start, visited, result)
    print("\nDFS Order:")
    print(" -> ".join(result))

    return 100


def monster_battle():
    print("\n===== MONSTER BATTLE ===== ")
    try:
        n = int(input("Enter number of monsters: "))
    except ValueError:
        print("Please enter a valid number.")
        return 0

    monsters = {}

    for i in range(n):
        print(f"\nMonster {i + 1} Details:")
        name = input("Enter name of Monster : ")
        try:
            health = int(input("Enter Health : "))
            attack = int(input("Enter Attack : "))
            reward = int(input("Enter Reward : "))
        except ValueError:
            print("Health, Attack, and Reward must all be numbers.")
            return 0

        monsters[name] = Monster(name, health, attack, reward)

    choice = input("\nChoose Monster: ")

    if choice not in monsters:
        print("Monster Not Found!")
        return 0
    else:
        monster = monsters[choice]
        battle_score = monster.battle_score()
        print("\nMonster:", monster.name)
        print("Battle Score:", int(battle_score))

    return int(battle_score)


def main():
    leaderboard_score = 0
    treasure_bonus = 0
    battle_score = 0
    exploration_bonus = 0

    while True:
        print("========== MAIN MENU ================== ")
        print("1. Sorting Type (Leaderboard)")
        print("2. Treasure Scanner (Binary Search)")
        print("3. Shortest Route (BFS)")
        print("4. Kingdom Explore (DFS)")
        print("5. Monster Battle")
        print("6. Exit")
        print("============================== ")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Not a valid number. Try again.")
            continue

        if choice == 1:
            leaderboard_score = sorting()
        elif choice == 2:
            treasure_bonus = treasure_scanner()
        elif choice == 3:
            shortest_route()
        elif choice == 4:
            exploration_bonus = kingdom_explore()
        elif choice == 5:
            battle_score = monster_battle()

        elif choice == 6:
            final_score = (
                leaderboard_score + treasure_bonus + battle_score + exploration_bonus
            )

            if final_score <= 299:
                rank = "Novice Explorer"
            elif final_score <= 599:
                rank = "Skilled Adventurer"
            elif final_score <= 999:
                rank = "Master Strategist"
            else:
                rank = "Algorithm Legend"

            print("\n===== GAME RESULT ===== ")
            print(f"Player Score: {leaderboard_score}")
            print(f"Treasure Bonus: {treasure_bonus}")
            print(f"Battle Score: {battle_score}")
            print(f"Exploration Bonus: {exploration_bonus}")
            print(f"\nFinal Score: {final_score}")
            print(f"Rank: {rank.upper()}")

            print("\nPeace Out!")
            break
        else:
            print("Pick a number between 1 and 6.")


if __name__ == "__main__":
    main()
