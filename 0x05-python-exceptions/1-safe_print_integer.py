
#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (isinstance(value, int)):
            print("{:d}".format(value))
            return True
        else:
            return False
    except Exception as e:
        return e
#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value[i], int):
            print("{:d}".format(value)) 
            return True
        else:
            return False
    except ValueError:
        return ValueError
