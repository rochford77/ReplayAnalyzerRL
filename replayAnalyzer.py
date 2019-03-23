#!/usr/bin/python3

import sys, argparse, json, os, carball
from os import listdir
from os.path import isfile, join
from google.protobuf import message as _message
from google.protobuf.json_format import MessageToJson
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from spellchecker import SpellChecker
from player import Player
from match import Match
from team import Team
from outputHandler import OutputHandler
from builder import Builder

def get_files(folder_path):
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    
    return onlyfiles

def parse_files(folder_path, spell_check, playlist_filter):

    temp_output_dir = "./TempJSON"
    verify_temp_directory(temp_output_dir)

    for file in get_files(folder_path):
        _json = carball.decompile_replay(folder_path + "/" + file, 
                                        output_path=temp_output_dir +'/foo.json', 
                                        overwrite=True)
        game = Game()
        game.initialize(loaded_json=_json)
        analysis = AnalysisManager(game)
        analysis.create_analysis()
        raw_json = MessageToJson(analysis.protobuf_game)
        data = json.loads(raw_json)

        f = open(temp_output_dir + "/lastfile.json", "w+")
        f.write(raw_json)
        f.close()

        Builder(data, spell_check, playlist_filter)

def verify_temp_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--folder", dest="folder_path",
                        help="please enter --folder pathToFolder", required=True)

    parser.add_argument("-s", "--spell", dest="spell_check",
                        help="enter Y or N for spell check", default="Y")

    parser.add_argument("-p", "--playlist", dest="playlist_filter",
        help="enter the name of the playlist to filter for", default = None)

    
    args = parser.parse_args()

    parse_files(args.folder_path, args.spell_check, args.playlist_filter)

    OutputHandler(args.folder_path)


if __name__ == "__main__":
    main()




