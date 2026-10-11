# 🎯 [DESAFIO #2] Codificador e Decodificador de Mensagens

![Python](https://shields.io)

Solução desenvolvida para o desafio de criptografia e segurança de dados. O projeto foi estruturado com foco em boas práticas de programação, segurança rígida no tratamento de dados e alta adaptabilidade.

## 📌 Sumário
- [📝 O Problema](#-o-problema)
- [🧩 Separação de Responsabilidades (Divisão do Problema)](#-separação-de-responsabilidades-divisão-do-problema)
- [💻 O Código Fonte](#-o-código-fonte)
- [🧠 Lógica de Programação Utilizada](#-lógica-de-programação-utilizada)
- [🏗️ Arquitetura e Decisões de Projeto](#️-arquitetura-e-decisões-de-projeto)
- [🚀 Como Executar o Projeto](#-como-executar-o-projeto)

---

## 📝 O Problema

Você foi contratado para criar um algoritmo que decodifica mensagens. Cada letra da mensagem foi substituída por uma letra 6 posições à frente. Além disso, os números na mensagem foram substituídos por números 3 posições à frente. Se ao somar a posição da letra/número for maior que o alfabeto ou o número de 0 a 9, você precisa recomeçar a lista.

Sua função de solução recebe uma string codificada. Crie o algoritmo que decodifique a mensagem e retorne a string correta.

---

## 🧩 Separação de Responsabilidades (Divisão do Problema)

1. **Filtro de Segurança e Acentuação:** Criação de regras de exceção para aceitar todas as letras acentuadas da língua portuguesa e barrar símbolos inválidos.
2. **Lógica de Codificação (Cifra de César):** Avanço matemático de caracteres para macronizar e mascarar as mensagens confidenciais da plataforma.
3. **Lógica de Decodificação (O Motor do Desafio):** Algoritmo reverso baseado em rotações circulares para recuperar a mensagem original correta.
4. **Interface e Validação de Fluxo (Menu):** Menu dinâmico de terminal que captura as intenções do usuário e blinda o sistema contra dados corrompidos.

---

## 💻 O Código Fonte

```python
# Função para codificar uma mensagem.
def codificador_mensagens(mensagem):
    mensagem_codificada = []

    try:
        for caractere in mensagem:

# 1. Filtro de Segurança e Acentuação
            # Lista de pontuações e acentos permitidos
            pontuacoes_permitidas = [
                '.', ',', '!', '?', '-', '_', ' ',
                'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü', 'ç',
                'Á', 'À', 'Ã', 'Â', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Õ', 'Ú', 'Ü', 'Ç'
            ]
    
# 2. Lógica de Codificação (Cifra de César)                        
            # Avança 6 posições no alfabeto para letras minúsculas
            if 'a' <= caractere <= 'z':
                posicao_letra_original = ord(caractere) - ord('a')
                posicao_letra_codificada = (posicao_letra_original + 6) % 26
                mensagem_codificada.append(chr(posicao_letra_codificada + ord('a')))

            # Avança 6 posições no alfabeto para letras maiúsculas
            elif 'A' <= caractere <= 'Z':
                posicao_letra_original = ord(caractere) - ord('A')
                posicao_letra_codificada = (posicao_letra_original + 6) % 26
                mensagem_codificada.append(chr(posicao_letra_codificada + ord('A')))
            
            # Avança 3 posições para números
            elif '0' <= caractere <= '9':
                posicao_numero_original = int(caractere)
                posicao_numero_codificado = (posicao_numero_original + 3) % 10
                mensagem_codificada.append(str(posicao_numero_codificado))

            # Mantém espaços, acentos e pontuações originais
            elif caractere in pontuacoes_permitidas:
                mensagem_codificada.append(caractere)   

            # Barra caracteres inválidos como #, $, %, etc.
            else:                                                   
                raise ValueError  

    except ValueError:
        print("Erro: Características Especiais não são permitidas, Digite apenas Letras e Números  ")
        return None

    return ''.join(mensagem_codificada)


# Função para decodificar uma mensagem codificada.
def decodificador_mensagens(mensagem):
    mensagem_original = []
    try:
        for caractere in mensagem:

# 1. Filtro de Segurança e Acentuação
            # Lista de pontuações e acentos permitidos
            pontuacoes_permitidas = [
                '.', ',', '!', '?', '-', '_', ' ',
                'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü', 'ç',
                'Á', 'À', 'Ã', 'Â', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Õ', 'Ú', 'Ü', 'Ç'
            ]

# 3. Lógica de Decodificação (O Motor do Desafio)              
            # Volta 6 posições no alfabeto para letras minúsculas
            if 'a' <= caractere <= 'z':
                posicao_letra_codificada = ord(caractere) - ord('a')
                posicao_letra_decodificada = (posicao_letra_codificada - 6) % 26
                mensagem_original.append(chr(posicao_letra_decodificada + ord('a')))

            # Volta 6 posições no alfabeto para letras maiúsculas
            elif 'A' <= caractere <= 'Z':
                posicao_letra_codificada = ord(caractere) - ord('A')
                posicao_letra_decodificada = (posicao_letra_codificada - 6) % 26
                mensagem_original.append(chr(posicao_letra_decodificada + ord('A')))
            
            # Volta 3 posições para números
            elif '0' <= caractere <= '9':
                posicao_numero_codificado = int(caractere)      
                posicao_numero_decodificado = (posicao_numero_codificado - 3) % 10
                mensagem_original.append(str(posicao_numero_decodificado))
            
            # Mantém espaços, acentos e pontuações originais
            elif caractere in pontuacoes_permitidas:
                mensagem_original.append(caractere)
            
            # Barra caracteres inválidos como #, $, %, etc.
            else:
                raise ValueError  

    except ValueError:
        print("Erro: Características Especiais não são permitidas, Digite apenas Letras e Números  ")
        return None
        
    return ''.join(mensagem_original)


# Função para receber as mensagens através de um Menu Interativo.
def menu():
    while True:
        print("\n--- CRIPTOGRAFIA ---")
        print("1. Codificar uma mensagem \n 2. Decodificar uma mensagem \n 3. Sair")
        
# 4. Interface e Validação de Fluxo (Menu)       
        try: 
            entrada_menu = input("Digite o número relativo a opção desejada : ")
        
            if entrada_menu == '1':
                texto = input("Digite a mensagem para CODIFICAR: ")
                resultado = codificador_mensagens(texto)

                # Garante que o resultado será resultante de uma mensagem totalmente válida.
                if resultado is not None: 
                    print(f"\nMensagem Codificada: {resultado}")
            
            elif entrada_menu == '2':
                texto = input("Digite a mensagem para DECODIFICAR: ")
                resultado = decodificador_mensagens(texto)

                # Garante que o resultado será resultante de uma mensagem totalmente válida.
                if resultado is not None:
                    print(f"\nMensagem Decodificada: {resultado}")
            
            elif entrada_menu == '3':
                print("Saindo do programa... Até logo!")
                break
                
            else:
                raise ValueError
    
        except ValueError:
            print("Erro: Digite apenas números que estão relacionados as opções do Menu.")

# Executa o menu
menu()
```

---

## 🧠 Lógica de Programação Utilizada

Para construir o algoritmo, usei conceitos fundamentais de lógica de programação que garantem que o sistema funcione bem, seja seguro e não quebre. Olha sob o que foi usado:

* **🛠️ Funções (`def`):** O código foi dividido em blocos de tarefas específicos. Duas funções puras cuidam exclusivamente do processamento da string e o `menu()` cuida da exibição e controle do fluxo. Isso mantém o sistema limpo e reutilizável.
* **🔄 Laço de Repetição Infinito (`while True`):** Usado no menu para criar um ciclo interativo contínuo, mantendo a aplicação ativa até que a opção de saída (Opção 3) quebre o laço de repetição.
* **🛡️ Tratamento de Erros (`try` e `except`):** Essa é a segurança do código! O bloco tenta validar os dados do usuário. Caso encontre um caractere não autorizado ou uma opção inexistente do menu, o `except` captura a falha (`ValueError`), exibe um alerta amigável na tela e retorna `None` para evitar travamentos indesejados (*crashes*).
* **🚦 Condicionais (`if` / `elif` / `else`):** Utilizados para classificar de forma precisa os dados do loop, descobrindo se o caractere atual deve girar no alfabeto, nos números ou ignorar o avanço (pontuações e acentos).
* **🧮 Operador de Resto da Divisão (`%`):** O coração da criptografia! Usar o módulo no Python garante que as listas de caracteres sejam circulares, fazendo com que o índice dê a volta e "recomeça a lista" automaticamente caso os limites sejam extrapolados.

---

## 🏗️ Arquitetura e Decisões de Projeto

Embora a **Cifra de César** seja um algoritmo puramente didático e inadequado para segurança em produção de sistemas reais de mercado devido à sua simplicidade matemática, o diferencial deste projeto está no **desenho arquitetural do código**. 

### 🔌 Modularidade e Acoplamento Zero
O projeto foi estruturado de forma a separar completamente a **Lógica de Negócio** da **Interface com o Usuário**:
* **Funções Puras:** As funções `codificador_mensagens` e `decodificador_mensagens` não dependem do terminal. Elas recebem parâmetros limpos e retornam strings limpas (ou `None`). Isso significa que a interface gráfica ou de linha de comando (`menu()`) pode ser totalmente substituída ou descartada sem que seja necessário alterar uma única linha do motor lógico.
