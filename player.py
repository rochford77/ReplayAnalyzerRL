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
        self.wins = 0

    def look_for_player_index(player_id):
        index = -100
        for player in Player.raw_players:
            if player.id == player_id:
                index = Player.raw_players.index(player)
                break
        return index

    def add_player_win(player_id):
        matched_index = Player.look_for_player_index(player_id)
        if(matched_index != -100):
            Player.raw_players[matched_index].wins = Player.raw_players[matched_index].wins + 1

    def add_team_name(team_name, player_id):
        matched_index = Player.look_for_player_index(player_id)
        if(matched_index != -100):
            Player.raw_players[matched_index].team_name = team_name

    def get_player_name_by_id(player_id):
        for player in Player.raw_players:
            if player.id == player_id:
                return player.name

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