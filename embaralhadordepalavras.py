from time import sleep

def traco():
    #uso estilístico#
    print("-"*50)
def banner():
    traco()
    print("Bem vindo ao embaralhador de palavras!;)")
    traco()

    
    
#menu
def menu():
    while True:
        try:
            option = int(input("\nVocê deseja:\n\n[1] Inverter palavras de trás pra frente\n[2] Embaralhar palavras\n[3] Inverter palavras (espelho)\nOpcão: "))
        except ValueError:
            traco()
            print("\nERRO: Escolha uma OPÇÃO entre 1 e 2.\n")
        except:
            print("ERRO: ")
            raise
        else:
            if option <= 3:
                return option
            elif option > 2:
                traco()
                print("Escolha uma opção entre 1 e 2.\n")



#inverte(de tras pra frente) palav
def dtf(palavras):
    palavras.reverse()
    print("\nSeu texto de trás pra frente:\n")
    for p in palavras:
        print("{} ".format(p), end = "")
    print("\n")
    traco()



#embaralha
def embaralhar(palavras):
    from random import shuffle
    shuffle(palavras)
    print("\nSeu texto:\n")
    for p in palavras:
        print("{} ".format(p), end = "")
    print("\n")
    traco()



#programa
def main():
    print("Bem vindo ao embaralhador de palavras! ;)")
    while True:
        # #fazer o banner aqui
        option = menu()
        # try:
        #     palavras = str(input("Digite as palavras: ").lower()).split()
        # except ValueError:
        #     print("\nApenas letras são permitidas! (por enquanto)\n")
        # except:
        #     print("Erro: ")
        #     raise

        if option == 1:
            palavras = str(input("Digite as palavras: ").lower()).split()
            dtf(palavras)
            sleep(3)

        elif option == 2:
            palavras = str(input("Digite as palavras: ").lower()).split()
            embaralhar(palavras)
            sleep(3)

        elif option == 3:
            palavras = str(input("Digite as palavras: ").lower())
            print("\n{}\n".format(palavras[::-1]))
            traco()
            sleep(3)



#executa
if __name__ == "__main__":
    main()
