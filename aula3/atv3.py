lista_de_usuarios = []
for i in range(5):
    usuario = {
        "nome": str(input("Digite o nome do usuário: ")),
        "cpf": str(input("Digite o cpf do usuário: ")),
        "rg": str(input("Digite o rg do usuário: ")),
        "serie": str(input("Digite o serie do usuário: ")),
        "endereço": str(input("Digite o endereço do usuário: "))
    }
    lista_de_usuarios.append(usuario)

print(lista_de_usuarios)





[
    {
    'nome': 'Joao',
    'cpf': '1',
    'rg': '1',
    'serie': '1',
    'endereço': '1'
    },
    {
    'nome': 'Maria',
    'cpf': '2',
    'rg': '2',
    'serie': '2',
    'endereço': '2'
    },
    {'nome': 'Ana',
     'cpf': '3',
     'rg': '3',
     'serie': '3',
     'endereço': '3'
     }, 
     {'nome': 'Antonio',
      'cpf': '4',
      'rg': '4',
      'serie': '4',
      'endereço': '4'
      },
      {'nome': 'Abel',
       'cpf': '5',
       'rg': '5',
       'serie': '5',
       'endereço': '5'
        }
]