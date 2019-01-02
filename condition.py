dd = [
    {
        "gender": "male",
        "name": "mark"
    },
    {
        "gender": "female",
        "name": "jane"
    },
    {
        "gender": "male",
        "name": "john"
    }
]


def replace_all(text, keys_, xc):
    for t in keys_:
        # print(xc[t])
        dc = text.split(t)
        # print(dc)
        text = xc[t].join(dc)
    return (text)


def check_condition(dd, cond):
    y = 1
    keys = list(dd[0].keys())
    keys_ = []
    correct = []
    for x in keys:
        if x in cond:
            keys_.append(str(x))
    # print(keys_)
    for xc in dd:
        # print(xc)
        condx = replace_all(cond, keys_, xc)
        # cond = cond.replace(t, xc[t])
        if (eval(condx)):
            correct.append(str(y))
        y += 1
        # print(list(xc.values()))
    return (correct)


print(check_condition(dd, "'gender'=='male' or 'name'=='jane'"))
'''
key=io and key=io
key=io or key=io
key!=io
key>5
key<5
nico#opon==jio and nico!=opon
'''
