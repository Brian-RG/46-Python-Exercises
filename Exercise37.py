import Functions
path="file.txt"
new="Nuevo.txt"
if Functions.archivo_valido(path):
    first=open(path,'r')
    second=open(new,'w')
    first_lines=first.readlines()
    line_cont=0
    linea=""
    for fl in first_lines:
        line_cont=int(line_cont)
        line_cont+=1
        line_cont=str(line_cont)
        linea=line_cont+") "+fl+'\n'
        second.write(linea+"\n")
