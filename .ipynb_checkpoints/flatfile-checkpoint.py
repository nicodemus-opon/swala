import zipfile
import os
import json
from shutil import copyfile
class flat:
    def __init__(self, directory, password=""):
      self.directory = directory
      self.password = password
      self.db=str(os.getcwd())+"\\"+directory
      self.connect()

    def create(self,cmd):
        bits=cmd.split(">")
        out=bits[0]
        loc=self.db+"\\"+out+"\\"
        if not os.path.exists(loc):
            os.makedirs(loc)
        pos=len([str(name) for name in os.listdir(loc)])
        loc=self.db+"\\"+out+"\\"+str(pos)+".f"
        f= open(loc,"w+")
        f.write("")
        f.close() 
        with open(loc, 'w+') as output:
            output.write(bits[1])
        mess="created data at "+bits[0]
        return(mess)
    def read(self,cmd):
        bits=cmd.split("<")
        out=bits[0]
        full_data=[]
        loc=self.db+"\\"+out+"\\"
        pos=len([str(name) for name in os.listdir(loc)])
        if bits[1]=="*":
            for x in range(pos):
                ji=self.db+"\\"+out+"\\"+str(x)+".f"
                try:
                    with open(ji, 'r') as output:
                        xc=output.read()
                        xc=xc.strip()
                        ni=xc.split(",")
                        full_data.append(ni)
                except Exception as e:
                    break
        return(full_data)
    def update(cmd):
        bits=cmd.split(">")
        out=bits[0]
        loc=self.db+"\\"+out+"\\"
        if not os.path.exists(loc):
            os.makedirs(loc)
        pos=len([str(name) for name in os.listdir(loc)])
        loc=self.db+"\\"+out+"\\"+str(pos)+".f"
        f= open(loc,"w+")
        f.write("")
        f.close() 
        with open(loc, 'w+') as output:
            output.write(bits[1])
        mess="created data at "+bits[0]
    def delete(self,cmd):
        pass
    
    def filer(self,cmd):
        bits=cmd.split("::")
        out=bits[0]
        loc=self.db+"\\"+out+"\\"
        if not os.path.exists(loc):
            os.makedirs(loc)
        pos=len([str(name) for name in os.listdir(loc)])
        loc=self.db+"\\"+out+"\\"+str(pos)+".f"
        f= open(loc,"w+")
        f.write("")
        f.close()
        locr=self.db+"\\"+out+"\\contains_file.f"
        f= open(locr,"w+")
        f.write("")
        f.close()
        #print(bits[1])
        #return(0)
        comp=bits[1].split("\\")
        cv=comp[-1]
        locx=self.db+"\\"+out+"\\"+cv
        with open(loc, 'w+') as output:
            full_text="map:"+str(pos)+":"+","+bits[2]
            output.write(full_text)
        copyfile(bits[1], locx)
        mess="created file at "+bits[0]

    def connect(self):
        d=self.directory
        d=d+".zip"
        dh=d.split(".")
        dc=dh[0]
        #print(d)
        xc=str(os.getcwd())+"\\"+dc
        with zipfile.ZipFile(d, 'r') as zip_ref:
            zip_ref.extractall(xc)
        #print(xc)
        return(0)

    def exec(self,command=""):
        task=command.split(">")
        if len(task)==2:
           return(self.create(command))
        if len(task)>2:
            return(self.update(command))
        task=command.split("<")
        if len(task)==2:
            return(self.read(command))
        if "!" in command:
            return(self.delete(command))
        if "::" in command:
            return(self.filer(command))
        return("UH-OH :( unrecognised command")
