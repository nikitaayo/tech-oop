import sys

from container import Container


def main():
    input_file = open(sys.argv[1], "r")

    print('Start')

    container = Container()
    container.read_from(input_file)

    print('Filled container')

    output_file = open(sys.argv[2], "w")
    #container.write_to(output_file)
    container.write_two_dim_array_to(output_file)

    container.clear()

    print('Empty container')
    container.write_to(output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()