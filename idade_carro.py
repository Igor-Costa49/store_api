from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antiguidade(self):
        if((datetime.now().year - ano) > 20):
            return "Veículo antigo"
        else: 
            return "Veículo novo"    

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())

