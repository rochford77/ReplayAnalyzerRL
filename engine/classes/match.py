class Match:
    raw_matches = []

    def __init__(self, data, playlist_filter):
        self.map = data["gameMetadata"]["map"]
        self.time = data["gameMetadata"]["time"]
        self.guid = data["gameMetadata"]["matchGuid"]
        self.playlist = data["gameMetadata"]["playlist"]
        self.valid_match_created = self.check_valid_match(playlist_filter)


    def look_for_match_index(self):
        index = -100
        for match in Match.raw_matches:
            if match.guid == self.guid:
                index = Match.raw_matches.index(match)
                break
        return index

    def check_valid_match(self, playlist_filter):
        valid_match = False
        is_valid_playlist = (playlist_filter == None or playlist_filter == self.playlist)

        if ((self.look_for_match_index() == -100) and is_valid_playlist):
            self.add_match()
            valid_match = True
        return valid_match

    def add_match(self):
        if len(Match.raw_matches) == 0:
            Match.raw_matches.append(self)
        else:
            matched_index = self.look_for_match_index()
            if (matched_index == -100):
                Match.raw_matches.append(self)

