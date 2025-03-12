def valida_numero_float(numero):
    try:
        return float(numero)
    except ValueError:
        return None

def soma_digitos(numero):
    
    if numero.isdigit():
        soma = sum(int(digit) for digit in numero)
        return soma
    else:
        return "Valor inválido! Insira um número inteiro."

def main():
    
    temp_maxima = input("Informe a temperatura máxima: ")
    temp_minima = input("Informe a temperatura mínima: ")

    
    temp_maxima = valida_numero_float(temp_maxima)
    temp_minima = valida_numero_float(temp_minima)

    if temp_maxima is None or temp_minima is None:
        print("Valores de temperatura inválidos! Por favor, insira números válidos.")
        return

    
    media = (temp_maxima + temp_minima) / 2
    variacao = temp_maxima - temp_minima

    print(f"A média das temperaturas é: {media:.2f}")
    print(f"A variação entre as temperaturas é: {variacao:.2f}")

    
    numero = input("Informe um número para calcular a soma dos dígitos: ")


    resultado = soma_digitos(numero)
    print(f"Resultado: {resultado}")

# Executando o programa
main()
