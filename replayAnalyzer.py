#!/usr/bin/python3

import sys, argparse, json, os, carball
from os import listdir
from os.path import isfile, join
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
from google.protobuf.json_format import MessageToJson
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from spellchecker import SpellChecker

class Team:
    raw_teams = []

    def __init__(
            self,
            score,
            name,
            win,
        ):
        self.score = score
        self.name = name
        self.win = win
        self.games = 1

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
                Team.raw_teams[matched_index].score = Team.raw_teams[matched_index].score   + t.score
                Team.raw_teams[matched_index].win   = Team.raw_teams[matched_index].win     + t.win
                Team.raw_teams[matched_index].games = Team.raw_teams[matched_index].games   + t.games

class Player:
    raw_players = []

    def __init__(
            self,
            id,
            name,
            goals = 0,
            assists = 0,
            saves = 0,
            shots = 0,
            score = 0,
            boostUseage = 0,
            numSmallBoosts = 0,
            numLargeBoosts = 0,
            wastedCollection = 0,
            wastedUsage = 0,
            timeFullBoost = 0,
            timeLowBoost = 0,
            timeNoBoost = 0,
            numStolenBoosts = 0,
            averageBoostLevel = 0,
            ballHitForward = 0,
            timeClosestToBall = 0,
            timeFurthestFromBall = 0,
            possessionTime = 0,
            turnovers = 0,
            turnoversOnMyHalf = 0,
            turnoversOnTheirHalf = 0,
            wonTurnovers = 0,
            timeOnGround = 0,
            timeLowInAir = 0,
            timeHighInAir = 0,
            timeInDefendingHalf = 0,
            timeInAttackingHalf = 0,
            timeInDefendingThird = 0,
            timeInNeutralThird = 0,
            timeInAttackingThird = 0,
            timeBehindBall = 0,
            timeInFrontBall = 0,
            timeNearWall = 0,
            timeInCorner = 0,
            averageSpeed = 0,
            averageHitDistance = 0,
            averageDistanceFromCenter = 0,
            totalHits = 0,
            totalPasses = 0,
            totalShots = 0,
            totalDribbles = 0,
            totalDribbleConts = 0,
            totalAerials = 0,
            timeAtSlowSpeed = 0,
            timeAtSuperSonic = 0,
            timeAtBoostSpeed = 0
        ):
        self.id = id
        self.name = name
        self.goals = goals
        self.assists = assists
        self.saves = saves
        self.shots = shots
        self.score = score
        self.boostUseage = boostUseage
        self.numSmallBoosts = numSmallBoosts
        self.numLargeBoosts = numLargeBoosts
        self.wastedCollection = wastedCollection
        self.wastedUsage = wastedUsage
        self.timeFullBoost = timeFullBoost
        self.timeLowBoost = timeLowBoost
        self.timeNoBoost = timeNoBoost
        self.numStolenBoosts = numStolenBoosts
        self.averageBoostLevel = averageBoostLevel
        self.ballHitForward = ballHitForward
        self.timeClosestToBall = timeClosestToBall
        self.timeFurthestFromBall = timeFurthestFromBall
        self.possessionTime = possessionTime
        self.turnovers = turnovers
        self.turnoversOnMyHalf = turnoversOnMyHalf
        self.turnoversOnTheirHalf = turnoversOnTheirHalf
        self.wonTurnovers = wonTurnovers
        self.timeOnGround = timeOnGround
        self.timeLowInAir = timeLowInAir
        self.timeHighInAir = timeHighInAir
        self.timeInDefendingHalf = timeInDefendingHalf
        self.timeInAttackingHalf = timeInAttackingHalf
        self.timeInDefendingThird = timeInDefendingThird
        self.timeInNeutralThird = timeInNeutralThird
        self.timeInAttackingThird = timeInAttackingThird
        self.timeBehindBall = timeBehindBall
        self.timeInFrontBall = timeInFrontBall
        self.timeNearWall = timeNearWall
        self.timeInCorner = timeInCorner
        self.averageSpeed = averageSpeed
        self.averageHitDistance = averageHitDistance
        self.averageDistanceFromCenter = averageDistanceFromCenter
        self.totalHits = totalHits
        self.totalPasses = totalPasses
        self.totalShots = totalShots
        self.totalDribbles = totalDribbles
        self.totalDribbleConts = totalDribbleConts
        self.totalAerials = totalAerials
        self.timeAtSlowSpeed = timeAtSlowSpeed
        self.timeAtSuperSonic = timeAtSuperSonic
        self.timeAtBoostSpeed = timeAtBoostSpeed
        self.team_name = ""
        self.games = 1

    def look_for_player_index(player_id):
        index = -100
        for player in Player.raw_players:
            if player.id == player_id:
                index = Player.raw_players.index(player)
                break
        return index

    def add_team_name(team_name, player_id):
        matched_index = Player.look_for_player_index(player_id)
        if(matched_index != -100):
            Player.raw_players[matched_index].team_name = team_name

    def add_player(p):
        if len(Player.raw_players) == 0:
            Player.raw_players.append(p)
        else:
            matched_index = Player.look_for_player_index(p.id)

            if(matched_index == -100):
                Player.raw_players.append(p)
            else:
                # Be sure to scroll right here if your window is less than 140 characters wide (like GitHub)
                # Bad form I guess, but having things lined up is a dream for multi-cursor. Really, game changer.

                Player.raw_players[matched_index].goals                     = Player.raw_players[matched_index].goals                   + p.goals
                Player.raw_players[matched_index].assists                   = Player.raw_players[matched_index].assists                 + p.assists
                Player.raw_players[matched_index].saves                     = Player.raw_players[matched_index].saves                   + p.saves
                Player.raw_players[matched_index].goshotsals                = Player.raw_players[matched_index].shots                   + p.shots
                Player.raw_players[matched_index].score                     = Player.raw_players[matched_index].score                   + p.score
                Player.raw_players[matched_index].games                     = Player.raw_players[matched_index].games                   + p.games
                Player.raw_players[matched_index].boostUseage               = Player.raw_players[matched_index].boostUseage             + p.boostUseage
                Player.raw_players[matched_index].numSmallBoosts            = Player.raw_players[matched_index].numSmallBoosts          + p.numSmallBoosts
                Player.raw_players[matched_index].numLargeBoosts            = Player.raw_players[matched_index].numLargeBoosts          + p.numLargeBoosts
                Player.raw_players[matched_index].wastedCollection          = Player.raw_players[matched_index].wastedCollection        + p.wastedCollection
                Player.raw_players[matched_index].wastedUsage               = Player.raw_players[matched_index].wastedUsage             + p.wastedUsage
                Player.raw_players[matched_index].timeFullBoost             = Player.raw_players[matched_index].timeFullBoost           + p.timeFullBoost
                Player.raw_players[matched_index].timeLowBoost              = Player.raw_players[matched_index].timeLowBoost            + p.timeLowBoost
                Player.raw_players[matched_index].timeNoBoost               = Player.raw_players[matched_index].timeNoBoost             + p.timeNoBoost
                Player.raw_players[matched_index].numStolenBoosts           = Player.raw_players[matched_index].numStolenBoosts         + p.numStolenBoosts
                Player.raw_players[matched_index].averageBoostLevel         = Player.raw_players[matched_index].averageBoostLevel       + p.averageBoostLevel
                Player.raw_players[matched_index].ballHitForward            = Player.raw_players[matched_index].ballHitForward          + p.ballHitForward
                Player.raw_players[matched_index].timeClosestToBall         = Player.raw_players[matched_index].timeClosestToBall       + p.timeClosestToBall
                Player.raw_players[matched_index].timeFurthestFromBall      = Player.raw_players[matched_index].timeFurthestFromBall    + p.timeFurthestFromBall
                Player.raw_players[matched_index].possessionTime            = Player.raw_players[matched_index].possessionTime          + p.possessionTime
                Player.raw_players[matched_index].turnovers                 = Player.raw_players[matched_index].turnovers               + p.turnovers
                Player.raw_players[matched_index].turnoversOnMyHalf         = Player.raw_players[matched_index].turnoversOnMyHalf       + p.turnoversOnMyHalf
                Player.raw_players[matched_index].turnoversOnTheirHalf      = Player.raw_players[matched_index].turnoversOnTheirHalf    + p.turnoversOnTheirHalf
                Player.raw_players[matched_index].wonTurnovers              = Player.raw_players[matched_index].wonTurnovers            + p.wonTurnovers
                Player.raw_players[matched_index].timeOnGround              = Player.raw_players[matched_index].timeOnGround            + p.timeOnGround
                Player.raw_players[matched_index].timeLowInAir              = Player.raw_players[matched_index].timeLowInAir            + p.timeLowInAir
                Player.raw_players[matched_index].timeHighInAir             = Player.raw_players[matched_index].timeHighInAir           + p.timeHighInAir
                Player.raw_players[matched_index].timeInDefendingHalf       = Player.raw_players[matched_index].timeInDefendingHalf     + p.timeInDefendingHalf
                Player.raw_players[matched_index].timeInAttackingHalf       = Player.raw_players[matched_index].timeInAttackingHalf     + p.timeInAttackingHalf
                Player.raw_players[matched_index].timeInDefendingThird      = Player.raw_players[matched_index].timeInDefendingThird    + p.timeInDefendingThird
                Player.raw_players[matched_index].timeInNeutralThird        = Player.raw_players[matched_index].timeInNeutralThird      + p.timeInNeutralThird
                Player.raw_players[matched_index].timeInAttackingThird      = Player.raw_players[matched_index].timeInAttackingThird    + p.timeInAttackingThird
                Player.raw_players[matched_index].timeBehindBall            = Player.raw_players[matched_index].timeBehindBall          + p.timeBehindBall
                Player.raw_players[matched_index].timeInFrontBall           = Player.raw_players[matched_index].timeInFrontBall         + p.timeInFrontBall
                Player.raw_players[matched_index].timeNearWall              = Player.raw_players[matched_index].timeNearWall            + p.timeNearWall
                Player.raw_players[matched_index].timeInCorner              = Player.raw_players[matched_index].timeInCorner            + p.timeInCorner
                Player.raw_players[matched_index].averageSpeed              = Player.raw_players[matched_index].averageSpeed            + p.averageSpeed
                Player.raw_players[matched_index].averageHitDistance        = Player.raw_players[matched_index].averageHitDistance      + p.averageHitDistance
                Player.raw_players[matched_index].averageDistanceFromCenter = Player.raw_players[matched_index].averageDistanceFromCenter + p.averageDistanceFromCenter
                Player.raw_players[matched_index].totalHits                 = Player.raw_players[matched_index].totalHits               + p.totalHits
                Player.raw_players[matched_index].totalPasses               = Player.raw_players[matched_index].totalPasses             + p.totalPasses
                Player.raw_players[matched_index].totalShots                = Player.raw_players[matched_index].totalShots              + p.totalShots
                Player.raw_players[matched_index].totalDribbles             = Player.raw_players[matched_index].totalDribbles           + p.totalDribbles
                Player.raw_players[matched_index].totalDribbleConts         = Player.raw_players[matched_index].totalDribbleConts       + p.totalDribbleConts
                Player.raw_players[matched_index].totalAerials              = Player.raw_players[matched_index].totalAerials            + p.totalAerials
                Player.raw_players[matched_index].timeAtSlowSpeed           = Player.raw_players[matched_index].timeAtSlowSpeed         + p.timeAtSlowSpeed
                Player.raw_players[matched_index].timeAtSuperSonic          = Player.raw_players[matched_index].timeAtSuperSonic        + p.timeAtSuperSonic
                Player.raw_players[matched_index].timeAtBoostSpeed          = Player.raw_players[matched_index].timeAtBoostSpeed        + p.timeAtBoostSpeed

