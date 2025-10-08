from nba import nba_db
from match import match
from typing import List, Tuple, Callablle, Any

def get_name(player: Tuple[str, int, str, List[str]]) -> str:
	return player[0]
def get_draftYear(player: Tuple[str, int, str, List[str]]) -> int:
	return player[1]
def get_currentTeam(player: Tuple[str, int, str, List[str]]) -> str:
	return player[2]
def get_teams(player: Tuple[str, int, str, List[str]]) -> List[str]:
	return player[3]

# Function to return teams based on name, return current team based on name, return draft year based on name, 

def team_by_name(matches: List[str]) -> List[str]:
"""Finds current team of NBA player
Args:
		matches - a list of one string, just the player's name
Returns:
		a list of 1 string, the player's current team
"""
name = matches[0]
result = []
for player in nba_db:
		if get_name(player) == name:
			result.append(get_currentTeam(player))
return result

def year_by_name(matches: List[str]) -> List[in]:
	"""Finds draft year of passed player
	Args:
		matches - a list of 1 string, just the player's name
	Returns:
		a list of one item (an int), the draft year of the player
	"""
	name = matches[0]
	result = []
	for player in nba_db:
		if get_name(player) == name:
			result.append(get_draftYear(player))
	return result

def teams_by_name(matches: List[str]) -> List[str]:
	"""Finds teams the player has played for
	Args:
		matches - a list of 1 string, just the player's name
	Returns:
		a list of teams the player has played for
"""
name = matches[0]
result = []
for player in nba_db:
	if get_name(player) == name:
		result = get_teams(player)
		break
