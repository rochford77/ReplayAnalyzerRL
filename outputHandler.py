from team import Team
from player import Player
from match import Match

class OutputHandler():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.create_team_output()
        self.create_player_output()

    def create_player_output(self):

        player_header_data = ("ID,NAME,TEAM,GOALS,ASSISTS,SAVES,SHOTS,SCORE,GAMES,WINS,BOOST USAGE,NUMBER OF SMALL BOOSTS,"
            + "NUMBER OF LARGE BOOSTS,WASTED COLLECTION,WASTED USAGE,TIME FULL BOOST,TIME LOW BOOST,TIME NO BOOST,STOLEN BOOSTS,"
            + "AVERAGE BOOST LVL,BALL HIT FORWARD,T NEAREST BALL,T FURTHEST BALL,POSSESSION T,TURNOVERS,TURNOVERS MY HALF,"
            + "TURNOVERS THEIR HALF,WON TURNOVERS,T ON GROUND,T LOW AIR,T HIGH AIR,T DEFENDING HALF,T ATTACKING HALF,"
            + "T DEFENDING THIRD,T NEUTRAL THIRD,T ATTACKING THIRD,T BEHIND BALL,T FRONT BALL,T NEAR WALL,T CORNER,AVG SPEED,"
            + "AVG HIT DISTANCE,AVG DISTANCE FROM CENTER,TOTAL HITS,TOTAL PASSES,TOTAL SHOTS,TOTAL DRIBBLES,TOTAL DTIBBLE CONTS,"
            + "TOTAL AERIALS,T AT SLOW SPEED,T AT SUPERSONIC,T AT BOOST SPEED\n"
        )

        self.write_output_file(self.folder_path + "player_data.csv", player_header_data, "w+")

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
                + "," + str(thePlayer.wins)
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
            self.write_output_file(self.folder_path + "player_data.csv", player_data, "a")

    def create_team_output(self):
        team_header_data = ("NAME,SCORE,WINS,GAMES\n")

        self.write_output_file(self.folder_path + "team_data.csv", team_header_data, "w+")

        for theTeam in Team.raw_teams:
            team_data = (str(theTeam.name)
                + "," + str(theTeam.score)
                + "," + str(theTeam.win)
                + "," + str(theTeam.games)
                + "," + str(theTeam.maps_played)
                +"\n"
            )
            self.write_output_file(self.folder_path + "team_data.csv", team_data, "a")

    
    def write_output_file(self, filename, data, permissions):
        player_file = open(filename, permissions)
        player_file.write(data)
        player_file.close()