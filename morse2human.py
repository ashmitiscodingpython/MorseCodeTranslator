code = ''
decode = {
    '._': 'A',
    '_...': 'B',
    '_._.': 'C',
    '_..': 'D',
    '.': 'E',
    '.._.': 'F',
    '__.': 'G',
    '....': 'H',
    '..': 'I',
    '.___': 'J',
    '_._': 'K',
    '._..': 'L',
    '__': 'M',
    '_.': 'N',
    '___': 'O',
    '.__.': 'P',
    '__._': 'Q',
    '._.': 'R',
    '...': 'S',
    '_': 'T',
    '.._': 'U',
    '..._': 'V',
    '.__': 'W',
    '_.._': 'X',
    '_.__': 'Y',
    '__..': 'Z',
    '|': ' ',
    '._._._': '.'
}
print('THIS IS A MORSE>ENGLISH TRANSLATOR. ENTER YOUR TEXT DOWN BELOW.')
code = input('> ')
letters = code.split(' ')
for letter in letters:
    print(decode.get(letter), end='')
