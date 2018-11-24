'''
Application : Cribbit
Version:\ 0.0.3
Author: Steve Linder
'''

import books
import notes


def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('          Cribbit')
    print('----------------------------')
    print()


def books_header():
    print('----------------------------')
    print('          Books')
    print('----------------------------')
    print()


def notes_header(book_name):
    print('----------------------------')
    print('          {}'.format(book_name))
    print('          Notes')
    print('----------------------------')
    print()


def notes_menu(book_name):
    notes_header(book_name)
    notes.list_notes(book_name)
    notescmd = 'Empty'
    while notescmd != 'X' and notescmd:
        notescmd = input('[A]dd, [D]elete, [E]dit, [L]ist, [R]ead, E[x]it: ')
        notescmd = notescmd.upper().strip()

        if notescmd == 'L':
            notes.list_notes(book_name)

        elif notescmd == 'A':
            note_name = input('Name of your note: ')
            notes.add_note(book_name, note_name)
        elif notescmd == 'D':
            note_name = input('Name of note to delete: ')
            notes.delete_note(book_name, note_name)
        elif notescmd == 'E':
            note_name = input('Name of note to edit: ')
            notes.edit_note(book_name, note_name)

        elif notescmd == 'R':
            note_name = input('Name of the note to read: ')
            notes.read_note(book_name, note_name)

        elif notescmd != 'X' and notescmd:
            print('Bad Entry = {}'.format(notescmd))

    return


def run_event_loop():
    books_header()
    books.list_books()
    cmd = 'Empty'

    while cmd != 'X' and cmd:
        cmd = input('[A]dd, [D]elete, [L]ist, [O]pen, E[x]it: ')
        cmd = cmd.upper().strip()

        if cmd == 'L':
            books.list_books()

        elif cmd == 'A':
            book_name = input('Name of your book: ')
            books.add_book(book_name)
            notes_menu(book_name)

        elif cmd == 'D':
            book_name = input('Name of book to delete: ')
            books.delete_book(book_name)

        elif cmd == 'O':
            book_name = input('Name of the book to open: ')
            found = 0
            found = books.open_book(book_name)
            if found:
                notes_menu(book_name)

        elif cmd != 'X' and cmd:
            print('Bad Entry = {}'.format(cmd))

    print('Goodbye')

if __name__ == '__main__':
    main()
