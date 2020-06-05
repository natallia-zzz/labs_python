def extract_file(file_name):
    txtfile = file_name + 'txt'
    f = open(txtfile, "r")
    return from_json(str_gen(f))


def str_gen(s):
    for ch in s:
        yield ch


def from_json(obj):
    ch = next(obj)
    if ch.isdigit() or ch == "-":
        return json_num(ch, obj)
    elif ch.isalpha():
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
        elif ch.isdigit() or ch.isalpha():
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
    res = []
    while True:
        ch = next(obj)
        if ch.isspace():
            continue
        if ch == "]":
            return res
        if ch == '{':
            res.append(json_dict(obj))
        elif ch == '[':
            res.append(json_list(obj))
        elif ch == '"':
            res.append(json_str(obj))
        elif ch.isdigit() or ch == '-':
            res.append(json_num(ch, obj))
        elif ch.isalpha():
            value = json_val(ch, obj)
            if value == "true":
                res.append(True)
            elif value == "false":
                res.append(False)
            elif value == "null":
                res.append(None)
            else:
                raise ValueError


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
