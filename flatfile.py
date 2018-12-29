import zipfile
import os
import json
from shutil import copyfile
import os.path as path
class flat:
    def __init__(self, directory, password=""):
      self.directory = directory
      self.password = password
      self.db=str(path.join(str(os.getcwd()),directory))
      self.connect()

    def check_condition(self,di,ju):
        for x in range(pos):
            x+=1
            ji=self.db+"\\"+out+"\\"+str(x)+".f"
            jir=self.db+"\\"+out+"\\"+"schema.f"
            try:
                with open(ji, 'r') as output:
                    xc=output.read()
                    xc=xc.strip()
                    ni=xc.split(",")
                    with open(jir, 'r') as ou:
                        xs=ou.read()
                        xs=xs.strip()
                        #print(xs)
                        if xs=="auto":
                            auto=True
                        else:
                            list_of_keys=xs.split(",")
                            #print(list_of_keys)
                    #for x in ni:
                    dd={}
                    if auto==True:
                        nn=len(ni)
                        ft=list(range(nn))
                        for ll in ft:
                            dd[str(ll)]=ni[ll]
                        full_data.append(dd)
                    else:
                        ft=list_of_keys
                        gg=list(range(len(ft)))
                        kkk=0
                        for ll in ft:
                            dd[str(ll)]=ni[kkk]
                            kkk+=1
                        full_data.append(dd)
            except Exception as e:
                #print(e)
                break

    def create(self,cmd):
        bits=cmd.split(">")
        out=bits[0]
        loc=self.db+"\\"+out+"\\"
        oo=self.db+"\\"+out+"\\"
        if not os.path.exists(loc):
            os.makedirs(loc)
            kk=loc+"schema.f"
            f= open(kk,"w+")
            f.write("auto")
            f.close()

        yu=1
        kk=len(bits)
        while yu<len(bits):
            try:
                pos=len([str(name) for name in os.listdir(oo)])
                loc=self.db+"\\"+out+"\\"+str(pos)+".f"
                f= open(loc,"w+")
                f.write("")
                f.close()
                with open(loc, 'w+') as output:
                    output.write(bits[yu])
                    yu+=1
            except Exception as e:
                print(e)
                break
        mess={"success":"created data at "+bits[0]}
        return(mess)
    
    def read(self,cmd):
        bits=cmd.split("<")
        out=bits[0]
        full_data=[]
        loc=path.join(self.db,out,)
        #print(loc)
        pos=len([str(name) for name in os.listdir(loc)])
        list_of_keys=[]
        auto=False
        if bits[1]=="*":
            for x in range(pos):
                x+=1
                ji=path.join(self.db,out,str(x)+".f")
                jir=path.join(self.db,out,"schema.f")
                try:
                    with open(ji, 'r') as output:
                        xc=output.read()
                        xc=xc.strip()
                        ni=xc.split(",")
                        with open(jir, 'r') as ou:
                            xs=ou.read()
                            xs=xs.strip()
                            #print(xs)
                            if xs=="auto":
                                auto=True
                            else:
                                list_of_keys=xs.split(",")
                                #print(list_of_keys)
                        #for x in ni:
                        dd={}
                        if auto==True:
                            nn=len(ni)
                            ft=list(range(nn))
                            for ll in ft:
                                dd[str(ll)]=ni[ll]
                            full_data.append(dd)
                        else:
                            ft=list_of_keys
                            gg=list(range(len(ft)))
                            kkk=0
                            for ll in ft:
                                dd[str(ll)]=ni[kkk]
                                kkk+=1
                            full_data.append(dd)
                except Exception as e:
                    #print(e)
                    break
        else:
            gy=bits[1].split(",")
        return(full_data)
    
    def update(self,cmd):
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
    
    def scheme(self,cmd):
        bits=cmd.split(":")
        out=bits[0]
        loc=self.db+"\\"+out+"\\"+"schema.f"
        f= open(loc,"w+")
        f.write(bits[1])
        f.close()
        tt="created scheme at "+bits[0]
        return({"success":tt})
    
    def delete(self,cmd):
        pass
    
    def filer(self,cmd):
        bits=cmd.split("$")
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

    def custom(self,cmd):
        resp={}
        if cmd=="tables":
            nico=os.listdir(self.db)
            for x in nico:
                d=path.join(self.db,x)
                resp[str(x)]=len(os.listdir(d))-1
            return(resp)
        resp["error"]="unknown command"
        return(resp)
            

    def exec(self,command=""):
        task=command.split(">")
        if len(task)>1:
           return(self.create(command))
        if len(task)==78:
            return(self.update(command))
        task=command.split("<")
        if len(task)==2:
            return(self.read(command))
        if "!" in command:
            return(self.delete(command))
        if "$" in command:
            return(self.filer(command))
        if ":" in command:
            return(self.scheme(command))
        return(self.custom(command))
