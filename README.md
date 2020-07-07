# Description
This program takes as an input a quasipositive braid and generates a .tex file
which, when compiled by the user, gives a visualisation of its positive braid surface.

# Usage
0. Open a terminal and navigate to your desired
working directory.
1. Make sure you have python installed by 
typing `python --version` into the terminal. 
Expect the output to be `Python 3.x.x`. Install or update
python if necessary.
2. Similarly, make sure you have git installed.
3. Clone this repository by typing
`git clone https://github.com/raw-bacon/qp-tikz`. This will create
a folder called `qp-tikz` in your current directory.
4. Go into the newly created folder by typing `cd qp-tikz`.
5. Run the program by typing `python qp.py`.
6. Follow the prompts.
7. After having the program save a .tex file, compile it using your favorite LaTeX compiler.
You should now have a pdf containing just a figure, which you can import into your LaTeX document as you would any other figure.

# Example Output
Entering `1,5/2,4/1,6/3,4/3,4/1,3/1,6/2,6` will produce the following figure.

![](https://github.com/raw-bacon/qp-tikz/blob/master/example.png "Example" | height = 300)
