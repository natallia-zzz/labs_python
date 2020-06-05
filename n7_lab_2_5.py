def dict_to_json(d, indent=0):
    result = "{"
    for k, v in d.items():
        if type(k) != str:
            raise ValueError  # the key must be a string
        if result != "{":
            result += ","
        result += "\n" + ' ' * (indent + 2)
        result += '"' + k + '": '
        result += to_json(v, indent + 2)
    result += "\n" + ' ' * indent
    result += "}"
    return result


def list_to_json(li, indent=0):
    result = "["
    for el in li:
        if result != "[":
            result += ","
        result += "\n" + ' ' * (indent + 2)
        result += to_json(el)
    result += "\n" + ' ' * indent
    result += "]"
    return result


def to_json(obj, indent=0):
    if isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif isinstance(obj, float):
        return str(obj)
    elif isinstance(obj, bool):
        if obj:
            return "True"
        else:
            return "False"
    if isinstance(obj, dict):
        return dict_to_json(obj, indent)
    if isinstance(obj, (list, tuple)):
        return list_to_json(obj, indent)
    else:
        raise ValueError


def write_file(obj):
    f = open("json_file.txt", "a")
    f.write(to_json(obj))
    f.close()
