def direction(facing: str, turn: int):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    if facing not in directions or turn < -1080 or turn > 1080:
        return 'Incorrect input'

    turns = turn // 45
    start = directions.index(facing)
    end = (start + turns) % len(directions)
    
    return directions[end]
