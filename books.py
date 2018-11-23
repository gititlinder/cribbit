"""
This is the Books Module
"""
import os
import shutil

def list_books():
    foldername = os.path.abspath(os.path.join('.', 'books'))
    for dirName, subdirList, fileList in os.walk(foldername):
        for book in subdirList:
            print(book)


def add_book(book):
    foldername = os.path.abspath(os.path.join('.', 'books', book))
    if os.path.exists(foldername):
        print('Book:', book, 'already exists')
    else:
        print('Creating', book)
        os.mkdir(foldername)


def delete_book(book):
    foldername = os.path.abspath(os.path.join('.', 'books', book))
    if os.path.exists(foldername):
        print('Deleting', book)
        shutil.rmtree(foldername, ignore_errors=True)
    else:
        print('Book:', book, 'does not exist')


def open_book(book):
    foundbook = 0
    foldername = os.path.abspath(os.path.join('.', 'books'))
    for dirName, subdirList, fileList in os.walk(foldername):
        for bookname in subdirList:
            if (book == bookname):
                foundbook = 1
    if foundbook:
        pass
    else:
        print('Could not find', book)
    return foundbook
