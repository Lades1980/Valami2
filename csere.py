import re
regex = r"sheetNr=\"\d(.*?)\""

pattern=re.compile(regex)
i=0
ujf=open("UJ_BPHEHA.rsk","w",encoding="utf-8")
f=open("BPHEHA.rsk","r",encoding="utf-8")

k=0
sorok=f.readlines()
for sor in sorok:
    k=k+1
    talalat=pattern.finditer(sor)
    match=re.search(regex,sor)
    if match:
        if talalat:
            for v in talalat:    
                if v:
                    #print(v.group())
                    b=v.group()
                    csere="szöveg"
                    csere=b[0:9]+'MO_'+b[9:]
                    ujsor=re.sub(regex,csere,sor)
                    ujf.write(ujsor)
                    # print(ujsor)
                    # print(sor)
                    #print(b[0:9])
                    i=i+1
    else:
        ujf.write(sor)
ujf.close()
print(i)
print("Vége")