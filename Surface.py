from typing import List, Tuple


class Surface:
    # class variables
    width_of_disks = 1
    width_of_bands = 0.5
    distance_of_disks = 0.5
    distance_of_bands = 1
    buffer = 1


    # instance variables
    transpositions: List[Tuple[int, int]]
    number_of_strands: int

    # each tuple in transpositions should be sorted in ascending order
    def __init__(self, transpositions: List[Tuple[int, int]], number_of_strands=None):
        if number_of_strands is None:
            number_of_strands = max(t[1] for t in transpositions)
        self.number_of_strands = number_of_strands
        self.transpositions = transpositions

    def to_tikz(self) -> str:
        tikz = ""

        # the disks
        tikz += "% The disks\n"
        for k in range(self.number_of_strands):
            x = k * (self.width_of_disks + self.distance_of_disks)
            y = 0
            tikz += "\\draw[rounded corners] (" + str(x) + "," + str(y) + ") -- \n"
            x += self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            y += len(self.transpositions) * (self.distance_of_bands + self.width_of_bands) + 2*self.buffer
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            x -= self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            tikz += "\t\tcycle;\n\n"

        # erasing stuff
        tikz += "% Erasing the lines below the future bands\n"
        for i, t in enumerate(self.transpositions):
            # TODO
            tikz += "\\draw[fill=white] ..."

        return tikz
