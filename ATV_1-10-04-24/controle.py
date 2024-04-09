from televisao import Televisao

class Controle:
    def ligarTv(self, tv):
        tv.ligada = True
        print("TV - ON")
        print("Canal 1")

    def desligarTv(self, tv):
        tv.ligada = False
        print("TV - OFF")

    def mudarCanal(self, tv, novoCanal):
        if novoCanal in tv.canais:
            if novoCanal != tv.canalAtual:
                print(f'Mudando para o canal {novoCanal}')
            else:
                print (f'Você já esta no canal {tv.canalAtual}')
        else:
            print('Canal indisponivel')

    def ajustarVolume(self, tv, valor):
        novoVolume = tv.volumeAtual + valor
        if 0 <= novoVolume <= 10:
            tv.volumeAtual = novoVolume
            print(f'Ajustando volume para {tv.volumeAtual}')
        else:
            print('Limite alcançado')

    def aumentarVolume(self, tv):
        self.ajustarVolume(tv, 1)

    def diminuirVolume(self, tv):
        self.ajustarVolume(tv, -1)