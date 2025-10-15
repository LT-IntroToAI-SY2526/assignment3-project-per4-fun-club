from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
#FullNamebyPlayerID(ID)
# pID = 201939
# status = False
# pOBJ = []

# player_list = players.get_players()
# for player in player_list:
#     if player['id'] == pID:
#         status = True
#         pOBJ = player
#         break

# print(pOBJ)

# if status == True:
#     print("Player found: " + pOBJ['full_name'])
# else:
#     print("Player not found")

#-----------------------------------------------------------------

def Get_Players_By_TeamID(ID)
    status = False

    team_list = teams.get_teams()
    for team in team_list:
        if ID == team['id']:
            status = True
            break

    if status == True:
        roster = commonteamroster.CommonTeamRoster(team_id=team_id)
        df = roster.get_data_frames()[0]
        return "Players on team: " + ", ".join(df['PLAYER'].tolist())
    else:
        return "No team found: No players on team"

#----------------------------------------------------------------


#----------------------------------------------------------------

#Discovered dictionary data structures - Mention it in presentation
#Discovered data frames