def build_players(data):
    for player in data["players"]:
        # general stats
        p_id = player["id"]["id"]
        p_name = player["name"]
        p_goals = player["goals"]
        p_assists = player["assists"]
        p_saves = player["saves"]
        p_shots = player["shots"]
        p_score = player["score"]
        p_isbot = player["isBot"]

        # Carball wont output a key-value pair for something if its value as 0. At least it appears that way
        # Python will throw a key error if you set something as a node that isnt there
        # So we check for that before assigning the variable.

        if "stats" in player:
            # boost stats
            if "boost" in player["stats"]:
                if "boostUsage" in player["stats"]["boost"]: 
                    p_boostUseage = player["stats"]["boost"]["boostUsage"]
                else:
                    p_boostUseage = 0.00
                if "numSmallBoosts" in player["stats"]["boost"]:
                    p_numSmallBoosts = player["stats"]["boost"]["numSmallBoosts"]
                else:
                    p_numSmallBoosts = 0

                if "numLargeBoosts" in player["stats"]["boost"]:
                    p_numLargeBoosts = player["stats"]["boost"]["numLargeBoosts"]
                else:
                    p_numLargeBoosts = 0 

                if "wastedCollection" in player["stats"]["boost"]:
                    p_wastedCollection = player["stats"]["boost"]["wastedCollection"]
                else:
                    p_wastedCollection = 0.00

                if "wastedUsage" in player["stats"]["boost"]:
                    p_wastedUsage = player["stats"]["boost"]["wastedUsage"]
                else:
                    p_wastedUsage  = 0.00

                if "timeFullBoost" in player["stats"]["boost"]:
                    p_timeFullBoost = player["stats"]["boost"]["timeFullBoost"]
                else:
                    p_timeFullBoost  = 0.00

                if "timeLowBoost" in player["stats"]["boost"]:
                    p_timeLowBoost = player["stats"]["boost"]["timeLowBoost"]
                else:
                    p_timeLowBoost = 0.00

                if "timeNoBoost" in player["stats"]["boost"]:
                    p_timeNoBoost = player["stats"]["boost"]["timeNoBoost"]
                else:
                    p_timeNoBoost = 0.00

                if "numStolenBoosts" in player["stats"]["boost"]:
                    p_numStolenBoosts = player["stats"]["boost"]["numStolenBoosts"]
                else:
                    p_numStolenBoosts = 0

                if "averageBoostLevel" in player["stats"]["boost"]:
                    p_averageBoostLevel = player["stats"]["boost"]["averageBoostLevel"]
                else:
                    p_averageBoostLevel = 0.00

            # distance stats
            if "distance" in player["stats"]:
                if "ballHitForward" in player["stats"]["distance"]:
                    p_ballHitForward = player["stats"]["distance"]["ballHitForward"]
                else:
                    p_ballHitForward  = 0.00

                if "timeClosestToBall" in player["stats"]["distance"]:
                    p_timeClosestToBall = player["stats"]["distance"]["timeClosestToBall"]
                else:
                    p_timeClosestToBall = 0.00

                if "timeFurthestFromBall" in player["stats"]["distance"]:
                    p_timeFurthestFromBall = player["stats"]["distance"]["timeFurthestFromBall"]
                else:
                    p_timeFurthestFromBall = 0.00


            # possession stats
            if "possession" in player["stats"]:
                if "possessionTime" in player["stats"]["possession"]:
                    p_possessionTime = player["stats"]["possession"]["possessionTime"]
                else:
                    p_possessionTime = 0.00

                if "turnovers" in player["stats"]["possession"]:
                    p_turnovers = player["stats"]["possession"]["turnovers"]
                else:
                    p_turnovers = 0

                if "turnoversOnMyHalf" in player["stats"]["possession"]:
                    p_turnoversOnMyHalf = player["stats"]["possession"]["turnoversOnMyHalf"]
                else:
                    p_turnoversOnMyHalf = 0

                if "turnoversOnTheirHalf" in player["stats"]["possession"]:
                    p_turnoversOnTheirHalf = player["stats"]["possession"]["turnoversOnTheirHalf"]
                else:
                    p_turnoversOnTheirHalf = 0

                if "wonTurnovers" in player["stats"]["possession"]:
                    p_wonTurnovers = player["stats"]["possession"]["wonTurnovers"]
                else:
                    p_wonTurnovers = 0

            # positionalTendencies stats
            if "positionalTendencies" in player["stats"]:
                if "timeOnGround" in player["stats"]["positionalTendencies"]:
                    p_timeOnGround = player["stats"]["positionalTendencies"]["timeOnGround"]
                else:
                    p_timeOnGround  = 0.00

                if "timeLowInAir" in player["stats"]["positionalTendencies"]:
                    p_timeLowInAir = player["stats"]["positionalTendencies"]["timeLowInAir"]
                else:
                    p_timeLowInAir  = 0.00

                if "timeHighInAir" in player["stats"]["positionalTendencies"]:
                    p_timeHighInAir = player["stats"]["positionalTendencies"]["timeHighInAir"]
                else:
                    p_timeHighInAir = 0.00

                if "timeInDefendingHalf" in player["stats"]["positionalTendencies"]:
                    p_timeInDefendingHalf = player["stats"]["positionalTendencies"]["timeInDefendingHalf"]
                else:
                    p_timeInDefendingHalf = 0.00

                if "timeInAttackingHalf" in player["stats"]["positionalTendencies"]:
                    p_timeInAttackingHalf = player["stats"]["positionalTendencies"]["timeInAttackingHalf"]
                else:
                    p_timeInAttackingHalf = 0.00

                if "timeInDefendingThird" in player["stats"]["positionalTendencies"]:
                    p_timeInDefendingThird = player["stats"]["positionalTendencies"]["timeInDefendingThird"]
                else:
                    p_timeInDefendingThird = 0.00

                if "timeInNeutralThird" in player["stats"]["positionalTendencies"]:
                    p_timeInNeutralThird = player["stats"]["positionalTendencies"]["timeInNeutralThird"]
                else:
                    p_timeInNeutralThird = 0.00

                if "timeInAttackingThird" in player["stats"]["positionalTendencies"]:
                    p_timeInAttackingThird = player["stats"]["positionalTendencies"]["timeInAttackingThird"]
                else:
                    p_timeInAttackingThird = 0.00

                if "timeBehindBall" in player["stats"]["positionalTendencies"]:
                    p_timeBehindBall = player["stats"]["positionalTendencies"]["timeBehindBall"]
                else:
                    p_timeBehindBall = 0.00

                if "timeInFrontBall" in player["stats"]["positionalTendencies"]:
                    p_timeInFrontBall = player["stats"]["positionalTendencies"]["timeInFrontBall"]
                else:
                    p_timeInFrontBall = 0.00

                if "timeNearWall" in player["stats"]["positionalTendencies"]:
                    p_timeNearWall = player["stats"]["positionalTendencies"]["timeNearWall"]
                else:
                    p_timeNearWall = 0.00

                if "timeInCorner" in player["stats"]["positionalTendencies"]:
                    p_timeInCorner = player["stats"]["positionalTendencies"]["timeInCorner"]
                else:
                    p_timeInCorner = 0.00
                    
            # average stats
            if "averages" in player["stats"]:
                if "averageSpeed" in player["stats"]["averages"]:
                    p_averageSpeed = player["stats"]["averages"]["averageSpeed"]
                else:
                    p_averageSpeed = 0.00
                if "averageHitDistance" in player["stats"]["averages"]:
                    p_averageHitDistance = player["stats"]["averages"]["averageHitDistance"]
                else:
                    p_averageHitDistance = 0.00
                if "averageDistanceFromCenter" in player["stats"]["averages"]:
                    p_averageDistanceFromCenter = player["stats"]["averages"]["averageDistanceFromCenter"]
                else:
                    p_averageDistanceFromCenter = 0.00

            # hit stats
            if "hitCounts" in player["stats"]:
                if "totalHits" in player["stats"]["hitCounts"]:
                    p_totalHits = player["stats"]["hitCounts"]["totalHits"]
                else:
                    p_totalHits = 0
                if "totalPasses" in player["stats"]["hitCounts"]:
                    p_totalPasses = player["stats"]["hitCounts"]["totalPasses"]
                else:
                    p_totalPasses = 0
                if "totalShots" in player["stats"]["hitCounts"]:
                    p_totalShots = player["stats"]["hitCounts"]["totalShots"]
                else:
                    p_totalShots = 0
                if "totalDribbles" in player["stats"]["hitCounts"]:
                    p_totalDribbles = player["stats"]["hitCounts"]["totalDribbles"]
                else:
                    p_totalDribbles = 0
                if "totalDribbleConts" in player["stats"]["hitCounts"]:
                    p_totalDribbleConts = player["stats"]["hitCounts"]["totalDribbleConts"]
                else:
                    p_totalDribbleConts = 0
                if "totalAerials" in player["stats"]["hitCounts"]:
                    p_totalAerials = player["stats"]["hitCounts"]["totalAerials"]
                else:
                    p_totalAerials = 0
            # speed
            if "speed" in player["stats"]:
                if "timeAtSlowSpeed" in player["stats"]["speed"]:
                    p_timeAtSlowSpeed = player["stats"]["speed"]["timeAtSlowSpeed"]
                else:
                    p_timeAtSlowSpeed = 0.00

                if "timeAtSuperSonic" in player["stats"]["speed"]:
                    p_timeAtSuperSonic = player["stats"]["speed"]["timeAtSuperSonic"]
                else:
                    p_timeAtSuperSonic = 0.00
                if "timeAtBoostSpeed" in player["stats"]["speed"]:
                    p_timeAtBoostSpeed = player["stats"]["speed"]["timeAtBoostSpeed"]
                else:
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

