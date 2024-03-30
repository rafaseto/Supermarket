class FuncionarioView:
    def mostrar_detalhes(self, funcionario):
        print("Detalhes do funcionário:")
        print("------------------------")
        print(f"Nome: {funcionario.nome}")
        print(f"CPF: {funcionario.cpf}")
        print(f"Data de nascimento: {funcionario.data_nascimento}")
        print(f"E-mail: {funcionario.email}")
        print(f"Telefone: {funcionario.telefone}")
        print(f"Sexo: {funcionario.sexo}")
        print(f"Login: {funcionario.login}")
        print(f"Status: {funcionario.status}") 
