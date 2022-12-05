 #!/usr/bin/python3
""" addition of two integers"""
def add_integer(c=0, d=98):

    """ function adds two integers """
    if type(c) is not int and type(c) is not float:
        raise TypeError("c has to be an integer")
    if type(d) is not int and type(c) is not float:
        raise TypeError("b must be an integer")
    if type(c) is float:
        c= int(c)
    if type(d) is float:
        c= int(d)
    return c+ d
