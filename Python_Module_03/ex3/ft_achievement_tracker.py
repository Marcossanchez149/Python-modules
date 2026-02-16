#!/usr/bin/env python3

class Player():
    def __init__(self, name, achivements):
        self.name = name
        self.achievements = set(achivements)

    def get_info(self):
        return (f"{self.name} achievements : {self.achievements}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    player1 = Player("Alice", ['first_kill', 'level_10',
                               'treasure_hunter', 'speed_demon',
                               'treasure_hunter'])
    player2 = Player("bob", ['first_kill', 'level_10', 'boss_slayer',
                             'collector'])
    player3 = Player("charlie", ['level_10', 'treasure_hunter',
                                 'boss_slayer', 'speed_demon',
                                 'perfectionist'])
    print(f"Player {player1.get_info()}")
    print(f"Player {player2.get_info()}")
    print(f"Player {player3.get_info()}")
    print("=== Achievement Analytics ===")
    unique_achievements = player1.achievements.union(
        player2.achievements.union(player3.achievements))
    print(f"All unique achievements: {unique_achievements}")
    size = len(unique_achievements)
    print(f"Total unique achievements: {size}")
    common = player1.achievements.intersection(
        player2.achievements.intersection(player3.achievements))
    print(f"Common to all players: {common}")
    player1_to_compare = player2.achievements.union(player3.achievements)
    rare_player1 = player1.achievements.difference(player1_to_compare)

    player2_to_compare = player1.achievements.union(player3.achievements)
    rare_player2 = player2.achievements.difference(player2_to_compare)

    player3_to_compare = player2.achievements.union(player1.achievements)
    rare_player3 = player3.achievements.difference(player3_to_compare)

    rare = rare_player1.union(rare_player2).union(rare_player3)
    print(f"Rare achievements (1 player): {rare}")
    print(f'Alice vs Bob common:'
          f'{player1.achievements.intersection(player2.achievements)}')
    print(f"Alice unique: "
          f"{player1.achievements.difference(player2.achievements)}")
    print(f"Bob unique: "
          f"{player2.achievements.difference(player1.achievements)} ")
