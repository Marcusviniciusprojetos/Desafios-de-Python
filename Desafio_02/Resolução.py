# 🎯 [DESAFIO #2] Codificador e Decodificador de Mensagens

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
