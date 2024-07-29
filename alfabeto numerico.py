contador = 0;

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
num = int(input("Digite quantos bagui vai ter: "))

if (num < 1 or num > 26):
    print("Pode não parceiro");
else:
    resultado = []
    for contador in range(num):
        resultado.append(alfabeto[contador])
    print(', '.join(resultado))