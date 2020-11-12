import os



#=====================================================================================================



#=====================================================================================================



class Person:



    def __init__(self, name, cpf,identificador ,email, user_password):

        self.name = name

        self.cpf = cpf

        self.identificador  = identificador 

        self.email = email

        self.user_password = user_password



    def get_name(self):

        return self.name



    def get_cpf(self):

        return self.cpf



    def get_identificador(self):

        return self.identificador



    def get_email(self):

        return self.email



    def get_user_password(self):

        return self.user_password



    def print_profile(self):

        while True:

            print("=============================== PERFIL ===============================")

            print(f"\n Nome: {self.get_name()}\n CPF: {self.get_cpf()}\n Id: {self.get_identificador()}\n Email: {self.get_email()}\n Senha: {self.get_user_password()}\n ")

            print('=' * 70)



            if(int(input(" Digite [ 0 ] Sair    [ 1 ] Continuar\n Escolha: ")) == 0):

                os.system('cls') or None

                break

            

            else:

                os.system('cls') or None

                continue



#=====================================================================================================



#=====================================================================================================



class Paciente :



    def __init__ (self,name,cpf,endereco,sexo):

        self.name = name

        self.cpf = cpf

        self.endereco  = endereco

        self.sexo = sexo



    def get_name(self):

        return self.name



    def get_cpf(self):

        return self.cpf



    def get_endereco(self):

        return self.endereco



    def get_sexo(self):

        return self.sexo

        

#=====================================================================================================



class Administrator(Person):

    employees = list()



    def __init__(self, name, cpf,identificador ,email, user_password):

        super().__init__(name, cpf,identificador ,email, user_password)

        self.job_title = 'Adm'



    def get_job(self):

        return self.job_title



    @classmethod

    def register_asst(cls,conexao,cnx):
        
        print("=" * 30,end='')
        print(" CADASTRO ",end='')
        print("=" * 30)
        

        asst = Assistent(input("\nNome: "),input("CPF: "),input("Id: "),input("Email: "), input("Senha: "))



        nome = asst.get_name()

        cpf = asst.get_cpf() 

        identificador = asst.get_identificador()

        job_title = asst.get_job()

        email = asst.get_email()

        senha = asst.get_user_password()

        conexao.execute("INSERT INTO Funcionarios(Name,CPF,ID,job_title,email,user_password) VALUES(%s,%s,%s,%s,%s,%s)",(nome,cpf,identificador,job_title,email,senha))

        cnx.commit()



    @classmethod

    def remove_asst(cls,conexao,cnx):
        print("=" * 30,end='')
        print(" REMOVER ",end='')
        print("=" * 30)

        cpf = input("Cite o cpf do assistente que você quer remover:")

        frase =f'Delete from Funcionarios where CPF = {cpf}'

       

        conexao.execute(frase)

        cnx.commit()



    @classmethod

    def check_asst(cls,conexao,cnx):
        print("=" * 30,end='')
        print(" FUNCIONÁRIOS ",end='')
        print("=" * 30)

        conexao.execute("select * from Funcionarios")

        for l in conexao.fetchall():

            print (l)



        cnx.commit()



#=====================================================================================================



#=====================================================================================================       



class Assistent(Person):



    def __init__(self,name, cpf,identificador ,email, user_password):

        super().__init__(name, cpf,identificador ,email, user_password)

        self.job_title = 'Asst'



    def get_job(self):

        return self.job_title



    @classmethod

    def add_promptuary(cls,conexao,cnx):

        self.promptuary = Promptuary( input("Grupo: "),input("Origem: "),input("Modalidade: "),input("Doença: "),



                                        input("Status: "),input("Familiar Responsável: "),input("TR Responsável: "))





        



class Secretary(Person):



    def __init__(self,name, cpf,identificador ,email, user_password):

        super().__init__(name, cpf,identificador ,email, user_password)

        self.job_title = 'Secretary'



    def get_job(self):

        return self.job_title



    def add_cadastro(cls,conexao,cnx):

        pessoa = Paciente(input("Name:"),input("Cpf:"),input("Endereco:"),input("Sexo:"))

        conexao.execute('INSERT INTO CADASTRO VALUES (%s,%s,%s,%s)', (pessoa.get_name(), pessoa.get_cpf(),pessoa.get_endereco(),pessoa.get_sexo()))

        cnx.commit()



#=====================================================================================================



#=====================================================================================================



class Promptuary:

    def __init__(self,group,origin,mode,illness,Tr_Responsable,Family_Responsable):

        self.group = group

        self.origin = origin 

        self.mode = mode

        self.illness = illness

        self.status = True

        self.Tr_Responsable= Tr_Responsable

        self.Family_Responsable =Family_Responsable

       

    #GETTERS



    def get_group(self):

        return self.group



    def get_origin(self):

        return self.origin



    def get_mode(self):

        return self.mode



    def get_status (self):

        return True



    def get_illness(self):

        return self.illness



    def get_Tr_Responsable(self):

        return self.Tr_Responsable



    def get_Family_Responsable(self):

        return self.Family_Responsable
