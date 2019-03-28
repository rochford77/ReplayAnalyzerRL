class Player:
    raw_players = []

    def __init__(self, node):
        self.team_name = node["name"] # when team mode is enabled, this is updated, otherwise they are their own team.
        self.games = 1
        self.wins = 0
        self.id = node["id"]["id"]
        self.name = node["name"]

        # (Verified by guys at SaltieRL/Calculated.gg/makers of carball)
        # Carball wont output a key-value pair for something if its value as 0.
        # Python will throw a key error if you set something as a node that isnt there
        # Must handle the errors

        # Primary stats
        try:
            self.isbot = node["isBot"]
        except KeyError:
            self.isbot = False

        try:
            self.goals = node["goals"]
        except KeyError:
            self.goals = 0

        try:
            self.assists = node["assists"]
        except KeyError:
            self.assists = 0

        try:
            self.saves = node["saves"]
        except KeyError:
            self.saves = 0

        try:
            self.shots = node["shots"]
        except KeyError:
            self.shots = 0

        try:
            self.score = node["score"]
        except KeyError:
            self.score = 0

        # Boost Stats
        boost_node = node["stats"]["boost"]
        try:
            self.boostUseage = boost_node["boostUsage"]
        except KeyError:
            self.boostUseage = 0.00

        try:
            self.numSmallBoosts = boost_node["numSmallBoosts"]
        except KeyError:
            self.numSmallBoosts = 0

        try:
            self.numLargeBoosts = boost_node["numLargeBoosts"]
        except KeyError:
            self.numLargeBoosts = 0 

        try:
            self.wastedCollection = boost_node["wastedCollection"]
        except KeyError:
            self.wastedCollection = 0.00

        try:
            self.wastedUsage = boost_node["wastedUsage"]
        except KeyError:
            self.wastedUsage  = 0.00

        try:
            self.timeFullBoost = boost_node["timeFullBoost"]
        except KeyError:
            self.timeFullBoost  = 0.00

        try:
            self.timeLowBoost = boost_node["timeLowBoost"]
        except KeyError:
            self.timeLowBoost = 0.00

        try:
            self.timeNoBoost = boost_node["timeNoBoost"]
        except KeyError:
            self.timeNoBoost = 0.00

        try:
            self.numStolenBoosts = boost_node["numStolenBoosts"]
        except KeyError:
            self.numStolenBoosts = 0

        try:
            self.averageBoostLevel = boost_node["averageBoostLevel"]
        except KeyError:
            self.averageBoostLevel = 0.00

        # Distance Stats
        distance_node = node["stats"]["distance"]
        try:
            self.ballHitForward = distance_node["ballHitForward"]
        except KeyError:
            self.ballHitForward  = 0.00

        try:
            self.timeClosestToBall = distance_node["timeClosestToBall"]
        except KeyError:
            self.timeClosestToBall = 0.00

        try:
            self.timeFurthestFromBall = distance_node["timeFurthestFromBall"]
        except KeyError:
            self.timeFurthestFromBall = 0.00

        # Possession Stats
        possession_node = node["stats"]["possession"]
        try:
            self.possessionTime = possession_node["possessionTime"]
        except KeyError:
            self.possessionTime = 0.00

        try:
            self.turnovers = possession_node["turnovers"]
        except KeyError:
            self.turnovers = 0

        try:
            self.turnoversOnMyHalf = possession_node["turnoversOnMyHalf"]
        except KeyError:
            self.turnoversOnMyHalf = 0

        try:
            self.turnoversOnTheirHalf = possession_node["turnoversOnTheirHalf"]
        except KeyError:
            self.turnoversOnTheirHalf = 0

        try:
            self.wonTurnovers = possession_node["wonTurnovers"]
        except KeyError:
            self.wonTurnovers = 0

        # Positional Stats
        position_node = node["stats"]["positionalTendencies"]
        try:
            self.timeOnGround = position_node["timeOnGround"]
        except KeyError:
            self.timeOnGround  = 0.00

        try:
            self.timeLowInAir = position_node["timeLowInAir"]
        except KeyError:
            self.timeLowInAir  = 0.00

        try:
            self.timeHighInAir = position_node["timeHighInAir"]
        except KeyError:
            self.timeHighInAir = 0.00

        try:
            self.timeInDefendingHalf = position_node["timeInDefendingHalf"]
        except KeyError:
            self.timeInDefendingHalf = 0.00

        try:
            self.timeInAttackingHalf = position_node["timeInAttackingHalf"]
        except KeyError:
            self.timeInAttackingHalf = 0.00

        try:
            self.timeInDefendingThird = position_node["timeInDefendingThird"]
        except KeyError:
            self.timeInDefendingThird = 0.00

        try:
            self.timeInNeutralThird = position_node["timeInNeutralThird"]
        except KeyError:
            self.timeInNeutralThird = 0.00

        try:
            self.timeInAttackingThird = position_node["timeInAttackingThird"]
        except KeyError:
            self.timeInAttackingThird = 0.00

        try:
            self.timeBehindBall = position_node["timeBehindBall"]
        except KeyError:
            self.timeBehindBall = 0.00

        try:
            self.timeInFrontBall = position_node["timeInFrontBall"]
        except KeyError:
            self.timeInFrontBall = 0.00

        try:
            self.timeNearWall = position_node["timeNearWall"]
        except KeyError:
            self.timeNearWall = 0.00

        try:
            self.timeInCorner = position_node["timeInCorner"]
        except KeyError:
            self.timeInCorner = 0.00

        # average stats
        avg_node = node["stats"]["averages"]
        try:
            self.averageSpeed = avg_node["averageSpeed"]
        except KeyError:
            self.averageSpeed = 0.00
        try:
            self.averageHitDistance = avg_node["averageHitDistance"]
        except KeyError:
            self.averageHitDistance = 0.00
        try:
            self.averageDistanceFromCenter = avg_node["averageDistanceFromCenter"]
        except KeyError:
            self.averageDistanceFromCenter = 0.00

        # hit stats
        hit_node = node["stats"]["hitCounts"]
        try:
            self.totalHits = hit_node["totalHits"]
        except KeyError:
            self.totalHits = 0
        try:
            self.totalPasses = hit_node["totalPasses"]
        except KeyError:
            self.totalPasses = 0
        try:
            self.totalShots = hit_node["totalShots"]
        except KeyError:
            self.totalShots = 0
        try:
            self.totalDribbles = hit_node["totalDribbles"]
        except KeyError:
            self.totalDribbles = 0
        try:
            self.totalDribbleConts = hit_node["totalDribbleConts"]
        except KeyError:
            self.totalDribbleConts = 0
        try:
            self.totalAerials = hit_node["totalAerials"]
        except KeyError:
            self.totalAerials = 0

        # speed
        speed_node = node["stats"]["speed"]
        try:
            self.timeAtSlowSpeed = speed_node["timeAtSlowSpeed"]
        except KeyError:
            self.timeAtSlowSpeed = 0.00
        try:
            self.timeAtSuperSonic = speed_node["timeAtSuperSonic"]
        except KeyError:
            self.timeAtSuperSonic = 0.00
        try:
            self.timeAtBoostSpeed = speed_node["timeAtBoostSpeed"]
        except KeyError:
            self.timeAtBoostSpeed = 0.00
        

    def look_for_player_index(self):
        index = -100
        for player in Player.raw_players:
            if player.id == self.id:
                index = Player.raw_players.index(player)
                break
        return index

    def add_player_win(self):
        matched_index = self.look_for_player_index()
        if(matched_index != -100):
            Player.raw_players[matched_index].wins = Player.raw_players[matched_index].wins + 1

    def add_team_name(self, team_name):
        matched_index = self.look_for_player_index()
        if(matched_index != -100):
            Player.raw_players[matched_index].team_name = team_name

    def get_player_by_id(player_id):
        for player in Player.raw_players:
            if player.id == player_id:
                return player

    def add_player(self):
        if len(Player.raw_players) == 0:
            Player.raw_players.append(self)
        else:
            matched_index = self.look_for_player_index()

            if(matched_index == -100):
                Player.raw_players.append(self)
            else:
                # Be sure to scroll right here if your window is less than 140 characters wide (like GitHub)
                # Bad form I guess, but having things lined up is a dream for multi-cursor. Really, game changer.

                Player.raw_players[matched_index].goals                     = Player.raw_players[matched_index].goals                       + self.goals
                Player.raw_players[matched_index].assists                   = Player.raw_players[matched_index].assists                     + self.assists
                Player.raw_players[matched_index].saves                     = Player.raw_players[matched_index].saves                       + self.saves
                Player.raw_players[matched_index].goshotsals                = Player.raw_players[matched_index].shots                       + self.shots
                Player.raw_players[matched_index].score                     = Player.raw_players[matched_index].score                       + self.score
                Player.raw_players[matched_index].games                     = Player.raw_players[matched_index].games                       + self.games
                Player.raw_players[matched_index].boostUseage               = Player.raw_players[matched_index].boostUseage                 + self.boostUseage
                Player.raw_players[matched_index].numSmallBoosts            = Player.raw_players[matched_index].numSmallBoosts              + self.numSmallBoosts
                Player.raw_players[matched_index].numLargeBoosts            = Player.raw_players[matched_index].numLargeBoosts              + self.numLargeBoosts
                Player.raw_players[matched_index].wastedCollection          = Player.raw_players[matched_index].wastedCollection            + self.wastedCollection
                Player.raw_players[matched_index].wastedUsage               = Player.raw_players[matched_index].wastedUsage                 + self.wastedUsage
                Player.raw_players[matched_index].timeFullBoost             = Player.raw_players[matched_index].timeFullBoost               + self.timeFullBoost
                Player.raw_players[matched_index].timeLowBoost              = Player.raw_players[matched_index].timeLowBoost                + self.timeLowBoost
                Player.raw_players[matched_index].timeNoBoost               = Player.raw_players[matched_index].timeNoBoost                 + self.timeNoBoost
                Player.raw_players[matched_index].numStolenBoosts           = Player.raw_players[matched_index].numStolenBoosts             + self.numStolenBoosts
                Player.raw_players[matched_index].averageBoostLevel         = Player.raw_players[matched_index].averageBoostLevel           + self.averageBoostLevel
                Player.raw_players[matched_index].ballHitForward            = Player.raw_players[matched_index].ballHitForward              + self.ballHitForward
                Player.raw_players[matched_index].timeClosestToBall         = Player.raw_players[matched_index].timeClosestToBall           + self.timeClosestToBall
                Player.raw_players[matched_index].timeFurthestFromBall      = Player.raw_players[matched_index].timeFurthestFromBall        + self.timeFurthestFromBall
                Player.raw_players[matched_index].possessionTime            = Player.raw_players[matched_index].possessionTime              + self.possessionTime
                Player.raw_players[matched_index].turnovers                 = Player.raw_players[matched_index].turnovers                   + self.turnovers
                Player.raw_players[matched_index].turnoversOnMyHalf         = Player.raw_players[matched_index].turnoversOnMyHalf           + self.turnoversOnMyHalf
                Player.raw_players[matched_index].turnoversOnTheirHalf      = Player.raw_players[matched_index].turnoversOnTheirHalf        + self.turnoversOnTheirHalf
                Player.raw_players[matched_index].wonTurnovers              = Player.raw_players[matched_index].wonTurnovers                + self.wonTurnovers
                Player.raw_players[matched_index].timeOnGround              = Player.raw_players[matched_index].timeOnGround                + self.timeOnGround
                Player.raw_players[matched_index].timeLowInAir              = Player.raw_players[matched_index].timeLowInAir                + self.timeLowInAir
                Player.raw_players[matched_index].timeHighInAir             = Player.raw_players[matched_index].timeHighInAir               + self.timeHighInAir
                Player.raw_players[matched_index].timeInDefendingHalf       = Player.raw_players[matched_index].timeInDefendingHalf         + self.timeInDefendingHalf
                Player.raw_players[matched_index].timeInAttackingHalf       = Player.raw_players[matched_index].timeInAttackingHalf         + self.timeInAttackingHalf
                Player.raw_players[matched_index].timeInDefendingThird      = Player.raw_players[matched_index].timeInDefendingThird        + self.timeInDefendingThird
                Player.raw_players[matched_index].timeInNeutralThird        = Player.raw_players[matched_index].timeInNeutralThird          + self.timeInNeutralThird
                Player.raw_players[matched_index].timeInAttackingThird      = Player.raw_players[matched_index].timeInAttackingThird        + self.timeInAttackingThird
                Player.raw_players[matched_index].timeBehindBall            = Player.raw_players[matched_index].timeBehindBall              + self.timeBehindBall
                Player.raw_players[matched_index].timeInFrontBall           = Player.raw_players[matched_index].timeInFrontBall             + self.timeInFrontBall
                Player.raw_players[matched_index].timeNearWall              = Player.raw_players[matched_index].timeNearWall                + self.timeNearWall
                Player.raw_players[matched_index].timeInCorner              = Player.raw_players[matched_index].timeInCorner                + self.timeInCorner
                Player.raw_players[matched_index].averageSpeed              = Player.raw_players[matched_index].averageSpeed                + self.averageSpeed
                Player.raw_players[matched_index].averageHitDistance        = Player.raw_players[matched_index].averageHitDistance          + self.averageHitDistance
                Player.raw_players[matched_index].averageDistanceFromCenter = Player.raw_players[matched_index].averageDistanceFromCenter   + self.averageDistanceFromCenter
                Player.raw_players[matched_index].totalHits                 = Player.raw_players[matched_index].totalHits                   + self.totalHits
                Player.raw_players[matched_index].totalPasses               = Player.raw_players[matched_index].totalPasses                 + self.totalPasses
                Player.raw_players[matched_index].totalShots                = Player.raw_players[matched_index].totalShots                  + self.totalShots
                Player.raw_players[matched_index].totalDribbles             = Player.raw_players[matched_index].totalDribbles               + self.totalDribbles
                Player.raw_players[matched_index].totalDribbleConts         = Player.raw_players[matched_index].totalDribbleConts           + self.totalDribbleConts
                Player.raw_players[matched_index].totalAerials              = Player.raw_players[matched_index].totalAerials                + self.totalAerials
                Player.raw_players[matched_index].timeAtSlowSpeed           = Player.raw_players[matched_index].timeAtSlowSpeed             + self.timeAtSlowSpeed
                Player.raw_players[matched_index].timeAtSuperSonic          = Player.raw_players[matched_index].timeAtSuperSonic            + self.timeAtSuperSonic
                Player.raw_players[matched_index].timeAtBoostSpeed          = Player.raw_players[matched_index].timeAtBoostSpeed            + self.timeAtBoostSpeed
