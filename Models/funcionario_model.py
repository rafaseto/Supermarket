class Funcionario:
    def __init__(self,
                 nome,
                 cpf,
                 data_nascimento,
                 email,
                 telefone,
                 sexo,
                 login,
                 senha,
                 status):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.sexo = sexo
        self.login = login
        self.senha = senha
        self.status = status

    def __str__(self):
        return (f"Nome: {self.nome} / "
                f"CPF: {self.cpf} / "
                f"Telefone: {self.telefone} / " 
                f"Status: {self.status}")