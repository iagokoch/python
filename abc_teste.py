from random import choice 
import string

tam_senha = print("Qual tamanho de senha você deseja: \n")
tam_senha = print("4 Dígitos")
tam_senha = print ("5 Dígitos")
tam_senha = print("6 Dígitos")
tam_senha = int(input("Digite a quantidade (4, 5 ou 6 dígitos): \n"))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha_segura= ''

for i in range(tam_senha):
    senha_segura += choice(caracteres)


print("A senha (segura) gerada é: \n", senha_segura)