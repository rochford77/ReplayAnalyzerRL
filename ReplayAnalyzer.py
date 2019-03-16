import carball

manager = carball.analyze_replay_file('MouseRat_4C4D838E11E94399D89A45AEDD16B2E9.replay', 
                                      output_path='9EB5E5814D73F55B51A1BD9664D4CBF3.json', 
                                      overwrite=True)
proto_game = manager.get_protobuf_data()