def update_player_team(player_ids_dict, t_name):
    for player_id in player_ids_dict:
        Player.add_team_name(t_name, player_id["id"])

def build_teams(data):

    # we know there will always be 2 teams so lets be explicit
    
    # general stats
    t0_player_ids_dict = data["teams"][0]["playerIds"]
    t0_score = data["teams"][0]["score"]
    t0_name= data["teams"][0]["name"]
    t0_win = 0

    update_player_team(t0_player_ids_dict, t0_name)

    t1_player_ids_dict = data["teams"][1]["playerIds"]
    t1_score = data["teams"][1]["score"]
    t1_name= data["teams"][1]["name"]
    t1_win = 0

    update_player_team(t1_player_ids_dict, t1_name)

    if t0_score > t1_score:
        t0_win = 1
    else:
        t1_win = 1

    t0 = Team(
        t0_score,
        t0_name,
        t0_win
    )

    t1 = Team(
        t1_score,
        t1_name,
        t1_win
    )
    Team.add_team(t0)
    Team.add_team(t1)



def get_files(folder_path):
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    return onlyfiles

def parse_files(folder_path):
    for file in get_files(folder_path):
        _json = carball.decompile_replay(folder_path + "/" + file, 
                                        output_path='foo.json', 
                                        overwrite=True)
        game = Game()
        game.initialize(loaded_json=_json)
        analysis = AnalysisManager(game)
        analysis.create_analysis()
        raw_json = MessageToJson(analysis.protobuf_game)
        data = json.loads(raw_json)

        f = open("lastfile.json", "a")
        f.write(raw_json)
        f.close()
        build_players(data)
        build_teams(data)


