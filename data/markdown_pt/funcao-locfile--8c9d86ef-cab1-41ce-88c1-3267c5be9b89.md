# Função LOCFILE( )

Localiza um arquivo no disco e retorna o nome do arquivo com seu caminho.

```foxpro
LOCFILE(cFileName [, cFileExtensions] [, cFileNameCaption])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo a localizar. Se cFileName incluir apenas um nome de arquivo, LOCFILE( ) procura primeiro no diretório ou pasta padrão do Visual FoxPro. Se o arquivo não for encontrado no diretório ou pasta padrão, o caminho do Microsoft Visual FoxPro é então pesquisado. Use SET PATH para especificar o caminho do Visual FoxPro. Se cFileName incluir um caminho e um nome de arquivo, o local especificado é pesquisado. Se o arquivo não puder ser encontrado no local especificado, LOCFILE( ) pesquisa o diretório ou pasta padrão do Visual FoxPro e, em seguida, o caminho do Visual FoxPro. Se o arquivo for localizado, LOCFILE( ) retorna o nome e o caminho do arquivo.
**cFileExtensions**
Especifica extensões de arquivo para o arquivo a localizar. Se o nome de arquivo que você especifica com cFileName não incluir uma extensão, o Visual FoxPro aplica as extensões de arquivo listadas em cFileExtensions ao nome do arquivo e pesquisa o arquivo novamente. cFileExtensions também especifica as extensões de nome de arquivo dos arquivos exibidos na caixa de diálogo Open quando o arquivo que você especificou não pode ser localizado. cFileExtensions pode assumir várias formas: Se cFileExtensions contém uma única extensão (por exemplo, PRG), apenas arquivos com essa extensão são exibidos. cFileExtensions também pode conter curingas (* e ?). Todos os arquivos com extensões que atendem aos critérios de curinga são exibidos. Por exemplo, se cFileExtensions é ?X?, todos os arquivos com a extensão .fxp, .exe ou .txt são exibidos. No Visual FoxPro para Windows, cFileExtensions pode conter uma descrição de arquivo seguida por uma extensão de arquivo ou uma lista de extensões de arquivo separadas por vírgulas. A descrição do arquivo aparece na caixa de listagem Files of Type. Separe a descrição do arquivo da extensão de arquivo ou lista de extensões de arquivo com dois pontos (:). Separe várias descrições de arquivo e suas extensões de arquivo com ponto e vírgula (;). Por exemplo, se cFileExtensions é "Text:TXT", a descrição de arquivo "Text" aparece na caixa de listagem Files of Type e todos os arquivos com extensão .txt são exibidos. Se cFileExtensions é "Tables:DBF; Files:TXT,BAK", as descrições de arquivo "Tables" e "Files" aparecem na caixa de listagem Files of Type. Quando "Tables" é escolhido na caixa de listagem Files of Type, todos os arquivos com extensão .dbf são exibidos. Quando "Files" é escolhido na caixa de listagem Files of Type, todos os arquivos com extensões .txt e .bak são exibidos.
**cFileNameCaption**
Especifica o texto que você deseja usar para solicitar ao usuário. O texto aparece à esquerda da caixa de texto na qual você insere o nome do arquivo. Se omitido, "File name:" é exibido.

Para uma lista de extensões de arquivo do Visual FoxPro e tipos de criador correspondentes, consulte o tópico online File Extensions and File Types.

# Valor de retorno

Caractere

# Observações

A caixa de diálogo Open é exibida se o arquivo não puder ser localizado no diretório ou pasta padrão, no caminho do Visual FoxPro ou em um local especificado. A caixa de diálogo Open pode ser usada para localizar o arquivo. Quando um arquivo é escolhido na caixa de diálogo Open, o nome do arquivo é retornado com o caminho do arquivo.

Se você sair da caixa de diálogo Open escolhendo Cancel, pressionando ESC ou escolhendo Close no menu Control, o Visual FoxPro gera uma mensagem de erro e LOCFILE( ) não retorna um valor.
