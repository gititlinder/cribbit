"""
This is the Notes Module
"""
import os


def add_note(book, note):
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)

    foldername = os.path.abspath(os.path.join('.', 'books', book))
    filename = os.path.abspath(os.path.join('.', 'books', book, note + '.txt'))

    f = open(filename, "w")
    f.write(text)


def read_note(book, note):
    data = []
    filename = os.path.abspath(os.path.join('.', 'books', book, note + '.txt'))

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    for d in data:
        print(d)


def delete_note(book, note):
    filename = os.path.abspath(os.path.join('.', 'books', book, note + '.txt'))

    if os.path.exists(filename):
        os.remove(filename)
        print(note,"deleted")
    else:
        print(note, "does not exist")


def edit_note(book, note):
    filename = os.path.abspath(os.path.join('.', 'books', book, note + '.txt'))

    if os.path.exists(filename):
        read_note(book,note)
        print('Enter new lines below:')
        os.remove(filename)
        add_note(book,note)

    else:
        print(note, "does not exist")


def list_notes(book):
    foldername = os.path.abspath(os.path.join('.', 'books', book))
    for dirName, subdirList, fileList in os.walk(foldername):
        for note in fileList:
            print(note[0:-4])
