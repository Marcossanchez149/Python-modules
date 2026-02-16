#!/usr/bin/env python3

class Player():
    def __init__(self, name, score, active, region, achievements):
        self.name = name
        self.score = score
        self.active = active
        self.region = region
        self.achievements = achievements


class AnalyticsDashboard:
    def __init__(self, players: list[Player]):
        self.players = players

    def print_list_analytics(self):
        print("=== List Comprehension Examples ===")
        h_scores = [scores.score for scores in self.players
                    if scores.score > 2000]
        print(f"High scorers (>2000): {h_scores}")
        d_scores = [scores.score * 2 for scores in self.players]
        print(f"Scores doubled: {d_scores}")
        players_active = [player.name for player in players if player.active]
        print(f"Active players: {players_active}")

    def print_dict_analytics(self):
        print("=== Dict Comprehension Examples ===")
        players_and_scores = {i.name: i.score for i in self.players}
        print(f"Player scores: {players_and_scores}")
        score_categoriy = {
            'high': len([p for p in self.players if p.score > 2000]),
            'medium': len([p for p in self.players
                           if 1000 <= p.score <= 2000]),
            'low': len([p for p in self.players if p.score < 1000])
        }
        print(f"Score categories: {score_categoriy}")
        achievement_counts = {i.name: len(i.achievements)
                              for i in self.players}
        print(f"Achievement counts: {achievement_counts}")

    def print_set_analytics(self):
        print("=== Set Comprehension Examples ===")
        unique_players = {i.name for i in self.players}
        print(f"Unique players: {unique_players}")
        unique_achievements = {j for i in self.players for j in i.achievements}
        print(f"Unique achievements: {unique_achievements}")
        active_regions = {i.region for i in self.players}
        print(f"Active regions: {active_regions}")

    def print_combined_analytics(self):
        print("=== Combined Analysis ===")
        total_players = len([i for i in self.players])
        print(f"Total players: {total_players}")
        total_unique_achievements = len({j for i in self.players
                                         for j in i.achievements})
        print(f"Total unique achievements: {total_unique_achievements}")
        average_score = sum([scores.score
                             for scores in self.players])/len(
                                 [i for i in self.players])
        print(f"Average score {average_score}")
        max_score = max([scores.score for scores in self.players])
        top_performer = {"Name": [i.name for i in self.players
                                  if i.score == max_score],
                         "Score": [i.score for i in self.players
                                   if i.score == max_score],
                         "achievements": [len(i.achievements) for i
                                          in self.players
                                          if i.score == max_score]}
        print(f"Top performer: {top_performer}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    player1 = Player("alice", 2300, True,  "north",
                     ['first_kill', 'level_10',
                      'treasure_hunter', 'speed_demon',
                      'treasure_hunter'])
    player2 = Player("bob", 1800, True, "east",
                     ['first_kill', 'level_10', 'boss_slayer'])
    player3 = Player("charlie", 2150, True, "central",
                     ['level_10', 'treasure_hunter',
                      'boss_slayer', 'speed_demon',
                      'perfectionist'])
    player4 = Player("alice", 1000, False,  "north",
                     ['first_kill', 'level_10'])
    players = [player1, player2, player3, player4]
    analytics_dashboard = AnalyticsDashboard(players)
    analytics_dashboard.print_list_analytics()
    analytics_dashboard.print_dict_analytics()
    analytics_dashboard.print_set_analytics()
    analytics_dashboard.print_combined_analytics()
