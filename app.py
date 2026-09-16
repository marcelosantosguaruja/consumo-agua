# Programa de Alerta de consumo de água (m3)
#*******************************************

# Preparo do ambiente
import os
os.system("cls")

# Verificando condições de consumo de água.
while True:

    opcao = input("""
            Informe qual o tipo de seu imóvel,
            C - Comercial
            H - Casa
            A - Apartamento

            Digite sua opção: """).upper()

    match opcao:

        case "C":
            print("Tarifa comercial aplicada – consulte o plano corporativo.")

        case "H" | "A":
            consumo = float(input("Informe o consumo de água em m3: "))

            if consumo < 10:    # 1ª Regra Consumo abaixo de 10
                print(f"""
                Consumo de água informado foi de {consumo} m3.
                EXCELENTE!!! O seu consumo foi ECONÔMICO
                e está abaixo do padrão de consumo residencial.
                """)

            elif consumo <= 25:    # 2ª Regra Consumo entre 10 e 25
                print(f"""
                Consumo de água informado foi de {consumo} m3.
                Consumo MODERADO dentro do padrão residencial.
                """)

            else:                   # Regra acima de 25
                print(f"""
                Consumo de água informado foi de {consumo} m3.
                CUIDADO!!! Consumo EXCESSIVO.
                Verifique vazamentos e adote medidas econômicas.
                """)

        case _:
            print("Opção inválida. Por favor, escolha C, H ou A.")
            continue