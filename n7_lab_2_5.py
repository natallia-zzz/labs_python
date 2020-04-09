def to_json(obj):
    if isinstance(obj, int):
        return "%d" % obj
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif isinstance(obj, float):
        return "%f" % obj
    elif isinstance(obj, bool):
        if obj:
            return "True"
        else:
            return "False"
    else:
        raise ValueError
