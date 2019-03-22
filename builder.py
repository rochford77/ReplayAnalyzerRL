from match import Match
from team import Team
from player import Player
from spellchecker import SpellChecker

class Builder():
    def __init__(self, data, spell_check):
        self.data = data
        self.spell_check = spell_check

        is_new_match = self.build_match()

        if(is_new_match):
            self.build_players()
            self.build_teams()


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

    def build_match(self):
        # Meta Data
        match_map = self.data["gameMetadata"]["map"]
        match_time = self.data["gameMetadata"]["time"]

        # Match Data
        playlist = self.data["gameMetadata"]["playlist"]
        match_guid = self.data["gameMetadata"]["matchGuid"]

        match = Match(match_map, match_time, match_guid, playlist)

        if (Match.look_for_match_index(match_guid) == -100):
            Match.add_match(match)
            return True
        else:
            return False
        
    def build_teams(self):

        # Match Data
        match_guid = self.data["gameMetadata"]["matchGuid"]
        match = Match.get_match(match_guid)

        # general stats
        t0_player_ids_dict = self.data["teams"][0]["playerIds"]
        t0_score = self.data["teams"][0]["score"]
        t0_win = 0
        
        # orange blue does not appear to get a node if names are not custom
        try:
            t0_name = self.check_name(self.data["teams"][0]["name"])
        except KeyError:
            t0_name = avoid_default_names(t0_player_ids_dict)

        update_player_team(t0_player_ids_dict, t0_name)

        t1_player_ids_dict = self.data["teams"][1]["playerIds"]
        t1_score = self.data["teams"][1]["score"]
        t1_win = 0

        # orange blue does not appear to get a node if names are not custom
        try:
            t1_name = self.check_name(self.data["teams"][1]["name"])
        except KeyError:
            t1_name = avoid_default_names(t1_player_ids_dict)

        update_player_team(t1_player_ids_dict, t1_name)

        if t0_score > t1_score:
            t0_win = 1
            update_player_wins(t0_player_ids_dict)
        elif t0_score < t1_score:
            t1_win = 1
            update_player_wins(t1_player_ids_dict)

        t0 = Team(t0_score, t0_name, t0_win, match.map)
        t1 = Team(t1_score, t1_name, t1_win, match.map)

        Team.add_team(t0)
        Team.add_team(t1)

    def build_players(self):

        for player in self.data["players"]:

            # general stats
            p_id = player["id"]["id"]
            p_name = player["name"]

            # (Verified by guys at SaltieRL/Claculated.gg/makers of carball)
            # Carball wont output a key-value pair for something if its value as 0.
            # Python will throw a key error if you set something as a node that isnt there
            # Must handle the errors

            # Primary stats
            try:
                p_isbot = player["isBot"]
            except KeyError:
                p_isbot = False

            try:
                p_goals = player["goals"]
            except KeyError:
                p_goals = 0

            try:
                p_assists = player["assists"]
            except KeyError:
                p_assists = 0

            try:
                p_saves = player["saves"]
            except KeyError:
                p_saves = 0

            try:
                p_shots = player["shots"]
            except KeyError:
                p_shots = 0

            try:
                p_score = player["score"]
            except KeyError:
                p_score = 0

            # Boost Stats
            try:
                p_boostUseage = player["stats"]["boost"]["boostUsage"]
            except KeyError:
                p_boostUseage = 0.00

            try:
                p_numSmallBoosts = player["stats"]["boost"]["numSmallBoosts"]
            except KeyError:
                p_numSmallBoosts = 0

            try:
                p_numLargeBoosts = player["stats"]["boost"]["numLargeBoosts"]
            except KeyError:
                p_numLargeBoosts = 0 

            try:
                p_wastedCollection = player["stats"]["boost"]["wastedCollection"]
            except KeyError:
                p_wastedCollection = 0.00

            try:
                p_wastedUsage = player["stats"]["boost"]["wastedUsage"]
            except KeyError:
                p_wastedUsage  = 0.00

            try:
                p_timeFullBoost = player["stats"]["boost"]["timeFullBoost"]
            except KeyError:
                p_timeFullBoost  = 0.00

            try:
                p_timeLowBoost = player["stats"]["boost"]["timeLowBoost"]
            except KeyError:
                p_timeLowBoost = 0.00

            try:
                p_timeNoBoost = player["stats"]["boost"]["timeNoBoost"]
            except KeyError:
                p_timeNoBoost = 0.00

            try:
                p_numStolenBoosts = player["stats"]["boost"]["numStolenBoosts"]
            except KeyError:
                p_numStolenBoosts = 0

            try:
                p_averageBoostLevel = player["stats"]["boost"]["averageBoostLevel"]
            except KeyError:
                p_averageBoostLevel = 0.00

            # Distance Stats
            try:
                p_ballHitForward = player["stats"]["distance"]["ballHitForward"]
            except KeyError:
                p_ballHitForward  = 0.00

            try:
                p_timeClosestToBall = player["stats"]["distance"]["timeClosestToBall"]
            except KeyError:
                p_timeClosestToBall = 0.00

            try:
                p_timeFurthestFromBall = player["stats"]["distance"]["timeFurthestFromBall"]
            except KeyError:
                p_timeFurthestFromBall = 0.00

            # Possession Stats
            try:
                p_possessionTime = player["stats"]["possession"]["possessionTime"]
            except KeyError:
                p_possessionTime = 0.00

            try:
                p_turnovers = player["stats"]["possession"]["turnovers"]
            except KeyError:
                p_turnovers = 0

            try:
                p_turnoversOnMyHalf = player["stats"]["possession"]["turnoversOnMyHalf"]
            except KeyError:
                p_turnoversOnMyHalf = 0

            try:
                p_turnoversOnTheirHalf = player["stats"]["possession"]["turnoversOnTheirHalf"]
            except KeyError:
                p_turnoversOnTheirHalf = 0

            try:
                p_wonTurnovers = player["stats"]["possession"]["wonTurnovers"]
            except KeyError:
                p_wonTurnovers = 0

            # Positional Stats
            try:
                p_timeOnGround = player["stats"]["positionalTendencies"]["timeOnGround"]
            except KeyError:
                p_timeOnGround  = 0.00

            try:
                p_timeLowInAir = player["stats"]["positionalTendencies"]["timeLowInAir"]
            except KeyError:
                p_timeLowInAir  = 0.00

            try:
                p_timeHighInAir = player["stats"]["positionalTendencies"]["timeHighInAir"]
            except KeyError:
                p_timeHighInAir = 0.00

            try:
                p_timeInDefendingHalf = player["stats"]["positionalTendencies"]["timeInDefendingHalf"]
            except KeyError:
                p_timeInDefendingHalf = 0.00

            try:
                p_timeInAttackingHalf = player["stats"]["positionalTendencies"]["timeInAttackingHalf"]
            except KeyError:
                p_timeInAttackingHalf = 0.00

            try:
                p_timeInDefendingThird = player["stats"]["positionalTendencies"]["timeInDefendingThird"]
            except KeyError:
                p_timeInDefendingThird = 0.00

            try:
                p_timeInNeutralThird = player["stats"]["positionalTendencies"]["timeInNeutralThird"]
            except KeyError:
                p_timeInNeutralThird = 0.00

            try:
                p_timeInAttackingThird = player["stats"]["positionalTendencies"]["timeInAttackingThird"]
            except KeyError:
                p_timeInAttackingThird = 0.00

            try:
                p_timeBehindBall = player["stats"]["positionalTendencies"]["timeBehindBall"]
            except KeyError:
                p_timeBehindBall = 0.00

            try:
                p_timeInFrontBall = player["stats"]["positionalTendencies"]["timeInFrontBall"]
            except KeyError:
                p_timeInFrontBall = 0.00

            try:
                p_timeNearWall = player["stats"]["positionalTendencies"]["timeNearWall"]
            except KeyError:
                p_timeNearWall = 0.00

            try:
                p_timeInCorner = player["stats"]["positionalTendencies"]["timeInCorner"]
            except KeyError:
                p_timeInCorner = 0.00

            # average stats
            try:
                p_averageSpeed = player["stats"]["averages"]["averageSpeed"]
            except KeyError:
                p_averageSpeed = 0.00
            try:
                p_averageHitDistance = player["stats"]["averages"]["averageHitDistance"]
            except KeyError:
                p_averageHitDistance = 0.00
            try:
                p_averageDistanceFromCenter = player["stats"]["averages"]["averageDistanceFromCenter"]
            except KeyError:
                p_averageDistanceFromCenter = 0.00

            # hit stats
            try:
                p_totalHits = player["stats"]["hitCounts"]["totalHits"]
            except KeyError:
                p_totalHits = 0
            try:
                p_totalPasses = player["stats"]["hitCounts"]["totalPasses"]
            except KeyError:
                p_totalPasses = 0
            try:
                p_totalShots = player["stats"]["hitCounts"]["totalShots"]
            except KeyError:
                p_totalShots = 0
            try:
                p_totalDribbles = player["stats"]["hitCounts"]["totalDribbles"]
            except KeyError:
                p_totalDribbles = 0
            try:
                p_totalDribbleConts = player["stats"]["hitCounts"]["totalDribbleConts"]
            except KeyError:
                p_totalDribbleConts = 0
            try:
                p_totalAerials = player["stats"]["hitCounts"]["totalAerials"]
            except KeyError:
                p_totalAerials = 0

            # speed
            try:
                p_timeAtSlowSpeed = player["stats"]["speed"]["timeAtSlowSpeed"]
            except KeyError:
                p_timeAtSlowSpeed = 0.00

            try:
                p_timeAtSuperSonic = player["stats"]["speed"]["timeAtSuperSonic"]
            except KeyError:
                p_timeAtSuperSonic = 0.00
            try:
                p_timeAtBoostSpeed = player["stats"]["speed"]["timeAtBoostSpeed"]
            except KeyError:
                p_timeAtBoostSpeed = 0.00

            if p_isbot == True:
                print("Robots are taking over!")
            else:
                p = Player(
                    p_id,
                    p_name,
                    p_goals,
                    p_assists,
                    p_saves,
                    p_shots,
                    p_score,
                    p_boostUseage,
                    p_numSmallBoosts,
                    p_numLargeBoosts,
                    p_wastedCollection,
                    p_wastedUsage,
                    p_timeFullBoost,
                    p_timeLowBoost,
                    p_timeNoBoost,
                    p_numStolenBoosts,
                    p_averageBoostLevel,
                    p_ballHitForward,
                    p_timeClosestToBall,
                    p_timeFurthestFromBall,
                    p_possessionTime,
                    p_turnovers,
                    p_turnoversOnMyHalf,
                    p_turnoversOnTheirHalf,
                    p_wonTurnovers,
                    p_timeOnGround,
                    p_timeLowInAir,
                    p_timeHighInAir,
                    p_timeInDefendingHalf,
                    p_timeInAttackingHalf,
                    p_timeInDefendingThird,
                    p_timeInNeutralThird,
                    p_timeInAttackingThird,
                    p_timeBehindBall,
                    p_timeInFrontBall,
                    p_timeNearWall,
                    p_timeInCorner,
                    p_averageSpeed,
                    p_averageHitDistance,
                    p_averageDistanceFromCenter,
                    p_totalHits,
                    p_totalPasses,
                    p_totalShots,
                    p_totalDribbles,
                    p_totalDribbleConts,
                    p_totalAerials,
                    p_timeAtSlowSpeed,
                    p_timeAtSuperSonic,
                    p_timeAtBoostSpeed
                )

                Player.add_player(p)


def avoid_default_names(player_ids_dict):
    team_name = ""
    playerarr = []
    for player_id in player_ids_dict:
        playerarr.append(Player.get_player_name_by_id(player_id["id"]))
    playerarr.sort()
    team_name = "_".join(playerarr)

    return team_name

def update_player_team(player_ids_dict, t_name):
    for player_id in player_ids_dict:
        Player.add_team_name(t_name, player_id["id"])

def update_player_wins(player_ids_dict):
    for player_id in player_ids_dict:
        Player.add_player_win(player_id["id"])