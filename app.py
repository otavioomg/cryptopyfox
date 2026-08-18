from cryptography.fernet import Fernet
import os

opcao_inicio = int(input("Bem-vindo ao Cryptopyfox, a raposa da criptografia!\nOBS:Ignore o \"b''\" quando for usar alguns comandos via terminal,pois quando o programa é usado na criptografia via terminal, ele criptografa de forma diferente do que arquivo txt\nEscolha umas das opções abaixo para começar a usar a ferramenta de criptografia e descriptografia de arquivos e textos.\n1-Importar uma chave existente\n2-Gerar uma nova chave\n3-Usar a chave padrão do programa (chave.key)\nOpção: "))

if opcao_inicio == 1:
    chaveimportada = input("Coloque a chave existente: ")

    print("Essa é a chave importada(ignore o \"b''\" no terminal): \n",chaveimportada)

    fernet = Fernet(chaveimportada)
    while True:
        os.system("figlet Cryptopyfox | lolcat && echo '                            By: Otavio OMG Dev' | lolcat && cowsay -f fox Bem-vindo a criptografia da Cryptopyfox, a raposa da criptografia! | lolcat")
        opcao = int(input('Escolhas as suas opções:\n1-Criptografar no arquivo crypt.txt\n2-Descriptografar arquivo crypt.txt\n3-Criptografar no próprio terminal\n4-Descriptografar no próprio terminal(Pode ocorrer erros)\n5-Criptografar arquivo específico\n6-Descriptografar arquivo específico\n7-Criar um arquivo de texto criptografado\nMais opções em breve...\nQual opção deseja escolher: '))

        if opcao == 1:
            texto = input('Digite o conteúdo a ser criptografado: ')
            with open('crypt.txt', 'wb') as text:
                text.write(texto.encode())
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()

            criptografado = fernet.encrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 2:
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 3:
            textforcrypt = input('Digite o conteúdo a ser criptografado: ')
            criptografado = fernet.encrypt(textforcrypt.encode())
            print(criptografado)
        elif opcao == 4:
            textfordescrypt = input('Digite o conteúdo a ser descriptografado: ')
            descriptografado = fernet.decrypt(textfordescrypt.encode())
            print(descriptografado)
            print("OBS: Essa ferramenta está em testes, ela não aceita letras com acentos, recomendo usar a opção 2 para descriptografar no arquivo crypt.txt, cole a mensagem criptografada dentro do arquivo crypt.txt")
        elif opcao == 5:
            arquivo = input('Digite o nome do arquivo a ser criptografado (com extensão): ')
            os.system = arquivo
            with open(arquivo, 'rb') as file:
                conteudo = file.read()
            criptografado = fernet.encrypt(conteudo)
            print(criptografado)
            criptografado = fernet.encrypt(conteudo)

            with open(arquivo, 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 6:
            arquivo = input('Digite o nome do arquivo a ser descriptografado (com extensão): ')
            with open(arquivo, 'rb') as file:
                conteudo_crypt = file.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open(arquivo, 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 7:
            nomedoarquivo_txt = input("Digite o nome do arquivo de texto (com extensão) que deseja criar: ")
            os.system(f"touch {nomedoarquivo_txt}.txt")
            conteudo = input("Digite o conteúdo que deseja adicionar ao arquivo: ")
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as text:
                        text.write(conteudo.encode())
            with open(f'{nomedoarquivo_txt}.txt', 'rb') as textcrypt:
                        conteudo_crypt = textcrypt.read()
            
            criptografado = fernet.encrypt(conteudo_crypt)
            
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as arquivo_criptografado:
                        arquivo_criptografado.write(criptografado)
            print(criptografado)
            print(f"Arquivo '{nomedoarquivo_txt}' criado com sucesso!") 
        else:
            print('Opção inválida. Por favor, escolha as opções de 1 a 7.')
            break
if opcao_inicio == 2:
    chave_gerada = Fernet.generate_key()

    print("Essa é a chave gerada(ignore o \"b''\" no terminal): \n",chave_gerada)

    fernet = Fernet(chave_gerada)

    while True:
        os.system("figlet Cryptopyfox | lolcat && echo '                            By: Otavio OMG Dev' | lolcat && cowsay -f fox Bem-vindo a criptografia da Cryptopyfox, a raposa da criptografia! | lolcat")
        opcao = int(input('Escolhas as suas opções:\n1-Criptografar no arquivo crypt.txt\n2-Descriptografar arquivo crypt.txt\n3-Criptografar no próprio terminal\n4-Descriptografar no próprio terminal(Pode ocorrer erros)\n5-Criptografar arquivo específico\n6-Descriptografar arquivo específico\n7-Criar um arquivo de texto criptografado\nMais opções em breve...\nQual opção deseja escolher: '))

        if opcao == 1:
            texto = input('Digite o conteúdo a ser criptografado: ')
            with open('crypt.txt', 'wb') as text:
                text.write(texto.encode())
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()

            criptografado = fernet.encrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 2:
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 3:
            textforcrypt = input('Digite o conteúdo a ser criptografado: ')
            criptografado = fernet.encrypt(textforcrypt.encode())
            print(criptografado)
        elif opcao == 4:
            textfordescrypt = input('Digite o conteúdo a ser descriptografado: ')
            descriptografado = fernet.decrypt(textfordescrypt.encode())
            print(descriptografado)
            print("OBS: Essa ferramenta está em testes, ela não aceita letras com acentos, recomendo usar a opção 2 para descriptografar no arquivo crypt.txt, cole a mensagem criptografada dentro do arquivo crypt.txt")
        elif opcao == 5:
            arquivo = input('Digite o nome do arquivo a ser criptografado (com extensão): ')
            os.system = arquivo
            with open(arquivo, 'rb') as file:
                conteudo = file.read()
            criptografado = fernet.encrypt(conteudo)
            print(criptografado)
            criptografado = fernet.encrypt(conteudo)

            with open(arquivo, 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 6:
            arquivo = input('Digite o nome do arquivo a ser descriptografado (com extensão): ')
            with open(arquivo, 'rb') as file:
                conteudo_crypt = file.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open(arquivo, 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 7:
            nomedoarquivo_txt = input("Digite o nome do arquivo de texto (com extensão) que deseja criar: ")
            os.system(f"touch {nomedoarquivo_txt}.txt")
            conteudo = input("Digite o conteúdo que deseja adicionar ao arquivo: ")
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as text:
                        text.write(conteudo.encode())
            with open(f'{nomedoarquivo_txt}.txt', 'rb') as textcrypt:
                        conteudo_crypt = textcrypt.read()
            
            criptografado = fernet.encrypt(conteudo_crypt)
            
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as arquivo_criptografado:
                        arquivo_criptografado.write(criptografado)
            print(criptografado)
            print(f"Arquivo '{nomedoarquivo_txt}' criado com sucesso!") 
        else:
            print('Opção inválida. Por favor, escolha as opções de 1 a 7.')
            break
if opcao_inicio == 3:
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()

    fernet = Fernet(chave)
    while True:
        os.system("figlet Cryptopyfox | lolcat && echo '                            By: Otavio OMG Dev' | lolcat && cowsay -f fox Bem-vindo a criptografia da Cryptopyfox, a raposa da criptografia! | lolcat")
        opcao = int(input('Escolhas as suas opções:\n1-Criptografar no arquivo crypt.txt\n2-Descriptografar arquivo crypt.txt\n3-Criptografar no próprio terminal\n4-Descriptografar no próprio terminal(Pode ocorrer erros)\n5-Criptografar arquivo específico\n6-Descriptografar arquivo específico\n7-Criar um arquivo de texto criptografado\nMais opções em breve...\nQual opção deseja escolher: '))

        if opcao == 1:
            texto = input('Digite o conteúdo a ser criptografado: ')
            with open('crypt.txt', 'wb') as text:
                text.write(texto.encode())
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()

            criptografado = fernet.encrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 2:
            with open('crypt.txt', 'rb') as textcrypt:
                conteudo_crypt = textcrypt.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open('crypt.txt', 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 3:
            textforcrypt = input('Digite o conteúdo a ser criptografado: ')
            criptografado = fernet.encrypt(textforcrypt.encode())
            print(criptografado)
        elif opcao == 4:
            textfordescrypt = input('Digite o conteúdo a ser descriptografado: ')
            descriptografado = fernet.decrypt(textfordescrypt.encode())
            print(descriptografado)
            print("OBS: Essa ferramenta está em testes, ela não aceita letras com acentos, recomendo usar a opção 2 para descriptografar no arquivo crypt.txt, cole a mensagem criptografada dentro do arquivo crypt.txt")
        elif opcao == 5:
            arquivo = input('Digite o nome do arquivo a ser criptografado (com extensão): ')
            os.system = arquivo
            with open(arquivo, 'rb') as file:
                conteudo = file.read()
            criptografado = fernet.encrypt(conteudo)
            print(criptografado)
            criptografado = fernet.encrypt(conteudo)

            with open(arquivo, 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
            print(criptografado)
        elif opcao == 6:
            arquivo = input('Digite o nome do arquivo a ser descriptografado (com extensão): ')
            with open(arquivo, 'rb') as file:
                conteudo_crypt = file.read()
            
            descriptografado = fernet.decrypt(conteudo_crypt)

            with open(arquivo, 'wb') as arquivo_descriptografado:
                arquivo_descriptografado.write(descriptografado)
            print(descriptografado)
        elif opcao == 7:
            nomedoarquivo_txt = input("Digite o nome do arquivo de texto (com extensão) que deseja criar: ")
            os.system(f"touch {nomedoarquivo_txt}.txt")
            conteudo = input("Digite o conteúdo que deseja adicionar ao arquivo: ")
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as text:
                        text.write(conteudo.encode())
            with open(f'{nomedoarquivo_txt}.txt', 'rb') as textcrypt:
                        conteudo_crypt = textcrypt.read()
            
            criptografado = fernet.encrypt(conteudo_crypt)
            
            with open(f'{nomedoarquivo_txt}.txt', 'wb') as arquivo_criptografado:
                        arquivo_criptografado.write(criptografado)
            print(criptografado)
            print(f"Arquivo '{nomedoarquivo_txt}' criado com sucesso!") 
        else:
            print('Opção inválida. Por favor, escolha as opções de 1 a 7.')
            break