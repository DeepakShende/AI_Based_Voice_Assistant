def remove_none(self):
    if hasattr(self, '__dict__'):
        di = self.__dict__
        keys = []
        for key in di.keys():
            obj = di[key]
            if obj is None:
                keys.append(key)
            else:
                remove_none(obj)
        for key in keys:
            del di[key]
    elif type(self) is list:
        for item in self:
            remove_none(item)


def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    if ltype not in ltypes:
        return l
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)
