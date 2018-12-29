def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            
def create_db(name):
    nam=name
    name+=".zip"
    zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)
    zipdir('temp', zipf)
    zipf.close()
    print("created database "+nam)

if __name__=="__main__":
    import flatfile
    import zipfile
    import os
    print("FLATFILE CLI")
    print("")
    xc=""
    n=0
    zs=flatfile.flat("nico")
    zs.connect()
    while xc!="quit":
        xc=input(":"+str(n)+":")
        xc=xc.lower()
        x=xc.split(" ")
        if x[0]=="init":
            create_db(x[1])
            break
        n+=1
        print(zs.exec(xc))
