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
        if 1 <= novoVolume <= 10:
            tv.volumeAtual = novoVolume
        else:
            print('Limite alcançado')

    def aumentarVolume(self, tv):
        self.ajustarVolume(tv, 1)
        print(f'Ajustando volume para {tv.volumeAtual}')

    def diminuirVolume(self, tv):
        self.ajustarVolume(tv, -1)
        print(f'Ajustando volume para {tv.volumeAtual}')

    def silenciarVolume(self, tv):
        self.ajustarVolume(tv, valor=0)
        print("Silenciado")
    
    def restaurarVolume(self, tv):
        volumeAnterior = tv.volumeAtual
        self.ajustarVolume(tv, volumeAnterior)
        print(f'Ajustando volume para {tv.volumeAtual}')