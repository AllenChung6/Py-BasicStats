from statzcw.stats import read_data_sets_x, read_data_sets_y
from sys import argv

if __name__ == "__main__":
    z = read_data_sets_x(argv[1:])
    y = read_data_sets_y(argv[1:])
    print(y)