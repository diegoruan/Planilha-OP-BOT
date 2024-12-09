import pandas as pd
import os
from classes import Tubos, Resultados

def organizar():
    df = pd.read_excel("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\LOTEtemp.xlsx", header=4 )
    df = df.drop(columns=['Unnamed: 4','Unnamed: 5','Unnamed: 6'])
    df = df.dropna(thresh=2)
    df = df.fillna("")
    df = df.rename(columns={'Código Produto': 'cod', 'Produto': 'pro', 'OP': 'op', 'Lote Insumo':'lote'})

    dfVazio = pd.DataFrame({'cod':['','','','',''], 'pro':['','','','',''], 'op':['','','','',''], 'lote':['','','','','']})

    lista=[]

    for i, infos in df.iterrows():
        if i == 0:
            guardaOp = 0
        else:
            if infos.op != "":
                    di = df.loc[guardaOp:i-1]
                    di = pd.concat([di, dfVazio])
                    tubo = Tubos(di.iat[0,2],di.iat[0, 1],di.iat[0,0],di.iat[0,3],di.iat[1,3],di.iat[2,3],di.iat[3,3],di.iat[4,3],di.iat[5,3])
                    lista.append(tubo)
                    guardaOp = i
    di = df.loc[guardaOp-1:]
    di = pd.concat([di, dfVazio])
    tubo = Tubos(di.iat[0,2],di.iat[0, 1],di.iat[0,0],di.iat[0,3],di.iat[1,3],di.iat[2,3],di.iat[3,3],di.iat[4,3],di.iat[5,3])
    lista.append(tubo)

    listaTabela = []

    for tubo in lista:
        listaTabela.append([tubo.op, tubo.des, tubo.cod, tubo.loteT()])

    dm = pd.DataFrame(listaTabela, columns=['OP', 'Material', 'Código Produto', 'Tubo Fundido'])
    dm['Código Produto'] = dm['Código Produto'].astype(int)

    dt = pd.read_excel("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\CUFtemp.xlsx", header=4)
    dt = dt.drop(columns=['DATA','SITUAÇÃO'])
    dt = dt.dropna(thresh=2)
    dt['LOTE'] = dt['LOTE'].ffill()
    dt['LOTE'] = pd.to_numeric(dt['LOTE'], errors='coerce')
    dt['RESULTADO'] = dt['RESULTADO'].str.replace(',', '.').astype(float)
    dt = dt.sort_values(['LOTE', 'RESULTADO'])

    listaResultados = []

    for tubo in lista:
        busca1 = dt.loc[dt['LOTE'] <= tubo.lote1]
        lote1_cob = busca1['RESULTADO'].iloc[-1] if tubo.lote1 - busca1['LOTE'].iloc[-1] <= 10 else None
        lote1_fos = busca1['RESULTADO'].iloc[-2] if tubo.lote1 - busca1['LOTE'].iloc[-1] <= 10 else None
            
        if tubo.lote2 != None:
            busca2 = dt.loc[dt['LOTE'] <= tubo.lote2]
            lote2_cob = busca2['RESULTADO'].iloc[-1] if tubo.lote2 - busca2['LOTE'].iloc[-1] <= 10 else None
            lote2_fos = busca2['RESULTADO'].iloc[-2] if tubo.lote2 - busca2['LOTE'].iloc[-1] <= 10 else None
        else:
            lote2_cob = None
            lote2_fos = None
            
        if tubo.lote3 != None:
            busca3 = dt.loc[dt['LOTE'] <= tubo.lote3]
            lote3_cob = busca3['RESULTADO'].iloc[-1] if tubo.lote3 - busca3['LOTE'].iloc[-1] <= 10 else None
            lote3_fos = busca3['RESULTADO'].iloc[-2] if tubo.lote3 - busca3['LOTE'].iloc[-1] <= 10 else None
        else:
            lote3_cob = None
            lote3_fos = None
            
        if tubo.lote4 != None:
            busca4 = dt.loc[dt['LOTE'] <= tubo.lote4]
            lote4_cob = busca4['RESULTADO'].iloc[-1] if tubo.lote4 - busca4['LOTE'].iloc[-1] <= 10 else None
            lote4_fos = busca4['RESULTADO'].iloc[-2] if tubo.lote4 - busca4['LOTE'].iloc[-1] <= 10 else None
        else:
            lote4_cob = None
            lote4_fos = None
            
        if tubo.lote5 != None:
            busca5 = dt.loc[dt['LOTE'] <= tubo.lote5]
            lote5_cob = busca5['RESULTADO'].iloc[-1] if tubo.lote5 - busca5['LOTE'].iloc[-1] <= 10 else None
            lote5_fos = busca5['RESULTADO'].iloc[-2] if tubo.lote5 - busca5['LOTE'].iloc[-1] <= 10 else None
        else:
            lote5_cob = None
            lote5_fos = None
            
        if tubo.lote6 != None:
            busca6 = dt.loc[dt['LOTE'] <= tubo.lote6]
            lote6_cob = busca6['RESULTADO'].iloc[-1] if tubo.lote6 - busca6['LOTE'].iloc[-1] <= 10 else None
            lote6_fos = busca6['RESULTADO'].iloc[-2] if tubo.lote6 - busca6['LOTE'].iloc[-1] <= 10 else None
        else:
            lote6_cob = None
            lote6_fos = None

        resultados = Resultados(lote1_cob, lote1_fos, lote2_cob, lote2_fos, lote3_cob, lote3_fos, lote4_cob, lote4_fos, lote5_cob, lote5_fos, lote6_cob, lote6_fos)
        listaResultados.append([resultados.cobMin(), resultados.cobMax(), resultados.fosMin(), resultados.fosMax()])

    dr = pd.DataFrame(listaResultados, columns=['% Cu Mín', '% Cu Máx', '% P Mín', '% P Máx'])

    tabelaFinal = pd.merge(dm, dr, left_index=True, right_index=True)
    tabelaFinal = tabelaFinal.dropna(subset=['% Cu Mín', '% Cu Máx', '% P Mín', '% P Máx'])

    os.remove("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\LOTEtemp.xlsx")
    os.remove("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\CUFtemp.xlsx")

    tabelaFinal.to_excel("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\Resultado.xlsx", index=False)