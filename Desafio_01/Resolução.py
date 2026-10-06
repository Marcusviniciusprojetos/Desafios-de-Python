#🎯 [DESAFIO #1] Contador de Enquetes


# 1. Criação das Enquetes 

from collections import Counter


def Respostas_user1():

    print("💡Enquete de Ideias e Sugestões")

    print("1. • Excesso de reuniões de alinhamento. \n2. • Comunicação interna (informações/arquivos). \n3. • Ferramentas desatualizadas (sistemas lentos ou softwares que não atendem mais). \n4. • Melhoria nos equipamentos e ferramentas físicas/digitais.")

# 2. Simulando Minha Resposta Como Usuário 
    while True:
        try:
            opcoes_validas = ["1", "2", "3", "4"]

            Entrada_user1 = input("Qual destes processo ou tarefa consome mais o seu tempo hoje e poderia ser simplificado?\nDigite o número relativo a sua escolha.").strip()
            
            int(Entrada_user1)
            
            if Entrada_user1 in opcoes_validas:
                return Entrada_user1
                
            else:
                print("Opção inválida, Digite apenas os números relativos a Enquete")

        except ValueError:
            print("Erro:Letras/símbolos não são permitidos! \n Digite apenas os números relativos a Enquete. ")

# 3. algoritmo que recebe a lista de respostas.

def Respostas_all_users():

# 3.1 Minha Resposta 
    user1 = Respostas_user1()

# 3.2 Respostas Dos Outros Usuários
    
    user2 = "3"
    user3 = "2"
    user4 = "1"
    user5 = "4"
    user6 = "2"
    user7 = "3"
    user8 = "4"
    user9 = "1"

    Lista_respostas = [user1,user2,user3,user4,user5,user6,user7,user8,user9]

#  4. resposta mais votada e a quantidade de votos.

    contador = Counter(Lista_respostas)

    mais_votada, quantidade = contador.most_common(1)[0]

    if mais_votada == "1":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo :Excesso de reuniões de alinhamento. Obteve mais votos com: ({quantidade}) números de votos.")

    if mais_votada == "2":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo :Comunicação interna (informações/arquivos). Obteve mais votos com: ({quantidade}) números de votos.")

    if mais_votada == "3":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo :Ferramentas desatualizadas (sistemas lentos ou softwares que não atendem mais). Obteve mais votos com: ({quantidade}) números de votos.")

    if mais_votada == "4":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo :Melhoria nos equipamentos e ferramentas físicas/digitais. Obteve mais votos com: ({quantidade}) números de votos.")


Respostas_all_users()