def write_output_file(filename, data, permissions):
    player_file = open(filename, permissions)
    player_file.write(data)
    player_file.close()


def create_player_output(folder_path):
    player_header_data = ("ID,NAME,TEAM,GOALS,ASSISTS,SAVES,SHOTS,SCORE,GAMES,BOOST USAGE,NUMBER OF SMALL BOOSTS,NUMBER OF LARGE BOOSTS,"
        + "WASTED COLLECTION,WASTED USAGE,TIME FULL BOOST,TIME LOW BOOST,TIME NO BOOST,STOLEN BOOSTS,AVERAGE BOOST LVL,"
        + "BALL HIT FORWARD,T NEAREST BALL,T FURTHEST BALL,POSSESSION T,TURNOVERS,TURNOVERS MY HALF,TURNOVERS THEIR HALF,"
        + "WON TURNOVERS,T ON GROUND,T LOW AIR,T HIGH AIR,T DEFENDING HALF,T ATTACKING HALF,T DEFENDING THIRD,"
        + "T NEUTRAL THIRD,T ATTACKING THIRD,T BEHIND BALL,T FRONT BALL,T NEAR WALL,T CORNER,AVG SPEED,AVG HIT DISTANCE,"
        + "AVG DISTANCE FROM CENTER,TOTAL HITS,TOTAL PASSES,TOTAL SHOTS,TOTAL DRIBBLES,TOTAL DTIBBLE CONTS,TOTAL AERIALS,"
        + "T AT SLOW SPEED,T AT SUPERSONIC,T AT BOOST SPEED\n"
    )

    write_output_file(folder_path + "player_data.csv", player_header_data, "w+")

    for thePlayer in Player.raw_players:
        
        player_data = (str(thePlayer.id)
            + "," + str(thePlayer.name)
            + "," + str(thePlayer.team_name)
            + "," + str(thePlayer.goals)
            + "," + str(thePlayer.assists)
            + "," + str(thePlayer.saves)
            + "," + str(thePlayer.shots)
            + "," + str(thePlayer.score)
            + "," + str(thePlayer.games)
            + "," + str(thePlayer.boostUseage)
            + "," + str(thePlayer.numSmallBoosts)
            + "," + str(thePlayer.numLargeBoosts)
            + "," + str(thePlayer.wastedCollection)
            + "," + str(thePlayer.wastedUsage)
            + "," + str(thePlayer.timeFullBoost)
            + "," + str(thePlayer.timeLowBoost)
            + "," + str(thePlayer.timeNoBoost)
            + "," + str(thePlayer.numStolenBoosts)
            + "," + str(thePlayer.averageBoostLevel)
            + "," + str(thePlayer.ballHitForward)
            + "," + str(thePlayer.timeClosestToBall)
            + "," + str(thePlayer.timeFurthestFromBall)
            + "," + str(thePlayer.possessionTime)
            + "," + str(thePlayer.turnovers)
            + "," + str(thePlayer.turnoversOnMyHalf)
            + "," + str(thePlayer.turnoversOnTheirHalf)
            + "," + str(thePlayer.wonTurnovers)
            + "," + str(thePlayer.timeOnGround)
            + "," + str(thePlayer.timeLowInAir)
            + "," + str(thePlayer.timeHighInAir)
            + "," + str(thePlayer.timeInDefendingHalf)
            + "," + str(thePlayer.timeInAttackingHalf)
            + "," + str(thePlayer.timeInDefendingThird)
            + "," + str(thePlayer.timeInNeutralThird)
            + "," + str(thePlayer.timeInAttackingThird)
            + "," + str(thePlayer.timeBehindBall)
            + "," + str(thePlayer.timeInFrontBall)
            + "," + str(thePlayer.timeNearWall)
            + "," + str(thePlayer.timeInCorner)
            + "," + str(thePlayer.averageSpeed)
            + "," + str(thePlayer.averageHitDistance)
            + "," + str(thePlayer.averageDistanceFromCenter)
            + "," + str(thePlayer.totalHits)
            + "," + str(thePlayer.totalPasses)
            + "," + str(thePlayer.totalShots)
            + "," + str(thePlayer.totalDribbles)
            + "," + str(thePlayer.totalDribbleConts)
            + "," + str(thePlayer.totalAerials)
            + "," + str(thePlayer.timeAtSlowSpeed)
            + "," + str(thePlayer.timeAtSuperSonic)
            + "," + str(thePlayer.timeAtBoostSpeed)
            +"\n"
        )
        write_output_file(folder_path + "player_data.csv", player_data, "a")

