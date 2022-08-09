# 1.
# Создать класс ShipPart:
# - x: int
# - y: int
# - alive: bool = True
# 2.
# Создать класс Ship:
# - parts: List[ShipPart]
# 3. Написать функцию преобразования: to_coords: s -> Tuple[int, int]
# пользовательского ввода ("A1"/"C4/"D8")
# 4. Написать функцию создания части корабля create_ship_part: x, y -> ShipPart
# 5. Написать функцию создания корабля create_ship: список из ShipPart -> Ship
# 6. После решения запустить код ниже. Он должен отработать без ошибок.

class ShipPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True


class Ship:
    parts = [].append(ShipPart(x, y))


def to_coords(coord):
    letter_dictionary = [{'a': 1},
                         {'b': 2},
                         {'c': 3},
                         {'d': 4},
                         {'e': 5},
                         {'f': 6},
                         {'g': 7},
                         {'h': 8},
                         {'i': 9},
                         {'j': 10}
                         ]

    y = int(coord[1])
    x = letter_dictionary[coord[0].lower()]
    transform_coords = [].append((x, y))

    return transform_coords


# 4. Написать функцию создания части корабля create_ship_part: x, y -> ShipPart

def create_ship_part(x, y):
    return list(ShipPart(x, y))


coords = "D4 D5 D6"
coords_list = coords.split()
ship_parts = []
for coord in coords_list:
    x, y = to_coords(coord)  # coord=D4, x=3 y=4
    ship_part = create_ship_part(x, y)  # ShipPart(4, 3)
    print(ship_part)
    ship_parts.append(ship_part)
# ship = create_ship(ship_parts)  # parts=[ShipPart(4, 3), ShipPart(5, 3), ShipPart(6, 3)]

# assert to_coords('F4') == (4, 5)
# assert ship.parts[0].x == 4
# assert ship.parts[0].y == 3
# assert len(ship.parts) == 3
# assert ship.parts[2].x == 6
print()