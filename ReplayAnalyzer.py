#!/usr/bin/python3

import carball
import os
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
import json



class Player:
    raw_players = []

    def __init__(self, id, name, goals = 0, assists = 0, saves = 0, shots = 0, score = 0):
        self.id = id
        self.name = name
        self.goals = goals
        self.assists = assists
        self.saves = saves
        self.shots = shots
        self.score = score

    def look_for_player_index(p):
        index = -100
        for player in Player.raw_players:
            print("does " + player.id + " = " + p.id + "?")
            if player.id == p.id:
                print("YES!")
                index = Player.raw_players.index(player)
            else:
                print("no!")
        return index

    def add_player(p):
        if len(Player.raw_players) == 0:
            print("The list is empty, adding player")
            print(p.id)
            print(p.name)
            Player.raw_players.append(p)
        else:
            print("there are players in the list, checking for doubles")
            print("searching for player: " + p.name)
            
            matched_index = Player.look_for_player_index(p)

            if(matched_index == -100):
                print("________________________________________ no match | appending ______________________________________")
                Player.raw_players.append(p)
            else:
                print("________________________________________ found match | updating ______________________________________")
                Player.raw_players[matched_index].goals        = Player.raw_players[matched_index].goals + p.goals
                Player.raw_players[matched_index].assists      = Player.raw_players[matched_index].assists + p.assists
                Player.raw_players[matched_index].saves        = Player.raw_players[matched_index].saves + p.saves
                Player.raw_players[matched_index].goshotsals   = Player.raw_players[matched_index].shots + p.shots
                Player.raw_players[matched_index].score        = Player.raw_players[matched_index].score + p.score


def build_players(data):
    for player in data["players"]:
        p_id = player["id"]["id"]
        p_name = player["name"]
        p_goals = player["goals"]
        p_assists = player["assists"]
        p_saves = player["saves"]
        p_shots = player["shots"]
        p_score = player["score"]

        p = Player(p_id, p_name, p_goals, p_assists, p_saves, p_shots, p_score)
        Player.add_player(p)

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
        data = json.loads(MessageToJson(analysis.protobuf_game))
        build_players(data)


def start():
    folder_path = "w12y2019"
    parse_files(folder_path)

    for thePlayer in Player.raw_players:
        print(
            "id: " + str(thePlayer.id)
            + " name: " + str(thePlayer.name)
            + " goals: " + str(thePlayer.goals)
        )
start()




