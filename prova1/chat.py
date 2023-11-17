#! /bin/env python3
import re


intent_dict = {
    r"\b(?:(?:atualizar)\s(?:pagamento))": "pagamento",
    r"\b(?:(?:acompanhar)\s(pedido))": "pedido",    
}

action_dict = {
    "pagamento": "Aqui estão as novas opções de pagamentos!",
    "pedido": "Seu pedido está a 3 anos preso em Curitiba! :)",
}
sair = False
while(sair == False):
    command = input("Digite o seu comando: ")
    if (command == 'sair'):
        sair = True
    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if (str(groups) == "['atualizar pagamento']"):
            print (action_dict['pagamento'])
        else if (str(groups) == "['acompanhar pedido']"):
            print (action_dict['pedido'])
    print()