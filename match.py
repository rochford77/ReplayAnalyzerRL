class Match:
    raw_matches = []

    def __init__(self, map, time, guid, playlist):
        self.map = map
        self.time = time
        self.guid = guid
        self.playlist = playlist

    def look_for_match_index(match_guid):
        index = -100
        for match in Match.raw_matches:
            if match.guid == match_guid:
                index = Match.raw_matches.index(match)
                break
        return index

    def add_match(m):
        if len(Match.raw_matches) == 0:
            Match.raw_matches.append(m)
        else:
            matched_index = Match.look_for_match_index(m.guid)

            if (matched_index == -100):
                Match.raw_matches.append(m)

    def get_match(guid):
        index = Match.look_for_match_index(guid)
        return Match.raw_matches[index]

    