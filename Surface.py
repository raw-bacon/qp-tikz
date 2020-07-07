from typing import List, Tuple


class Surface:
    # class variables
    width_of_disks = 1
    width_of_bands = 3
    distance_of_disks = 2
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
        self.transpositions = [(i-1, j-1) for (i, j) in transpositions]

    def to_tikz(self) -> str:
        tikz = ""

        # the disks
        tikz += "% The disks\n"
        for k in range(self.number_of_strands):
            x = k * (self.width_of_disks + self.distance_of_disks)
            y = 0
            tikz += "\\draw[rounded corners, fill=black!10] (" + str(x) + "," + str(y) + ") -- \n"
            x += self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            y += len(self.transpositions) * (self.distance_of_bands + self.width_of_bands) + \
                 2*self.buffer - self.distance_of_bands
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            x -= self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            tikz += "\t\tcycle;\n\n"

        # erasing stuff
        tikz += "% Erasing the lines below the future bands\n"
        y = self.buffer
        for t in self.transpositions:
            y += 2 * self.width_of_bands / 3

            # erasing highest
            x = t[1] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\\draw[thick, color=black!10] (" + str(x) + ", " + str(y) + ") -- "
            y += self.width_of_bands / 3
            tikz += "(" + str(x) + ", " + str(y) + ");\n"
            y -= self.width_of_bands

            # erasing leftest

            x = t[0] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\\draw[thick, color=black!10] (" + str(x) + ", " + str(y) + ") -- "
            y += self.width_of_bands / 3
            tikz += "(" + str(x) + ", " + str(y) + ");\n"
            y -= self.width_of_bands / 3

            for i in range(t[0], t[1]):
                x = (i + 1) * (self.width_of_disks + self.distance_of_disks)
                tikz += "\\draw[thick, color=black!10] (" + str(x) + ", " + str(y) + ") -- "
                y += self.width_of_bands / 3
                tikz += "(" + str(x) + ", " + str(y) + ");\n"
                y -= self.width_of_bands / 3

                x += self.width_of_disks
                tikz += "\\draw[thick, color=black!10] (" + str(x) + ", " + str(y) + ") -- "
                y += self.width_of_bands / 3
                tikz += "(" + str(x) + ", " + str(y) + ");\n"
                y -= self.width_of_bands / 3

            y += self.distance_of_bands + self.width_of_bands


        # filling the bands
        tikz += "\n"
        tikz += "% The bands; filling\n"
        y = self.buffer + self.width_of_bands
        for t in self.transpositions:
            x = t[0] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            y -= 2 * self.width_of_bands / 3
            tikz += "\\fill[black!10] (" + str(x) + ", " + str(y) + ") --\n"
            x = t[1] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") .. \n"
            tikz += "\t\tcontrols +(" + str(self.width_of_bands / 6) + ", 0) and +(" \
                    + str(self.width_of_bands / 6) + ", 0)\n"
            y += self.width_of_bands / 3
            tikz += "\t\t.. (" + str(x) + ", " + str(y) + ") -- \n"
            y += self.width_of_bands / 3
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") .. \n"

            tikz += "\t\tcontrols +(" + str(self.width_of_bands / 2) + ", 0) and +(" \
                    + str(self.width_of_bands / 2) + ", 0) ..\n"
            y -= self.width_of_bands
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") -- \n"
            x = t[0] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks

            tikz += "\t\t(" + str(x) + ", " + str(y) + ");\n\n"
            y += self.distance_of_bands + 2 * self.width_of_bands


        # drawing the bands
        tikz += "\n"
        tikz += "% The bands; boundary lines\n"
        y = self.buffer + self.width_of_bands
        for t in self.transpositions:
            x = t[0] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            y -= 2 * self.width_of_bands / 3
            tikz += "\\draw (" + str(x) + ", " + str(y) + ") --\n"
            x = t[1] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") .. \n"

            tikz += "\t\tcontrols +(" + str(self.width_of_bands / 6) + ", 0) and +(" \
                    + str(self.width_of_bands / 6) + ", 0)\n"
            y += self.width_of_bands / 3
            tikz += "\t\t.. (" + str(x) + ", " + str(y) + ");\n"

            y -= 2 * self.width_of_bands / 3
            x = t[0] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\\draw (" + str(x) + ", " + str(y) + ") --\n"
            x = t[1] * (self.width_of_disks + self.distance_of_disks) + self.width_of_disks
            tikz += "\t\t(" + str(x) + ", " + str(y) + ") .. \n"

            tikz += "\t\tcontrols +(" + str(self.width_of_bands / 2) + ", 0) and +(" \
                    + str(self.width_of_bands / 2) + ", 0)\n"
            y += self.width_of_bands
            tikz += "\t\t.. (" + str(x) + ", " + str(y) + ");\n"

            y += self.distance_of_bands + self.width_of_bands

        return tikz
