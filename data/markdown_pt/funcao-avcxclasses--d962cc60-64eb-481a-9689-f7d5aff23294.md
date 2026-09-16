# Função AVCXCLASSES( )

Coloca as informações sobre classes em uma biblioteca de classes em uma matriz.

```foxpro
AVCXCLASSES(ArrayName, cLibraryName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz na qual as informações de classe são colocadas. Se a matriz que você especificar não existir, o Visual FoxPro cria automaticamente a matriz. Se a matriz existir e não for grande o suficiente para conter os nomes de classes e classes base, o Visual FoxPro aumenta automaticamente o tamanho da matriz. Se a matriz for maior que o necessário, o Visual FoxPro trunca a matriz. A matriz contém uma linha para cada classe na biblioteca de classes, e cada linha contém 11 colunas com informações sobre a classe. A tabela a seguir lista as informações de classe em cada coluna. Coluna Informação de classe Nome do campo .VCX 1 Nome da classe. OBJNAME 2 Classe base da classe. BASECLASS 3 Nome da classe pai da classe. CLASS 4 Caminho relativo e nome de arquivo da biblioteca de classes pai. CLASSLOC 5 Caminho relativo e nome de arquivo do bitmap para um ícone de classe personalizada. RESERVED4 6 Caminho relativo e nome de arquivo para um ícone de classe personalizada do Gerenciador de projetos ou Navegador de classes. RESERVED5 7 ScaleMode da classe, Pixels ou Foxels. RESERVED6 8 Descrição da classe. RESERVED7 9 Caminho relativo e nome de arquivo para o arquivo #INCLUDE da classe. RESERVED8 10 Informações definidas pelo usuário para a classe. USER 11 True lógico (.T.) se a classe é OLEPUBLIC, caso contrário false lógico (.F.). RESERVED2
**cLibraryName**
Especifica o nome da biblioteca de classes para a qual AVCXCLASSES( ) coloca informações de classe na matriz especificada com ArrayName . cLibraryName pode conter um caminho para a biblioteca de classes. Um erro é gerado se a biblioteca de classes que você especificar não existir.

# Valor de retorno

Numérico

# Observações

AVCXCLASSES( ) retorna o número de linhas na matriz (o número de classes na biblioteca de classes).

# Exemplo

O exemplo a seguir usa AVCXCLASSES( ) para criar e preencher uma matriz chamada aClasses com os nomes e classes base das classes na biblioteca de classes Buttons. DISPLAY MEMORY lista o conteúdo da matriz na janela principal do Visual FoxPro.

```foxpro
ACTIVATE SCREEN
CLEAR
? AVCXCLASSES(aClasses, '\VFP\SAMPLES\CLASSES\BUTTONS.VCX')
*** Displays 5
FOR nColCount = 1 TO ALEN(aClasses,2) && Loop through columns
   ? aClasses(1, nColCount) && Each column of the 1st class
NEXT
*** Displays the following:
*
* cmdCancel
* commandbutton
* cmdok
* buttons.vcx
* cancel.bmp
* cancel.bmp
* Pixels
* Release Form or Form Set
*
*
* .F.
```
