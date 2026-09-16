# Função GETFILE( )

Exibe a caixa de diálogo Open.

```foxpro
GETFILE([cFileExtensions] [, cText] [, cOpenButtonCaption]
   [, nButtonType] [, cTitleBarCaption])
```

#### Parâmetros
 **cFileExtensions**
Especifica as extensões de nome de arquivo para os arquivos a serem exibidos na caixa de diálogo Open quando o tipo All Files não é escolhido. Ao passar um valor como literal, envolva-o com aspas (""). Não inclua um ponto (.) na frente das extensões de nome de arquivo. Observação O parâmetro cFileExtensions não pode exceder 254 caracteres de comprimento. cFileExtensions pode assumir várias formas: Se cFileExtensions contém uma única extensão, por exemplo, "prg", a caixa de diálogo Open exibe apenas os nomes de arquivo com essa extensão. Se cFileExtensions é a cadeia de caracteres vazia, a caixa de diálogo Open exibe todos os arquivos no diretório atual. cFileExtensions pode conter caracteres curinga como * e ?. A caixa de diálogo Open exibe todos os nomes de arquivo com extensões que atendem aos critérios curinga. Por exemplo, se cFileExtensions é "?X?", a caixa de diálogo Open exibe todos os nomes de arquivo com a extensão .fxp, .exe e .txt. cFileExtensions pode conter uma descrição de arquivo seguida de uma extensão de arquivo ou uma lista de extensões de arquivo separadas por vírgulas. A descrição do arquivo aparece na caixa de diálogo Open na lista Files of Type. Separe a descrição do arquivo da extensão de arquivo ou lista de extensões de arquivo com dois pontos (:). Separe várias descrições de arquivo e suas extensões com ponto e vírgula (;). Por exemplo, se cFileExtensions é "Text:TXT", a caixa de diálogo Open exibe a descrição de arquivo "Text" na lista Files of Type e exibe todos os arquivos com extensão .txt. Se cFileExtensions é "Tables:DBF; Files:TXT,BAK", as descrições de arquivo "Tables" e "Files" aparecem na lista Files of Type. Quando "Tables" é escolhido na lista Files of Type, todos os arquivos com extensão .dbf são exibidos. Quando "Files" é escolhido na lista Files of Type, todos os arquivos com extensões .txt e .bak são exibidos. Se cFileExtensions contém apenas um ponto e vírgula (";"), a caixa de diálogo Open exibe todos os arquivos sem extensões.
**cText**
Especifica o texto a ser exibido para o rótulo File Name na caixa de diálogo Open.
**cOpenButtonCaption**
Especifica uma legenda para o botão OK na caixa de diálogo Open.
**nButtonType**
Especifica o número e o tipo de botões que aparecem na caixa de diálogo Open. A tabela a seguir lista os valores para nButtonType. nButtonType Botões exibidos 0 (ou omitido) OK, Cancel 1 OK, New, Cancel 2 OK, None, Cancel Observação GETFILE( ) retorna a cadeia de caracteres "Untitled" com o caminho especificado na caixa de diálogo Open quando nButtonType é definido como 1 e o usuário clica em New, ou quando nButtonType é definido como 2 e o usuário clica em None.
**cTitleBarCaption**
Especifica a legenda para a barra de título da caixa de diálogo Open.

# Valor de retorno

Character. GETFILE( ) retorna o nome do arquivo escolhido na caixa de diálogo Open ou a cadeia de caracteres vazia se o usuário fechar a caixa de diálogo Open pressionando ESC, clicando em Cancel ou no botão Close na caixa de diálogo Open.

# Observações

# Exemplo

```foxpro
CLOSE DATABASES
SELECT 0
gcTable=GETFILE('DBF', 'Browse or Create a .DBF:',
   'Browse', 1, 'Browse or Create')
DO CASE
   CASE 'Untitled' $ gcTable
      CREATE (gcTable)
   CASE EMPTY(gcTable)
      RETURN
   OTHERWISE
      USE (gcTable)
      BROWSE
ENDCASE
```
