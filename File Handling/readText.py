def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

filename = 'example.txt'
read_and_print_file(filename)
