def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def create_db(name):
    nam = name
    name += ".zip"
    zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)
    zipdir('temp', zipf)
    zipf.close()
    hu = {"success": "created database " + nam}
    print(hu)


if __name__ == "__main__":
    import flatfile
    import zipfile
    import os
    import json

    print("SWALA CLI")
    xc = ""
    n = 1
    zs = flatfile.flat("nico")
    zs.connect()
    while xc != "quit":
        xc = input(":" + str(n) + ":")
        xc = xc.lower()
        x = xc.split(" ")
        if x[0] == "init":
            create_db(x[1])
            break
        n += 1
        if xc == "":
            # print("")
            continue
        ii = zs.exec(xc)
        # print(ii)
        p = str(ii)
        p = p.replace("'", '"')
        parsed = json.loads(p)
        print(json.dumps(parsed, indent=4, sort_keys=True))
