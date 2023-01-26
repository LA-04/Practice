from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


# def generate_stamp(previous_value):
#     score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
#     home_score_change = 1 if score_changed and random.random() > 1 - \
#                              PROBABILITY_HOME_SCORE else 0
#     away_score_change = 1 if score_changed and not home_score_change else 0
#     offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1
#
#     return {
#         "offset": previous_value["offset"] + offset_change,
#         "score": {
#             "home": previous_value["score"]["home"] + home_score_change,
#             "away": previous_value["score"]["away"] + away_score_change
#         }
#     }
#
#
# def generate_game():
#     stamps = [INITIAL_STAMP, ]
#     current_stamp = INITIAL_STAMP
#     for _ in range(TIMESTAMPS_COUNT):
#         current_stamp = generate_stamp(current_stamp)
#         stamps.append(current_stamp)
#
#     return stamps
#
#
# game_stamps = generate_game()
#
# pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    goals = [INITIAL_STAMP, ]
    home = 0
    away = 0

    for game in game_stamps:
        if game["score"]["home"] != home or game["score"]["away"] != away:
            goals.append(game)
            home = game["score"]["home"]
            away = game["score"]["away"]
    goals.append(game_stamps[-1])
    print(goals)
    for id, goal in enumerate(goals):
        if offset < goal["offset"]:
            return goals[id - 1]["score"]["home"], goals[id - 1]["score"]["away"]
        if offset == goal["offset"]:
            return goals[id]["score"]["home"], goals[id]["score"]["away"]


last_offset = game_stamps[-1]["offset"]
offset = int(input(f'Enter a number in the range from 0 to {last_offset}: '))

home, away = get_score(game_stamps, offset)

print(f"Home {home}:{away} Away")
