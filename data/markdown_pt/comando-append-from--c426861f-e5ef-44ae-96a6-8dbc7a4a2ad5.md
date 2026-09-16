# Comando APPEND FROM

Adiciona registros ao final da tabela selecionada atualmente a partir de outro arquivo.

```foxpro
APPEND FROM FileName | ?[FIELDS FieldList] [FOR lExpression]
   [[TYPE] [DELIMITED [WITH Delimiter | WITH BLANK | WITH TAB
      | WITH CHARACTER Delimiter] | DIF | FW2 | MOD | PDOX | RPD |
      SDF | SYLK | WK1 | WK3 | WKS | WR1 | WRK | CSV | XLS | XL5
      [SHEET cSheetName] | XL8 [SHEET cSheetName]]] [AS nCodePage]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo do qual anexar. Se você não incluir uma extensão de nome de arquivo, uma tabela Visual FoxPro e a extensão padrão .dbf são assumidas. Se você estiver anexando de uma tabela Visual FoxPro, registros na tabela marcados para exclusão são anexados se a configuração atual de SET DELETED estiver OFF.
**?**
Exibe a caixa de diálogo Open, na qual você pode escolher uma tabela da qual anexar.
**FIELDS FieldList**
Especifica em quais campos os dados são anexados. Observação Você não pode anexar a campos memo a partir de arquivos de texto como CSV e SDF.
**FOR lExpression**
Anexa um novo registro para cada registro na tabela selecionada atualmente para o qual lExpression resulta em True (.T.). Os registros são anexados até que o final da tabela selecionada atualmente seja alcançado. Se você omitir FOR, o arquivo de origem inteiro é anexado à tabela selecionada atualmente.
**TYPE**
Especifica o tipo de arquivo de origem do arquivo do qual você está anexando. Embora você deva especificar um tipo de arquivo se o arquivo do qual você está anexando não for uma tabela Visual FoxPro, você não precisa incluir a palavra-chave TYPE. Você pode anexar de uma ampla variedade de tipos de arquivo diferentes, incluindo arquivos de texto ASCII delimitados, nos quais você pode especificar um delimitador de campo. Se o arquivo de origem do qual você está anexando não tiver a extensão de arquivo padrão usual para esse tipo de arquivo, o nome do arquivo de origem deve incluir a extensão do arquivo. Por exemplo, planilhas Microsoft Excel normalmente têm uma extensão .xls. Se a planilha Microsoft Excel da qual você anexa tiver uma extensão diferente da .xls esperada, certifique-se de especificar a extensão. Observação Quando você anexa de uma planilha, os dados na planilha devem ser armazenados em ordem row-major em vez de column-major. Isso permite que os dados anexados da planilha correspondam à estrutura da tabela.
**DELIMITED**
Especifica que o arquivo de origem do qual os dados são anexados à tabela Visual FoxPro atual é um arquivo delimitado. Um arquivo delimitado é um arquivo de texto ASCII no qual cada registro termina com carriage return e line feed. Por padrão, presume-se que o conteúdo dos campos é separado uns dos outros por vírgulas (não inclua espaços extras antes ou depois das vírgulas) e que os valores de campos de caractere são adicionalmente delimitados por aspas duplas. Por exemplo: "Smith",9999999,"TELEPHONE" A extensão do arquivo é assumida como .txt para todos os arquivos delimitados. Você pode importar datas de arquivos delimitados se as datas estiverem no formato de data adequado. O formato de data padrão é mm/dd/yy. Incluir a porção do século de uma data é opcional. O Visual FoxPro importará uma data, como 12/25/95, que não inclui o século e assume que a data está no século vinte. Delimitadores de data podem ser qualquer caractere não numérico, exceto o delimitador que separa os campos no arquivo delimitado. Datas em outros formatos podem ser importadas se seus formatos corresponderem aos formatos de data disponíveis em SET DATE. Para testar se um formato de data pode ser importado com sucesso, use-o com CTOD( ). Se a data for aceitável para CTOD( ), a data será importada corretamente.
**DELIMITED WITH Delimiter**
Indica que campos de caractere são separados por um caractere diferente da aspas.
**DELIMITED WITH BLANK**
Especifica arquivos que contêm campos separados por espaços em vez de vírgulas.
**DELIMITED WITH TAB**
Especifica arquivos que contêm campos separados por tabulações em vez de vírgulas.
**DELIMITED WITH CHARACTER Delimiter**
Especifica arquivos que contêm campos todos delimitados pelo caractere especificado com Delimiter . Se Delimiter for um ponto e vírgula (o caractere usado no Visual FoxPro para indicar continuação de linha de comando), coloque o ponto e vírgula entre aspas. Você também pode especificar as palavras-chave BLANK e TAB para Delimiter . A cláusula WITH Delimiter pode ser combinada com a cláusula WITH CHARACTER. Por exemplo, o comando a seguir adiciona registros de um arquivo de texto com campos de caractere delimitados por sublinhados e todos os campos delimitados uns dos outros com asteriscos: APPEND FROM mytxt.txt DELIMITED WITH _ WITH CHARACTER *
**DIF**
Inclua DIF para importar dados de um arquivo VisiCalc .dif (Data Interchange Format). Vetores (colunas) tornam-se campos na tabela selecionada atualmente e tuplas (linhas) tornam-se registros. Nomes de arquivo DIF são assumidos com extensão .dif.
**FW2**
Inclua FW2 para importar dados de um arquivo criado pelo Framework II. Nomes de arquivo FW2 são assumidos com extensão .fw2.
**MOD**
Inclua MOD para importar dados de um arquivo Microsoft Multiplan versão 4.01. Arquivos MOD são criados pelo Microsoft Multiplan versão 4.01 e são assumidos com extensão .mod.
**PDOX**
Inclua PDOX para importar dados de um arquivo de banco de dados Paradox versão 3.5 ou 4.0. Nomes de arquivo Paradox são assumidos com extensão .db.
**RPD**
Inclua RPD para importar dados de um arquivo criado pelo RapidFile versão 1.2. Nomes de arquivo RapidFile são assumidos com extensão .rpd.
**SDF**
Inclua SDF para importar dados de um arquivo System Data Format. Um arquivo SDF é um arquivo de texto ASCII no qual os registros têm comprimento fixo e terminam com carriage return e line feed. Campos não são delimitados. A extensão do nome de arquivo é assumida como .txt para arquivos SDF. A conversão eficaz de dados de data de arquivos SDF para tabelas Visual FoxPro requer que os dados sejam armazenados no formato YYYYMMDD. Se as informações de data forem armazenadas em formatos ambíguos, você deve mapear a coluna de data para uma coluna de caractere de largura apropriada para poder inspecionar o valor e então aplicar a rotina de conversão correta para criar dados de data formatados corretamente.
**SYLK**
Inclua SYLK para importar dados de um arquivo no formato de intercâmbio SYLK (Symbolic Link). Arquivos SYLK são usados no Microsoft MultiPlan. Colunas no arquivo SYLK tornam-se campos na tabela Visual FoxPro e linhas tornam-se registros. Arquivos SYLK não têm extensão.
**WK1**
Inclua WK1 para importar dados de uma planilha Lotus 1-2-3 versão 2.x. Cada coluna da planilha torna-se um campo na tabela; cada linha da planilha torna-se um registro na tabela. Uma extensão de nome de arquivo .WK1 é atribuída a uma planilha criada no Lotus 1-2-3 revisão 2.x.
**WK3**
Inclua WK3 para importar dados de uma planilha Lotus 1-2-3. Cada coluna da planilha torna-se um campo na tabela; cada linha da planilha torna-se um registro na tabela. Uma extensão de nome de arquivo .wk3 é atribuída a uma planilha criada no Lotus 1-2-3 revisão 3.x.
**WKS**
Inclua WKS para importar dados de uma planilha Lotus 1-2-3 revisão 1-A. Cada coluna da planilha torna-se um campo na tabela; cada linha da planilha torna-se um registro na tabela. Uma extensão de nome de arquivo .wks é atribuída a uma planilha criada no Lotus 1-2-3 revisão 1-A.
**WR1**
Inclua WR1 para importar dados de uma planilha Lotus Symphony versão 1.1 ou 1.2. Cada coluna da planilha torna-se um campo na tabela e cada linha da planilha torna-se um registro na tabela. Uma extensão de nome de arquivo .wr1 é atribuída a uma planilha criada no Symphony versões 1.1 ou 1.2.
**WRK**
Inclua WRK para importar dados de uma planilha Lotus Symphony versão 1.0. Cada coluna da planilha torna-se um campo na tabela e cada linha da planilha torna-se um registro na tabela. Uma extensão de nome de arquivo .wrk é atribuída a uma planilha criada no Symphony versão 1.0.
**CSV**
Inclua CSV para importar dados de um arquivo comma separated value. Um arquivo CSV tem nomes de campo como a primeira linha no arquivo; os nomes de campo são ignorados quando o arquivo é importado.
**XLS**
Inclua XLS para importar dados de uma planilha Microsoft Excel. Cada coluna da planilha torna-se um campo na tabela e cada linha da planilha torna-se um registro na tabela. Planilhas criadas no Microsoft Excel recebem uma extensão de nome de arquivo .xls.
**XL5**
Inclua XL5 para importar dados do Microsoft Excel versão 5.0. Colunas da planilha tornam-se campos na tabela; as linhas da planilha tornam-se registros na tabela. Planilhas criadas no Microsoft Excel têm extensão .xls. Se você omitir a cláusula SHEET, os dados em Sheet1 são importados. Para importar dados de uma planilha específica, inclua a palavra-chave SHEET e especifique o nome da planilha com cSheetName .
**XL8**
Inclua XL8 para importar dados do Microsoft Excel 97. Colunas da planilha tornam-se campos na tabela; as linhas da planilha tornam-se registros na tabela. Planilhas criadas no Microsoft Excel têm extensão .xls. Se você omitir a cláusula SHEET, os dados em Sheet1 são importados. Para importar dados de uma planilha específica, inclua a palavra-chave SHEET e especifique o nome da planilha com cSheetName .
**AS nCodePage**
Especifica a página de código da tabela ou arquivo de origem. O Visual FoxPro copia o conteúdo da tabela ou arquivo de origem e, ao copiar os dados, converte automaticamente os dados para a página de código da tabela atual. Se você especificar um valor para nCodePage que não seja suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, possibilitando especificar uma página de código para a tabela ou arquivo anexado. Se você omitir AS nCodePage e o Visual FoxPro não puder determinar a página de código da tabela ou arquivo de origem, o Visual FoxPro copia o conteúdo da tabela ou arquivo de origem. Ao copiar os dados, converte automaticamente os dados para a página de código atual do Visual FoxPro. Se SET CPDIALOG estiver ON, a tabela na área de trabalho selecionada atualmente é marcada com uma página de código. Se você estiver anexando de uma tabela não marcada com uma página de código, a caixa de diálogo Code Page é exibida, possibilitando escolher a página de código da tabela da qual você está anexando. A página de código atual do Visual FoxPro pode ser determinada com CPCURRENT( ). Se você omitir AS nCodePage e o Visual FoxPro puder determinar a página de código da tabela ou arquivo sendo anexado, o Visual FoxPro copia o conteúdo da tabela ou arquivo anexado. Ao copiar os dados, converte automaticamente os dados para a página de código da tabela selecionada atualmente. Se nCodePage for 0, o Visual FoxPro assume que a página de código da tabela ou arquivo sendo anexado é a mesma da tabela selecionada atualmente. Nenhuma conversão para a página de código atual do Visual FoxPro ocorre.

# Observações

Se o arquivo do qual você anexa for uma tabela Visual FoxPro ou uma tabela criada em uma versão anterior do FoxPro, uma extensão .dbf é assumida. Se a tabela Visual FoxPro ou a tabela criada em uma versão anterior do FoxPro não tiver extensão .dbf, você deve especificar sua extensão. Se o arquivo não for uma tabela Visual FoxPro ou uma tabela criada em uma versão anterior do FoxPro, você deve especificar o tipo de arquivo do qual anexa.

Antes de anexar de uma tabela criada no dBASE IV ou dBASE V que contém um campo memo, você deve primeiro abrir a tabela no Visual FoxPro com USE. Quando solicitado a converter o arquivo, escolha Yes.

Se você anexar de uma tabela Visual FoxPro ou de uma tabela criada em uma versão anterior do FoxPro, a tabela da qual você anexa pode estar aberta em outra área de trabalho. Registros marcados para exclusão na tabela da qual você está anexando são desmarcados depois que os registros são anexados.

Use a função DBF( ) para anexar de um cursor temporário somente leitura criado por um comando SELECT - SQL Command . Inclua o nome do cursor na função DBF( ) como no exemplo a seguir:

```foxpro
APPEND FROM DBF('<Cursor Name>')
```

Se a tabela de destino usar auto-incremento, APPEND FROM falha se AUTOINCERROR estiver definido como ON, a menos que a opção FIELDS seja usada para omitir a coluna AUTOINC. Definir AUTOINCERROR como OFF ou desativar auto-incremento na tabela de destino usando CURSORSETPROP( ) permite que APPEND FROM seja bem-sucedido. O campo ou campos de auto-incremento da tabela de destino são incrementados de acordo com os valores especificados, e os valores na tabela de origem não são aplicados.

# Exemplo

No exemplo a seguir, a tabela `customer` é aberta, sua estrutura é copiada para uma tabela chamada `backup,` e `backup` é então aberta. O Visual FoxPro então anexa todos os registros em que country é igual a Finland da tabela `customer`. Esses registros são então copiados para um novo arquivo delimitado chamado `TEMP.TXT`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Open customer table
COPY STRUCTURE TO backup
USE backup
APPEND FROM customer FOR country = 'Finland'
COPY TO temp TYPE DELIMITED
MODIFY FILE temp.txt
USE
DELETE FILE backup.dbf
DELETE FILE temp.txt
```
