import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Enviar mensagem")
        print("2. Ver mensagens")
        print("3. Calcular soma")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            msg = input("Digite a mensagem: ")
            response = requests.post(f"{BASE_URL}/message", json={"message": msg})
            print(response.json())

        elif opcao == '2':
            response = requests.get(f"{BASE_URL}/messages")
            for i, msg in enumerate(response.json(), 1):
                print(f"{i}: {msg}")

        elif opcao == '3':
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                response = requests.post(f"{BASE_URL}/sum", json={"a": a, "b": b})
                print("Resultado:", response.json()["resultado"])
            except ValueError:
                print("Por favor, insira números válidos.")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()