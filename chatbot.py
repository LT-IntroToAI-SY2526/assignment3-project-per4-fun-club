from nba import nba_db
from match import match
from typing import List, Tuple, Callable, Any

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

def year_by_name(matches: List[str]) -> List[int]:
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
	return result

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what year was _ drafted"), year_by_name),
    (str.split("what team does % play for"), team_by_name),
    (["bye"], bye_action),
] # Every Tuple: (pattern, action_function)

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["Sorry, no answers were found."]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["Sorry, no answers were found."] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["Sorry, no answers were found."]
    return["I don't understand"]

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


if __name__ == "__main__":
	assert isinstance(year_by_name(["james harden"]), list), "year_by_name not returning a list"
	assert sorted(year_by_name(["james harden"])) == sorted(
        [2009]
    ), "failed year_by_name test"
	print("All tests passed!")