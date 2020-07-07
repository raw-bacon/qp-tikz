from BraidParser import parse
from Surface import Surface

print("Please enter a braid, e.g., 1,2/1,3/1,4 for sigma_(1,2) * sigma_(1,3) * sigma_(1, 4).\n")
string = input("Your braid:")

surface = Surface(parse(string))

print("Your tikz code:\n")
print(surface.to_tikz())
