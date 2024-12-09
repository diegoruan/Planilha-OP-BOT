import re

class Tubos():

    def __init__(self, op, des, cod, lote1, lote2, lote3, lote4, lote5, lote6):
        self.op = op
        self.des = des
        self.cod = cod
        self.lote1 =lote1
        self.lote2 =lote2
        self.lote3 =lote3
        self.lote4 =lote4
        self.lote5 =lote5
        self.lote6 =lote6

    def loteT(self):
        listaLotes = [self.lote1, self.lote2, self.lote3, self.lote4, self.lote5, self.lote6]
        listaLotes = [texto for texto in listaLotes if texto.strip()]
        listaAnos = listaLotes.copy()
        
        padraoLote = re.compile(r'^([^\-]+)')
        padraoAno = re.compile(r'.{2}$')

        for i, texto in enumerate(listaLotes):
            resultadoLote = padraoLote.search(texto)
            resultadoAnos = padraoAno.search(texto)
            if resultadoLote:
                listaLotes[i] = resultadoLote.group(0)
                listaAnos[i] = resultadoAnos.group(0)

        listaAnos = [int(val) for val in listaAnos]
        listaLotes = [int(val) for val in listaLotes]

        self.lote1 = listaLotes[0]
        self.lote2 = listaLotes[1] if 1 < len(listaLotes) else None
        self.lote3 = listaLotes[2] if 2 < len(listaLotes) else None
        self.lote4 = listaLotes[3] if 3 < len(listaLotes) else None
        self.lote5 = listaLotes[4] if 4 < len(listaLotes) else None
        self.lote6 = listaLotes[5] if 5 < len(listaLotes) else None

        xy = zip(listaAnos, listaLotes)

        listaOrdenada = sorted(xy, key = lambda x: (x[0], x[1]))

        listaAnos= list(map(lambda t: t[0], listaOrdenada))
        listaLotes= list(map(lambda t: t[1], listaOrdenada))

        lotesCompletos = self.loteP(listaAnos, listaLotes)
        return lotesCompletos

    def loteP(self, listaAnos, listaLotes):

        if len(set(listaAnos)) == 1:
            if len(listaLotes) == 6:
                completo = f'{listaLotes[0]}, {listaLotes[1]}, {listaLotes[2]}, {listaLotes[3]}, {listaLotes[4]}, {listaLotes[5]}/20{listaAnos[0]}'
            elif len(listaLotes) == 5:
                completo = f'{listaLotes[0]}, {listaLotes[1]}, {listaLotes[2]}, {listaLotes[3]}, {listaLotes[4]}/20{listaAnos[0]}'
            elif len(listaLotes) == 4:
                completo = f'{listaLotes[0]}, {listaLotes[1]}, {listaLotes[2]}, {listaLotes[3]}/20{listaAnos[0]}'
            elif len(listaLotes) == 3:
                completo = f'{listaLotes[0]}, {listaLotes[1]}, {listaLotes[2]}/20{listaAnos[0]}'
            elif len(listaLotes) == 2:
                completo = f'{listaLotes[0]}, {listaLotes[1]}/20{listaAnos[0]}'
            else:
                completo = f'{listaLotes[0]}/20{listaAnos[0]}'
        
        else:
            if len(listaLotes) == 6:
                completo = f'{f'{listaLotes[0]}/20{listaAnos[0]}' if listaAnos[0] != listaAnos[1] else listaLotes[0]}, {f'{listaLotes[1]}/20{listaAnos[1]}' if listaAnos[1] != listaAnos[2] else listaLotes[1]}, {f'{listaLotes[2]}/20{listaAnos[2]}' if listaAnos[2] != listaAnos[3] else listaLotes[2]}, {f'{listaLotes[3]}/20{listaAnos[3]}' if listaAnos[3] != listaAnos[4] else listaLotes[3]}, {f'{listaLotes[4]}/20{listaAnos[4]}' if listaAnos[4] != listaAnos[5] else listaLotes[4]}, {listaLotes[5]}/20{listaAnos[5]}'
            elif len(listaLotes) == 5:
                completo = f'{f'{listaLotes[0]}/20{listaAnos[0]}' if listaAnos[0] != listaAnos[1] else listaLotes[0]}, {f'{listaLotes[1]}/20{listaAnos[1]}' if listaAnos[1] != listaAnos[2] else listaLotes[1]}, {f'{listaLotes[2]}/20{listaAnos[2]}' if listaAnos[2] != listaAnos[3] else listaLotes[2]}, {f'{listaLotes[3]}/20{listaAnos[3]}' if listaAnos[3] != listaAnos[4] else listaLotes[3]}, {listaLotes[4]}/20{listaAnos[4]}'
            elif len(listaLotes) == 4:
                completo = f'{f'{listaLotes[0]}/20{listaAnos[0]}' if listaAnos[0] != listaAnos[1] else listaLotes[0]}, {f'{listaLotes[1]}/20{listaAnos[1]}' if listaAnos[1] != listaAnos[2] else listaLotes[1]}, {f'{listaLotes[2]}/20{listaAnos[2]}' if listaAnos[2] != listaAnos[3] else listaLotes[2]}, {listaLotes[3]}/20{listaAnos[3]}'
            elif len(listaLotes) == 3:
                completo = f'{f'{listaLotes[0]}/20{listaAnos[0]}' if listaAnos[0] != listaAnos[1] else listaLotes[0]}, {f'{listaLotes[1]}/20{listaAnos[1]}' if listaAnos[1] != listaAnos[2] else listaLotes[1]}, {listaLotes[2]}/20{listaAnos[2]}'
            else:
                completo = f'{listaLotes[0]}/20{listaAnos[0]}, {listaLotes[1]}/20{listaAnos[1]}'

        return completo

