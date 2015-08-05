from sys import exit

book_shelf = ['Bash', 'Python', 'MariaDB', 'Chef', 'PHP', 'Databases']

print book_shelf

choice = int(raw_input('> please select one book form the bookshelf (ex: 1,2,3 ... ) :> ' ))

if choice > 6 or choice == 0:
    print 'Sorry we have only 6 books on the shelf'
    exit(0)
else:
    print book_shelf.pop(choice - 1)

print 'Now we have these books on the book_shelf: ', book_shelf
