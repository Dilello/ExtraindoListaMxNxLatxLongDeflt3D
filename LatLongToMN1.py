#------------------Importando Bibliotecas------------------------------------------------
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#------------------- FIM da importação---------------------------------------------------

#-------------------Início da Função mnLatLongTotal() --------------------------------------
def mnLatLongTotal():
    
    CaminhoDaLatLong = str(input('Usando barra dupla (Exemplo no WIN 10:c:\\CAMINHO\\),\n Entrar com o caminho que leva ao arquivo.TXT de com a lista lat e longs totais da fronteira de interesse:\n>> '))
    ArquivoDaLatLong = str(input('Entrar com nome arquivo com extensão .TXT:\n>> '))
    ArquivoSaidaFront = str(input('Entrar com nome arquivo com extensão .CSV de SAÍDA:\n>> '))
    fronteira = str(input('Entrar com a fronteira e interesse [East,South,West]: '))
    BrutoLatLong = np.loadtxt(CaminhoDaLatLong+ArquivoDaLatLong)

    if fronteira == 'East':
        df_Bruto = pd.DataFrame(BrutoLatLong[1:,:4], columns = ['Long','Lat','iD1','iD2'])
    elif fronteira == 'South':
        df_Bruto = pd.DataFrame(BrutoLatLong[:,:4], columns = ['Long','Lat','iD1','iD2'])
    else:
        df_Bruto = pd.DataFrame(BrutoLatLong[1:,:4], columns = ['Long','Lat','iD1','iD2'])

    print(df_Bruto)

    while True:
        try:
            Mini = float(input('Entrar com valor M INICIAL da fronteira: '))
            Mfim = float(input('Entrar com valor M FINAL da fronteira: '))
            Nini = float(input('Entrar com valor N INICIAL da fronteira: '))
            Nfim = float(input('Entrar com valor N FINAL da fronteira: '))
            break
        except ValueError:
            print('Valor inválido. Entrar apenas com valores numérios.')
            continue

    if fronteira == 'East':
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 3]
    elif fronteira == 'South':
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 0]
    else:
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 4]
    
    if Mini != Mfim:
        df1_FronteiraTotal['M'] = np.arange(Mini,Mfim+1)
    else:
        df1_FronteiraTotal['M'] = [Mini]*len(df1_FronteiraTotal)

    if Nini != Nfim:
        df1_FronteiraTotal['N'] = np.arange(Nini,Nfim+1)
    else:
        df1_FronteiraTotal['N'] = [Nini]*len(df1_FronteiraTotal)
    

    print(df1_FronteiraTotal)
    df1_FronteiraTotal.to_csv(CaminhoDaLatLong + ArquivoSaidaFront, sep=';')
    return df1_FronteiraTotal

#-------------------FIM da Função mnLatLongTotal() -----------------------------------------

#-------------------Início da Função mnLatLongTrecho()--------------------------------------
def mnLatLongTrecho(resultado1):

    CaminhoTrechoMxN = input('\nUsando barra dupla (Exemplo no WIN 10:c:\\CAMINHO\\),\n Entrar com o caminho que leva ao arquivo .CSV de com a lista M e N  dos trechos usados como entrada da fronteira de interesse:\n>> ')
    ArquivoTrechoMxN = str(input('Entrar com nome arquivo com extensão .CSV:\n>> '))
    ArquivoSaidaTrecho = str(input('Entrar com nome arquivo com extensão .CSV de SAÍDA:\n>> '))
    fronteira = str(input('Entrar com a fronteira e interesse [East,South,West]: '))
    df_MxN_trecho = pd.read_csv(CaminhoTrechoMxN+ArquivoTrechoMxN, header = 0, sep =';')
    df = df_MxN_trecho.loc[df_MxN_trecho['Fronteira'] == fronteira]
    
    dfm1 = pd.DataFrame()
    dfm1['Mi'] = pd.DataFrame(df['Mf'])
    dfm = pd.concat([df, dfm1])
    
    dfn1 = pd.DataFrame()
    dfn1['Ni'] = pd.DataFrame(df['Nf'])
    dfn = pd.concat([df, dfn1])
    
    dfmn = pd.DataFrame()
    dfmn ['M'] = pd.DataFrame(dfm['Mi'])
    dfmn ['N'] = pd.DataFrame(dfn['Ni'])
    dfmn = dfmn.sort_values(['N'], ignore_index=True)

    df_MxNxLatxLong = resultado1[resultado1.set_index(['M','N']).index.isin(dfmn.set_index(['M','N']).index)].drop(['iD1', 'iD2'], axis=1)
    df_MxNxLatxLong.to_csv(CaminhoTrechoMxN + ArquivoSaidaTrecho, sep=';')
    return df_MxNxLatxLong
#-------------------FIM da Função mnLatLongTrecho() -----------------------------------------

#-------------------Início CÓDIGO PRINCIPAL -------------------------------------------------

print('+ ================================================================================== +')
print('|                                                                                    |')
print('| Título: Criação um lista de coordenadas (MxNxLatxLong) da fronteira da malha Delft |')
print('|                                                                                    |')
print('| Autor: Oceanógrafo Marcelo Di Lello Jordão                                         |')
print('| Data: 02/08/2022                                                                   |')
print('| Contato: dilellocn@gmail.com                                                       |')
print('|                                                                                    |')
print('| Objetivo:  Selecionar a partir de um lista de Lat e Long da fronteira DELFT3D4     |')
print('| apenas as Lat e Long de início e fim de cada trecho usado na condição de contorno. |')
print('+ ================================================================================== +\n\n')
resultado1 = pd.DataFrame()
resultado2 = pd.DataFrame()
while True:
    try:
        opcao = int(input('Escolha a poção desejada [1 ou 2]:\n1 - Executar codigo\n2 - Sair\n>>'))
        if opcao == 1:
            resultado1 = mnLatLongTotal()
            resultado2 = mnLatLongTrecho(resultado1)
            visualizar = input('Deseja visualizar os dados na forma de tabela? [S/N]')
            if visualizar in 'Ss':
                print(resultado2)
                continue
            else:
                continue 
        elif opcao == 2:
            break
        else:
            print('Opção inválida. Entrar novamente, apenas com número 1 ou 2.')
            continue
    except ValueError:
        print('Opção inválida. Entrar novamente, apenas com número 1 ou 2.')
        continue
print('Programa finalizado!')

#-------------------FIM da CÓDIGO PRINCIPAL -----------------------------------------