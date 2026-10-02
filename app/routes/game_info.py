from fastapi import APIRouter

router = APIRouter()


@router.get("/game-info")
def game_info():
    return {
        "slug": "monster-quiz-battle",
        "name": "Monster Quiz Battle",
        "team": "Team 5 (BSCS 3-1)",  # TODO: your team name and section
        "description": "Answer questions to damage the monster, open mystery chests, "
                       "and deal the most damage before time runs out.",
        "min_players": 1,
        "max_players": 30,  # TODO: confirm with your team
        "thumbnail_url": "/games/monster-quiz-battle/thumbnail.png",
        "play_url": "/games/monster-quiz-battle/",
        "version": "1.0.0",
    }
