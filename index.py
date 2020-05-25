from os import listdir
from os.path import isfile, join
from colorama import Fore


def readTxtFile(filename):
    f = open(filename, "r")
    s = f.read()
    f.close()
    return s.replace('\n', ' ').replace('\r', ' ').split(' ')


def printColred(keywords):
    result = ''
    hotkeys = []
    for word in keywords:
        index = 0
        if word[index] in hotkeys:
            for w in word:
                if w in hotkeys:
                    index += 1
                    continue
        hotkeys.append(word[index])
        if index == 0:
            word = f'{Fore.RED}{word[0]}{Fore.YELLOW}{word[1:]}'
        else:
            word = f'{Fore.YELLOW}{word[:index]}{Fore.RED}{word[index]}{Fore.YELLOW}{word[(index + 1):]}'
        result += word + ' '
    print(result)
    return hotkeys


def main(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    menufile = 'menu.txt'
    keywords = readTxtFile(menufile)
    hotkeys = printColred(keywords)
    key = input('Input one of red characters : ')
    index = 0
    for hot in hotkeys:
        if hot == key:
            key = keywords[index]
            break
        index += 1
    for word in keywords:
        if key in word:
            key = word
            break
    if key + '.txt' in onlyfiles:
        subkeywords = readTxtFile(key + '.txt')
        printColred(subkeywords)
    else:
        print('There is no text file named', key + '.txt')
        print('Files', onlyfiles)


# word = 'hello, world'
# word = f'{Fore.RED}{word[0]}{Fore.YELLOW}{word[1:]}'
# print(word)
if __name__ == '__main__':
    main('.')
