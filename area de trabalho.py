disciplinas = ["Algoritmos","Segurança","Desenv.Web"]
turma =[]

def cadastro_alunos (nome,matricula,idade):
    aluno ={
    "nome":nome,
    "matricula":matricula,
    "idade":idade,
    "notas":[[],[],[]]    
        
    }

    turma.append(aluno)
def encontra_alunos(matricula):
    for aluno in turma:
        if aluno["matricula"]== matricula:
            return aluno
    return None
    
    
def inicializa_notas(matricula):
    aluno = encontra_alunos(matricula)
    for notas_disciplina in aluno["notas"]:
        for item_nota in range (0,5):
            notas_disciplina.append(0)

def insere_Notas(matricula,cod_disc):
    aluno= encontra_alunos (matricula)
    for nota in  range (0,5):
        aluno["notas"] [cod_disc][nota] = float
        nota = float(input("informe a nota:"))
        
cadastro_alunos ("açucena",123,19)
inicializa_notas(123)
cadastro_alunos ("lucas",425,20)
inicializa_notas(425)


#print (encontra_alunos(123))
#
# 
for aluno in turma :
    print (aluno)
    

açucena ={
 "matricula":123,
 "nome":"Açucena",
 "idade":19,
 "notas":[[10],[10],[10],[10]]
 
}  
    
 
lucas ={
  "matricula":425,
  "nome":"lucas",
  "idade":20,
  "notas":[[5],[8],[10]]   
   
        
     
     
 }   
