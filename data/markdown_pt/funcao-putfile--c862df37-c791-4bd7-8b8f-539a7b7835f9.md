# Função PUTFILE( )

Invoca a caixa de diálogo Save As e retorna o nome do arquivo que você especifica.

```foxpro
PUTFILE([cCustomText] [, cFileName] [, cFileExtensions])
```

#### Parâmetros
 **cCustomText**
Especifica texto personalizado a ser exibido na caixa de diálogo Save As.
**cFileName**
Especifica o nome de arquivo padrão exibido na caixa de texto.
**cFileExtensions**
Especifica extensões de nome de arquivo. Somente nomes de arquivo com a extensão especificada são exibidos na lista rolável da caixa de diálogo Save As quando a caixa de seleção All Files está desmarcada. A primeira extensão em cFileExtensions é automaticamente anexada ao nome de arquivo digitado se uma extensão não for incluída com o nome do arquivo. O parâmetro cFileExtensions não pode exceder 254 caracteres de comprimento. Para uma lista de extensões de arquivo do Visual FoxPro e tipos de criador correspondentes, consulte o tópico online File Extensions and File Types. A expressão de caractere cFileExtensions pode assumir uma das seguintes formas: cFileExtensions pode conter uma única extensão, como PRG, e somente nomes de arquivo com essa extensão são exibidos. cFileExtensions pode conter uma lista de extensões de nome de arquivo separadas por ponto e vírgula. Por exemplo, se você incluir PRG;FXP, o Visual FoxPro exibe todos os nomes de arquivo com as extensões .prg e .fxp. Se os nomes de arquivo tiverem o mesmo nome raiz, mas extensões diferentes (por exemplo, Customer.prg e Customer.fxp), o Visual FoxPro exibe somente o nome de arquivo com a extensão que aparece primeiro em cFileExtensions. cFileExtensions pode conter uma lista de extensões de nome de arquivo separadas por barras verticais, como PRG|FXP. Nesse caso, o Visual FoxPro exibe todos os nomes de arquivo com as extensões listadas, mesmo se os arquivos tiverem o mesmo nome raiz. Se cFileExtensions contiver apenas um ponto e vírgula (;), o Visual FoxPro exibe todos os nomes de arquivo que não têm extensão. Se cFileExtensions for uma cadeia de caracteres vazia, o Visual FoxPro exibe os nomes de todos os arquivos no diretório ou pasta atual. Se cFileExtensions contiver curingas do MS-DOS, como o ponto de interrogação (?) e o asterisco (*), o Visual FoxPro exibe todos os nomes de arquivo com extensões que atendam aos critérios de curinga. Por exemplo, se cFileExtensions for ?X?, todos os nomes de arquivo com as extensões .fxp, .exe, .txt e assim por diante são exibidos.

# Valor de retorno

Caractere

# Observações

Use PUTFILE( ) para escolher um nome de arquivo existente ou especificar um novo nome de arquivo. PUTFILE( ) retorna o nome do arquivo com seu caminho. Se você não digitar um nome de arquivo, PUTFILE( ) retorna o nome de arquivo padrão (especificado com cFileName) e a extensão (especificada por cFileExtensions). Se você escolher Cancel ou pressionar ESC, PUTFILE( ) retorna uma cadeia de caracteres vazia. Você pode usar o nome de arquivo que PUTFILE( ) retorna para nomear um arquivo e salvá-lo no disco.

# Exemplo

O exemplo a seguir cria um arquivo de dados delimitado a partir de qualquer tabela existente que o usuário escolher. GETFILE( ) é usado para localizar e abrir uma tabela e PUTFILE( ) é usado para retornar o nome do arquivo de destino.

```foxpro
gcTableName = GETFILE('DBF', 'Open Table:')
USE (gcTableName)
gcDelimName = ALIAS() + '.DLM'
gcDelimFile = PUTFILE('Delimited file:', gcDelimName, 'DLM')
IF EMPTY(gcDelimFile)  && Esc pressed
   CANCEL
ENDIF
COPY TO (gcDelimFile) DELIMITED   && Create delimited file
MODIFY FILE (gcDelimFile) NOEDIT
```
