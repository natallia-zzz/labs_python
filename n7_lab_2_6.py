from string import ascii_letters as letter


def extract_file(file_name):
    txtfile = file_name+'txt'
    f = open(txtfile, "r")
    return f.read()


def from_json(obj):
    ch = next(obj)
    if ch.isdigit() or ch == "-":
        return json_num(ch, obj)
    elif ch in letter:
        return json_str(ch, obj)
    else:
        raise ValueError


def json_num(first_ch, obj):
    num_str = first_ch
    is_int = True
    while True:
        ch = next(obj)
        if ch.isspace():
            if is_int:
                return int(num_str)
            else:
                return float(num_str)
        elif ch.isdigit():
            num_str += ch
        elif ch == ".":
            is_int = False
            num_str += ch
        else:
            raise ValueError
