from spellchecker import SpellChecker
from player import Player
class Team:
    raw_teams = []

    def __init__(self, data, game_map, team_index, spell_check, playlist_filter):
        self.maps_played = [game_map]
        self.spell_check = spell_check
        self.playlist_filter = playlist_filter
        self.games = 1
        self.win = 0
        self.team_node = data["teams"][team_index]

        self.score = self.team_node["score"]
        self.player_ids_dict = self.team_node["playerIds"]

        # orange blue does not appear to get a node if names are not custom
        try:
            self.name = self.check_name(self.team_node["name"])
        except KeyError:
            self.name = self.get_non_default_name()
 
    def check_name(self, t_name):
        # credit goes to Jordak for the idea <3
        verified_name = ""

        if(self.spell_check == 'N'):
            verified_name = t_name
        else:
            spell = SpellChecker()
            spell.word_frequency.load_text_file('./TeamNameSpellCheckerCustomLanguage.txt')
            namearr = t_name.split()
            misspelled = spell.unknown(namearr)
            corrections = {}

            for word in misspelled:
                correct = spell.correction(word)
                corrections[word] = correct

            for index, this_word in enumerate(namearr):
                if this_word in corrections.keys():
                    namearr[index] = corrections[this_word]

            verified_name = " ".join(namearr)
        return verified_name

    def get_non_default_name(self):
        team_name = ""
        playerarr = []
        for player_id in self.player_ids_dict:
            p = Player.get_player_by_id(player_id["id"])
            playerarr.append(p.name)
        playerarr.sort()
        team_name = "_".join(playerarr)

        return team_name

    def look_for_team_index(team_name):
        index = -100
        for team in Team.raw_teams:
            if team.name == team_name:
                index = Team.raw_teams.index(team)
                break
        return index


    def add_team(t):
        if len(Team.raw_teams) == 0:
            Team.raw_teams.append(t)
        else:
            matched_index = Team.look_for_team_index(t.name)

            if (matched_index == -100):
                Team.raw_teams.append(t)
            else:
                Team.raw_teams[matched_index].score         = Team.raw_teams[matched_index].score       + t.score
                Team.raw_teams[matched_index].win           = Team.raw_teams[matched_index].win         + t.win
                Team.raw_teams[matched_index].games         = Team.raw_teams[matched_index].games       + t.games
                Team.raw_teams[matched_index].maps_played   = list(set(Team.raw_teams[matched_index].maps_played + t.maps_played))