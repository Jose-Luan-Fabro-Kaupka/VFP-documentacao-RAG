# Comando FOR EACH ... ENDFOR

Executa um conjunto de comandos para cada elemento em uma matriz ou coleção do Visual FoxPro.

```foxpro
FOR EACH Var [AS Type [OF Class Library]] IN Group [FOXOBJECT]
      Commands
   [EXIT]
   [LOOP]
ENDFOR | NEXT [Var]
```

#### Parâmetros
 **Var**
Uma variável ou elemento de matriz usado para iterar pelos elementos de Group.
**Type**
Uma classe base, nome de classe ou biblioteca de tipos. (Somente para Intellisense)
**Class Library**
Biblioteca de classes contendo a classe base, o nome de classe ou a biblioteca de tipos especificada com Type. (Somente para Intellisense)
**Group**
Uma matriz do Visual FoxPro, uma matriz OLE, uma coleção do Visual FoxPro ou uma coleção OLE.
**FOXOBJECT**
Especifica que a variável ou elemento de matriz Var conterá apenas objetos nativos (não COM) do Visual FoxPro.
**Commands**
Especifica os comandos do Visual FoxPro a serem executados para cada elemento em Group. Commands pode incluir qualquer número de comandos.
**EXIT**
Transfere o controle de dentro do loop FOR EACH ... ENDFOR para o comando imediatamente após ENDFOR. Você pode colocar EXIT em qualquer lugar entre FOR EACH e ENDFOR.
**LOOP**
Retorna o controle diretamente de volta à cláusula FOR EACH sem executar as instruções entre LOOP e ENDFOR. LOOP pode ser colocado em qualquer lugar entre FOR EACH e ENDFOR.

# Exemplos

Os exemplos a seguir demonstram como FOR EACH é usado para enumerar elementos em uma matriz do Visual FoxPro, uma matriz OLE e um conjunto de botões de comando atribuídos a uma matriz de objetos.

No exemplo a seguir, uma matriz de variáveis do Visual FoxPro é criada e FOR EACH é usado para exibir o conteúdo de cada elemento na matriz.

```foxpro
DIMENSION cMyArray(3)
cMyArray[1] = 'A'
cMyArray[2] = 'B'
cMyArray[3] = 'C'
FOR EACH cMyVar IN cMyArray
   ? cMyVar
ENDFOR
```

No exemplo a seguir, uma instância do Microsoft Excel é criada e um novo workbook é adicionado. FOR EACH é usado para exibir o nome de cada planilha no workbook. Este exemplo requer que o Microsoft Excel esteja instalado corretamente na máquina em que o exemplo é executado.

```foxpro
oExcel = CREATE("Excel.Application")
oExcel.Workbooks.ADD
FOR EACH oMyVar IN oExcel.sheets
   ? oMyVar.name
NEXT oMyVar
```

No exemplo a seguir, cinco botões de comando são colocados em um formulário. FOR EACH é usado para exibir os botões no formulário e especificar as legendas, estilos de fonte e posições de cada botão.

```foxpro
PUBLIC oMyObject
oMyObject = CREATEOBJECT("frmTest")
oMyObject.SHOW
DEFINE CLASS frmTest AS FORM
Height = 200
DIMENSION MyArray[5]
   PROCEDURE Init
      FOR i = 1 to 5
         THIS.AddObject('THIS.MyArray[i]',;
            'COMMANDBUTTON')
      ENDFOR
      ****** FOR EACH - NEXT ******
      FOR EACH oButton IN THIS.MyArray
         oButton.Visible = .T.
      NEXT

      ****** FOR EACH - NEXT element  ******
      FOR EACH oButton IN THIS.MyArray
         oButton.FontBold = .T.
      NEXT obutton
      j = 1
      ****** FOR EACH - ENDFOR ******
      FOR EACH oButton IN THIS.MyArray
         oButton.top = j * 30
         j = j + 1
      ENDFOR

      ****** FOR EACH - ENDFOR element ******
      FOR EACH oButton IN THIS.MyArray
         oButton.FontItalic = .T.
      ENDFOR obutton

      j = 1
      ****** EXIT  ******
      FOR EACH oButton IN THIS.MyArray
         oButton.Caption = "test" + str(j)
         j = j+1
         IF j > 3
            EXIT
         ENDIF
      NEXT

      j = 1
      ****** LOOP  ******
      FOR EACH oButton IN THIS.MyArray
         IF j > 3
            LOOP
         ENDIF
         j = j + 1
         oButton.Left = 25
      NEXT
   ENDPROC
ENDDEFINE
```
