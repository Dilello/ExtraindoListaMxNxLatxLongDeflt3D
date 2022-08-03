# Criando lista com M, N, Lat e Long dos trechos da Condição de Contorno do Delft

## Pré-requisitos

1 - Exportar a malha do Delft3D num arquivo shapefile (.shp);

2 - No ArcGis ou Qgis extrair as Lat e Long dos vértices de cada célula da fronteira e salvar como arquivo .txt (1º arquivo);

3 - Extrair do arquivo .bnd do seu modelo no Delft3D, os limites M e N de cada trecho da condição de contorno e salvar como arquivo .csv (2º arquivo);

## Observações importantes caso mude de projeto

Inspecione o 1º arquivo e verifice qual foi o ordenamento dos pontos. Pode se que tenha variação de um arquivo para o outro, sendo necessário, as vezes, descartar 
as primeiras linha e selecionar as linhas de 2 em 2. Para tal, abra e visualize a malha no GUI do Delft e compare as lat e long dos vertices com as lat 
e long das primeiras linhas do 1º arquivo. Depois compare com o código (linha 18, 20, 22, 38, 40, 42).
As Fronteiras também podem mudar de nome (East, West, South). Caso isso aconteça, mude os nomes no código (linhas 17, 19, 37 e 39).

Segue abaixo o trecho onde se deve fazer as alterações:


    if fronteira == 'East':
        df_Bruto = pd.DataFrame(BrutoLatLong[1:,:4], columns = ['Long','Lat','iD1','iD2'])
    elif fronteira == 'South':
        df_Bruto = pd.DataFrame(BrutoLatLong[:,:4], columns = ['Long','Lat','iD1','iD2'])
    else:
        df_Bruto = pd.DataFrame(BrutoLatLong[1:,:4], columns = ['Long','Lat','iD1','iD2'])
  [...]
  
      if fronteira == 'East':
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 3]
    elif fronteira == 'South':
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 0]
    else:
        df1_FronteiraTotal = df_Bruto.loc[df_Bruto['iD2'] == 4]
 


