class Veiculo:
    def movimentar(self):
        print('Sou um veículo em movimento.')
   
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None
       
    def set_num_registro(self, registro):
        self.__num_registro = registro
   
    def get_fab_modl_numr(self):
        print(f'\nModelo: {self.__modelo}, fabricante: {self.__fabricante}, número de registro: {self.__num_registro} \n')
       
   
#====================================================
#herança

class Carro(Veiculo):
    def movimentar(self):
        print('Sou um carro andando.')


#============================================

class Motocicleta(Veiculo):
    def movimentar(self):
        print('Sou uma moto e corro muito.')
#=================================================

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        super().__init__(fabricante, modelo)
       
    def movimentar(self):
        print('Sou um avião, e estou voando.')
       
    def get_categoria(self):
        return self.__categoria
#===================================================

if __name__ == '__main__':
    meu_veiculo = Veiculo('Ford', 'F1000')
    meu_veiculo.movimentar()
    meu_veiculo.set_num_registro('234235234')
    meu_veiculo.get_fab_modl_numr()
   
   
    meu_carro = Carro('GM', 'Golf')
    meu_carro.movimentar()
    meu_carro.set_num_registro('a738429423')
    meu_carro.get_fab_modl_numr()
       
    minha_moto = Motocicleta('Shineray', 'Worker 125')
    minha_moto.movimentar()
    minha_moto.set_num_registro(237462734)
    minha_moto.get_fab_modl_numr()
   
    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.set_num_registro(999999999999)
    meu_aviao.get_fab_modl_numr()
    print(meu_aviao.get_categoria())
