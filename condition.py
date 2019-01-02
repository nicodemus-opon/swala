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


def check_condition(dd, cond):
    x = 1
    keys = list(dd[0].keys())
    keys_ = []
    for x in keys:
        if x in cond:
            keys_.append(str(x))
    print(keys_)
    for xc in dd:
        # print(xc)
        for t in keys_:
            print(xc[t])
            dc = cond.split(t)
            print(dc)
            condx = xc[t].join(dc)
            # cond = cond.replace(t, xc[t])
        print(condx)
        # print(list(xc.values()))


print(check_condition(dd, "gender==male and name==jane"))
'''
key=io and key=io
key=io or key=io
key!=io
key>5
key<5
nico#opon==jio and nico!=opon
'''
