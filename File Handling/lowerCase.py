def remove_lowercase(infile , outfile):
    with open(outfile,"w") as output:
        with open(infile) as input_file:
            for line in input_file:
                if not line or line[0] not in "abcdefghijklmnopqrstuvwxyz":
                    output.write(line)
            