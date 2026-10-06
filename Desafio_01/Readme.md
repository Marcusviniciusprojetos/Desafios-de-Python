#  🎯[DESAFIO #1] Contador de Enquetes

![Python](https://shields.io)


Solução desenvolvida para o desafio de computação de votos da plataforma de enquetes da **Empresa TMJ**. O projeto foi estruturado com foco em boas práticas de programação, segurança rígida no tratamento de dados e alta adaptabilidade.

## 📌 Sumário
- [📝 O Problema](#-o-problema)
- [🧩 Separação de Responsabilidades (Divisão do Problema)](#-separação-de-responsabilidades-divisão-do-problema)
- [💻 O Código Fonte](#-o-código-fonte)
- [🧠 Lógica de Programação Utilizada](#-lógica-de-programação-utilizada)
- [🏗️ Arquitetura e Decisões de Projeto](#️-arquitetura-e-decisões-de-projeto)
- [🚀 Como Executar o Projeto](#-como-executar-o-projeto)

---

## 📝 O Problema

A empresa TMJ tem uma plataforma que gera enquetes para seus usuários. Sua tarefa é desenvolver um algoritmo que recebe a lista de respostas e retorne a resposta mais votada e a quantidade de votos.

O seu método precisa retornar uma lista onde a primeira posição é a resposta mais selecionada e a segunda posição a quantidade.

---

## 🧩 Separação de Responsabilidades (Divisão do Problema)

1. **Criação das Enquetes:** Definição clara das opções disponíveis para a votação.
2. **Simulando Minha Resposta Como Usuário:** Interface de terminal para capturar a resposta com validações ativas de segurança.
3. **Algoritmo que recebe a lista de respostas:** Agrupamento do voto atual com dados simulados de outros usuários.
4. **Resposta mais votada e a quantidade de votos:** Processamento da lista para encontrar o vencedor e exibir o resultado formatado.

---

## 💻 O Código Fonte

```python
from collections import Counter

# 1. Criação das Enquetes
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
            print("Erro: Letras/símbolos não são permitidos! \n Digite apenas os números relativos a Enquete. ")

# 3. Algoritmo que recebe a lista de respostas.
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

    Lista_respostas = [user1, user2, user3, user4, user5, user6, user7, user8, user9]

    # 4. Resposta mais votada e a quantidade de votos.
    contador = Counter(Lista_respostas)
    mais_votada, quantidade = contador.most_common(1)[0]

    if mais_votada == "1":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo: Excesso de reuniões de alinhamento. Obteve mais votos com: ({quantidade}) números de votos.")
    if mais_votada == "2":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo: Comunicação interna (informações/arquivos). Obteve mais votos com: ({quantidade}) números de votos.")
    if mais_votada == "3":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo: Ferramentas desatualizadas (sistemas lentos ou softwares que não atendem mais). Obteve mais votos com: ({quantidade}) números de votos.")
    if mais_votada == "4":
        print(f"Na Enquete sobre o processo ou tarefa que consome mais tempo: Melhoria nos equipamentos e ferramentas físicas/digitais. Obteve mais votos com: ({quantidade}) números de votos.")

# Execução do sistema
Respostas_all_users()
```

---

## 🧠 Lógica de Programação Utilizada

Para construir o algoritmo, usei conceitos fundamentais de lógica de programação que garantem que o sistema funcione bem, seja seguro e não quebre. Olha só o que foi usado:

* **🛠️ Funções (`def`):** O código foi dividido em blocos de tarefas específicos. Uma função cuida apenas de pegar o voto do usuário e a outra cuida de juntar todos os votos e fazer a contagem. Isso deixa o código limpo e organizado.
* **🔄 Laço de Repetição Infinito (`while True`):** Usado para prender o usuário em um "loop" até que ele digite uma opção válida. O programa só avança quando a escolha for correta.
* **🛡️ Tratamento de Erros (`try` e `except`):** Essa é a segurança do código! O `try` tenta transformar a resposta em número. Se o usuário digitar uma letra, o `except` entra em ação na hora, captura o erro (`ValueError`), avisa que letras não são permitidas e impede que o programa feche sozinho (sofra um crash).
* **🚦 Condicionais (`if`):** Usados para verificar se o número digitado está entre as opções válidas (1, 2, 3 ou 4) e, no final, para descobrir qual texto exibir na tela dependendo de quem foi o grande vencedor.
* **📦 Biblioteca Nativa (`Counter`):** Em vez de criar um código gigante para contar voto por voto, importei uma ferramenta pronta do Python chamada `Counter` (da biblioteca `collections`). Ela recebe a lista de respostas e faz a contagem de forma ultra rápida e eficiente.

---

## 🏗️ Arquitetura e Decisões de Projeto

O grande diferencial deste projeto não é apenas resolver o algoritmo proposto, mas sim a forma como ele foi desenhado. O código foi estruturado pensando em cenários reais de mercado, focando em duas frentes: **Adaptabilidade** e **Segurança**.

### 🔌 Adaptabilidade para Banco de Dados e Login
O código foi modularizado para permitir que o projeto cresça sem a necessidade de refatorar a lógica principal:
* **Fácil Integração com BD:** A lista de respostas e o input do usuário foram isolados. Se amanhã decidirmos plugar um banco de dados (como PostgreSQL, MySQL ou MongoDB), a transição será imediata. O sistema estará pronto tanto para obter a lista de votos quanto para salvar o input do usuário diretamente nas tabelas.
* **Pronto para Autenticação (Login):** Graças à separação de funções, se houver a necessidade de criar uma camada de Login ou controle de sessão antes da votação, ela pode ser acoplada no início do fluxo sem gerar conflitos ou impactar o motor de contagem. O sistema foi estruturado de forma modular para que seja extremamente simples. Além disso, o input foi blindado de uma forma que caso este código seja usado em um banco de dados no futuro não tem como sofrer ataques de SQL Injection, garantindo a segurança desde o início.

### 🛡️ Proteção de Dados
Através do uso do bloco `try/except`, o sistema valida rigorosamente a entrada do usuário. Isso impede o envio de dados corrompidos ou maliciosos, garantindo a integridade do sistema.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou salve o código fonte em um arquivo chamado `main.py`.
3. Execute o programa usando o terminal:
   ```bash
   python main.py
   ```
