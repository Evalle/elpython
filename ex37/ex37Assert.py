def some_input():
    user_input = raw_input("> ")
    assert (user_input == 0),"Input can't equal to 0"
    return user_input

some_input()
