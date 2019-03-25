from .match import Match
from .player import Player
from .team import Team

import sys

class Builder():
    def __init__(self, data, spell_check, playlist_filter):
        self.data = data
        self.spell_check = spell_check
        self.playlist_filter = playlist_filter

        match = Match(data, playlist_filter)
        is_valid_match = match.valid_match_created

        if(is_valid_match):
            self.build_players()
            self.build_teams(match)

    def build_teams(self, match):
        t0 = Team(self.data, match.map, 0, self.spell_check, self.playlist_filter)
        update_player_team_wins(t0.player_ids_dict, t0.name)

        t1 = Team(self.data, match.map, 1, self.spell_check, self.playlist_filter)
        update_player_team_wins(t1.player_ids_dict, t1.name)

        if t0.score > t1.score:
            t0.win = 1
            update_player_wins(t0.player_ids_dict)
        elif t0.score < t1.score:
            t1.win = 1
            update_player_wins(t1.player_ids_dict)

        t0.add_team()
        t1.add_team()

    def build_players(self):
        for player_node in self.data["players"]:
            p = Player(player_node)

            if p.isbot == True:
                print("Engine: Robots are taking over!")
                sys.stdout.flush()
            else:
                p.add_player()

def update_player_team_wins(player_ids_dict, t_name):
    for player_id in player_ids_dict:
        p = Player.get_player_by_id(player_id["id"])
        p.add_team_name(t_name)

def update_player_wins(player_ids_dict):
    for player_id in player_ids_dict:
        p = Player.get_player_by_id(player_id["id"])
        p.add_player_win()
