from string import ascii_letters as letter


def extract_file(file_name):
    txtfile = file_name+'txt'
    f = open(txtfile, "r")
    print(f.read())
    return from_json(f.read())


def from_json(obj):
    ch = next(obj)
    if ch.isdigit() or ch == "-":
        return json_num(ch, obj)
    elif ch in letter:
        val = json_val(ch, obj)
        if val == "null":
            return None
        elif val == "true":
            return True
        elif val == "false":
            return False
        else:
            raise ValueError
    elif ch == '"':
        return json_str(obj)
    elif ch == "[":
        return json_list(obj)
    elif ch == "{":
        return json_dict(obj)
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


def json_val(first_ch, obj):
    val = first_ch
    while True:
        ch = next(obj)
        if ch.isspace() or ch == ',':
            return val
        elif ch.isdigit() or ch in letter:
            val += ch
        else:
            raise ValueError


def json_str(obj):
    string = ''
    while True:
        ch = next(obj)
        if ch == '"':
            return string
        else:
            string += ch


def json_list(obj):
    list = []
    while True:
        ch = next(obj)
        if ch.isspace() or ch == ',':
            continue
        elif ch == "]":
            return list
        else:
            list += from_json(obj)


def json_dict(obj):
    dict = {}
    while True:
        ch = next(obj)
        if ch.isspace() or ch == ',':
            continue
        elif ch == '}':
            return dict
        elif ch == '"':
            k = json_str(obj)
            while True:
                ch = next(obj)
                if ch.isspace():
                    continue
                elif ch == ':':
                    break
                else:
                    raise ValueError
            v = from_json(obj)
            dict[k] = v
        else:
            raise ValueError
