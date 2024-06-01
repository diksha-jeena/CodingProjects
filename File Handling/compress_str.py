def compress_string(input_string):
    if not input_string:
        return ""

    compressed = []
    count = 1
    prev_char = input_string[0]

    for char in input_string[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(f"{prev_char}{count}")
            prev_char = char
            count = 1

    compressed.append(f"{prev_char}{count}")
    return ''.join(compressed)

#main
input_string = "aaaaabb"
compressed_string = compress_string(input_string)
print(compressed_string)  
