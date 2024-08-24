FILEPATH = "todos.txt"


def get_todos(filepath= FILEPATH):
    """ Read a text file and return the
    to-do items.
    """
    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_todos(todos_w, filepath_w=FILEPATH):
    """ Write the to-d- items in the text file. """
    with open(filepath_w, "w") as file_write:
        file_write.writelines(todos_w)

