#!/usr/bin/python3

import argparse
import json
import os
import sys
from os import listdir
from os.path import isfile, join

import carball
from carball.analysis.analysis_manager import AnalysisManager
from carball.json_parser.game import Game
from google.protobuf import message as _message
from google.protobuf.json_format import MessageToJson
from spellchecker import SpellChecker

from classes.builder import Builder
from classes.match import Match
from classes.outputHandler import OutputHandler
from classes.player import Player
from classes.team import Team


def get_files(abs_path):
    onlyfiles = [f for f in listdir(abs_path) if isfile(join(abs_path, f))]
    return onlyfiles

def parse_files(abs_path, spell_check, playlist_filter, single_player):

    temp_output_dir = abs_path + "/TempJSON/"
    replay_dir = abs_path
    print("Engine: verifying temp directory")
    sys.stdout.flush()
    print("Engine: parsing folder: " + replay_dir)
    for file in get_files(replay_dir):
        print("Engine: Analyzing replay: " + file)
        sys.stdout.flush()
        _json = carball.decompile_replay(replay_dir + "/" + file, 
                                        output_path=temp_output_dir +'foo.json', 
                                        overwrite=True)
        game = Game()
        game.initialize(loaded_json=_json)
        analysis = AnalysisManager(game)
        analysis.create_analysis()
        raw_json = MessageToJson(analysis.protobuf_game)
        data = json.loads(raw_json)

        f = open(temp_output_dir + "lastfile.json", "w+")
        f.write(raw_json)
        f.close()
        print("Engine: sending data from " + file +" to Builder")
        sys.stdout.flush()
        Builder(data, spell_check, playlist_filter, single_player)

def verify_temp_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    print("Engine Connected")
    sys.stdout.flush()
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--abspath", dest="abs_path",
                                help="please enter --folder pathToFolder", required=True)

    parser.add_argument("-s", "--spell", dest="spell_check",
                                help="enter Y or N for spell check", default="Y")

    parser.add_argument("-l", "--playlist", dest="playlist_filter",
        help="enter the name of the playlist to filter for", default = None)
    
    parser.add_argument("-m", "--mode", dest="is_single_player_mode",
        help="enter True for single player mode or leave blank or False for team mode", default = False)

    args = parser.parse_args()
    is_single_player = False

    if (args.is_single_player_mode == "true" or args.is_single_player_mode == True):
        is_single_player = True

    print("Engine: Parsing Replay Files")
    sys.stdout.flush()
    parse_files(args.abs_path, args.spell_check, args.playlist_filter, is_single_player)
    print("Engine: Creating Output")
    sys.stdout.flush()
    OutputHandler(args.abs_path)
    print("Engine: Batch Job Finished")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
