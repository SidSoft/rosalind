def read_fasta(file):
    f = open(file, 'r')
    identifier = ''
    string = ''
    strings = []
    for line in f:
        if line[0] == '>':
            if string != '':
                if identifier != '':
                    strings.append({'id': identifier, 'line': string})
                else:
                    strings.append(string)
                string = ''
            identifier = line[1:].strip('\t\n')
        else:
                string += line.strip('\t\n')
    if identifier != '':
        strings.append({'id': identifier, 'line': string})
    else:
        strings.append(string)
    return strings


print(read_fasta('test.txt'))
