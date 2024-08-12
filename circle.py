from vector import Vector2


# =================== helper functions and class ===================


class Run:
    def __init__(self, element, length: int):
        self.element = element
        self.length = length

    def __str__(self) -> str:
        return f"{self.length} {self.element}'s"

    def __repr__(self) -> str:
        return str(self)

def print_when_entered(elements: list):
    for element in elements:
        print(element)
        input()

def blocks_to_stacks(blocks: int):
    stacks, blocks = divmod(blocks, 64)
    print(f"{stacks} stacks, and {blocks} blocks.")

str_to_sections = lambda x: list(map(int, x.split(" ")))

sections_to_blocks = lambda x: sum(map(int, str_to_sections(x)))

sections_to_stacks = lambda x: blocks_to_stacks(sections_to_blocks(x))


# =================== start of actual functions ===================


def rle(sections: list[int]) ->list[Run]:
    runs = []
    count = 1

    buffer = sections[0]
    for section in sections[1:]:
        if section != buffer:
            runs.append(Run(buffer, count))
            buffer = section
            count = 1
        else:
            count += 1

    runs.append(Run(buffer, count))

    return runs

        
def rle_to_coordinates(runs: list[Run]) -> list[Vector2]:
    point = Vector2(x = -1, y = 0)
    points = []
    for run in runs:
        point += Vector2(run.length, run.length * run.element)
        points.append(Vector2(point.y, point.x))

    return points


def combine_runs_and_coords(rle: list[Run], coords: list[Vector2]):
    transform = lambda x: f"{x[0]} to {x[1]}"
    return list(map(transform, zip(rle, coords)))


# ===================end of actual functions===================


def main(sections_string: str):
    sections = str_to_sections(sections_string)
    runs = rle(sections)
    coords = rle_to_coordinates(runs)
    combined = combine_runs_and_coords(runs, coords)
    print_when_entered(combined)
    return combined

if __name__ == "__main__":
    main(input("string: "))