def create_team_output(folder_path):
    team_header_data = ("NAME,SCORE,WINS,GAMES\n")

    write_output_file(folder_path + "team_data.csv", team_header_data, "w+")

    for theTeam in Team.raw_teams:
        team_data = (str(theTeam.name)
            + "," + str(theTeam.score)
            + "," + str(theTeam.win)
            + "," + str(theTeam.games)
            +"\n"
        )
        write_output_file(folder_path + "team_data.csv", team_data, "a")

def main():
    # folder_path = ""
    # spell_check = ""
    # arg_parser = argparse.ArgumentParser(description="foo")

    # arg_parser.add_argument("-p", "--folder_path", required=True)
    # arg_parser.add_argument("-s", "--spell_check_enabled", default = "y")
    # # folder_path = arg_parser.parse_args(["--folder_path"])
    # spell_check = arg_parser.parse_args(["--spell_check_enabled"])
    parser = argparse.ArgumentParser()

    # Add more options if you like
    parser.add_argument("-f", "--folder", dest="folder_path",
                        help="please enter --folder pathToFolder", required=True)
                        
    parser.add_argument("-q", "--spell", dest="spell_check",
                        help="enter Y or N for spell check", default="Y")

    args = parser.parse_args()

    parse_files(args.folder_path)
    create_player_output(args.folder_path)
    create_team_output(args.folder_path)

if __name__ == "__main__":
    main()




