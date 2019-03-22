class Team:
    raw_teams = []

    def __init__(self, score, name, win):
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