class Resultados():

    def __init__(self, lote1_cob, lote1_fos, lote2_cob, lote2_fos, lote3_cob, lote3_fos, lote4_cob, lote4_fos, lote5_cob, lote5_fos, lote6_cob, lote6_fos):
        self.lote1Cob =lote1_cob
        self.lote1Fos =lote1_fos
        self.lote2Cob =lote2_cob
        self.lote2Fos =lote2_fos
        self.lote3Cob =lote3_cob
        self.lote3Fos =lote3_fos
        self.lote4Cob =lote4_cob
        self.lote4Fos =lote4_fos
        self.lote5Cob =lote5_cob
        self.lote5Fos =lote5_fos
        self.lote6Cob =lote6_cob
        self.lote6Fos =lote6_fos
    
    def cobMax(self):
        listaCobMax = [self.lote1Cob,self.lote2Cob,self.lote3Cob,self.lote4Cob,self.lote5Cob,self.lote6Cob]
        listaCobMax = list(filter(lambda x: x is not None, listaCobMax))
        return max(listaCobMax) if sum(listaCobMax) > 0 else None
    
    def cobMin(self):
        listaCobMin = [self.lote1Cob,self.lote2Cob,self.lote3Cob,self.lote4Cob,self.lote5Cob,self.lote6Cob]
        listaCobMin = list(filter(lambda x: x is not None, listaCobMin))
        return min(listaCobMin) if sum(listaCobMin) > 0 else None
    
    def fosMax(self):
        listaFosMax = [self.lote1Fos,self.lote2Fos,self.lote3Fos,self.lote4Fos,self.lote5Fos,self.lote6Fos]
        listaFosMax = list(filter(lambda x: x is not None, listaFosMax))
        return max(listaFosMax) if sum(listaFosMax) > 0 else None
    
    def fosMin(self):
        listaFosMin = [self.lote1Fos,self.lote2Fos,self.lote3Fos,self.lote4Fos,self.lote5Fos,self.lote6Fos]
        listaFosMin = list(filter(lambda x: x is not None, listaFosMin))
        return min(listaFosMin) if sum(listaFosMin) > 0 else None