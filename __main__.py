from parsing import parse
from Surface import Surface

print("Please enter a braid, e.g., 1,2/1,3/1,4 for sigma_(1,2) * sigma_(1,3) * sigma_(1, 4).\n")
string = input("Your braid: ")

surface = Surface(parse(string))


print("Would you like to tune the appearance of your positive braid surface? [y,n]")
yesno = input("Your answer: ")

if yesno.lower() == "y":
    surface.width_of_disks = float(input("width of disks (default 1):"))
    surface.width_of_bands = float(input("width of bands (default 3):"))
    surface.distance_of_disks = float(input("distance of disks (default 2):"))
    surface.distance_of_bands = float(input("distance of bands (default 1):"))
    surface.buffer = float(input("buffer (default 3):"))

print("Please enter a .tex filename, e.g., my_braid.tex")
filename = input("Your filename: ")

with open(filename, 'w') as file:
    file.write(surface.to_tikz())

print("Wrote to " + filename)
