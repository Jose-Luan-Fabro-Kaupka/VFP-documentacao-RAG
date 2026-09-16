# Comando COPY TO

Cria um novo arquivo a partir do conteúdo da tabela atualmente selecionada.

```foxpro
COPY TO FileName [DATABASE DatabaseName [NAME LongTableName]]
   [FIELDS FieldList | FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton]
   [Scope] [FOR lExpression1] [WHILE lExpression2]
   [ [WITH] CDX ] | [ [WITH] PRODUCTION ] [NOOPTIMIZE]
   [ [TYPE] [ FOXPLUS | FOX2X | DIF | MOD | SDF | SYLK | WK1 | WKS | WR1
   | WRK | CSV | XLS | XL5 | DELIMITED [ WITH Delimiter | WITH BLANK
   | WITH TAB | WITH CHARACTER Delimiter ] ] ] [AS nCodePage]
```

#### Parâmetros
 **FileName**
Especifica o nome do novo arquivo a ser criado. If you do not include a file extension, COPY TO assigns the default extension for the specified file type. If you do not specify a file type, COPY TO creates a new Visual FoxPro table and assigns the default .dbf extension to the table file name.
**DATABASE DatabaseName**
Especifica um banco de dados ao qual a nova tabela é adicionada.
**NAME LongTableName**
Especifica um nome longo para a nova tabela. Nomes longos podem conter até 128 caracteres e podem ser usados em vez de nomes curtos de arquivo no banco de dados.
**FIELDS FieldList**
Especifica quais campos são copiados para o novo arquivo. If you omit FIELDS FieldList , all fields are copied to the file. If the file you are creating is not a table, memo fields are not copied to the new file, even if memo field names are included in the field list.
**FIELDS LIKE Skeleton**
Especifica que campos da tabela original que correspondem ao esqueleto de campo Skeleton são incluídos no novo arquivo que COPY TO cria.
**FIELDS EXCEPT Skeleton**
Especifica que todos os campos, exceto os que correspondem ao esqueleto de campo Skeleton, são incluídos no novo arquivo que COPY TO cria.
**Scope**
Especifica um intervalo de registros a copiar para um arquivo. Apenas os registros dentro do intervalo são copiados. The scope clauses are: ALL , NEXT nRecords , RECORD nRecordNumber , and REST . Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses .
**FOR lExpression1**
Especifica que COPY TO copia apenas os registros para os quais a condição lógica lExpression1 é avaliada como True (.T.) para o arquivo. Para copiar registros condicionalmente, inclua a cláusula FOR lExpression1 para filtrar registros indesejados.
**WHILE lExpression2**
Especifica uma condição em que registros são copiados enquanto a expressão lógica lExpression2 é avaliada como True (.T.).
**[WITH] CDX | [WITH] PRODUCTION**
Cria um arquivo de índice estrutural para a nova tabela idêntico ao arquivo de índice estrutural da tabela existente. As tags e expressões de índice do arquivo de índice estrutural original são copiadas para o novo arquivo de índice estrutural. The CDX and PRODUCTION clauses are identical. No entanto, não inclua CDX ou PRODUCTION se estiver copiando para um arquivo que não seja uma nova tabela Visual FoxPro.
**NOOPTIMIZE**
Desabilita a Rushmore Query Optimization para COPY TO . For more information, see SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access .
**TYPE**
Especifica o tipo de arquivo se o arquivo que você cria não for uma tabela Visual FoxPro. Embora você deva especificar um tipo de arquivo, não precisa incluir a palavra-chave TYPE.
**FOXPLUS**
Visual FoxPro memo files have a different structure than Microsoft FoxBASE+™ memo files. If your source Visual FoxPro table contains a memo field, include the FOXPLUS clause to create a table that can be used in FoxBASE+. The Visual FoxPro memo field cannot contain binary data because FoxBASE+ does not support binary data in memo fields.
**FOX2X**
Creates a new table that can be opened in earlier versions of FoxPro (versions 2.0, 2.5, and 2.6). For Numeric, Float, Integer, Double, and Currency type fields, null values in the source table are converted to zero in the new table. For other field types, null values in the source table are converted to blanks in the new table. For further information about blank values, see ISBLANK( ) Function . The following table lists the Visual FoxPro field types that are converted to different field types in the new table when the FOX2X argument is included. Visual FoxPro field type FoxPro 2.x field type Blob Memo Currency Float DateTime Date Double Float Integer Numeric Varbinary Memo Varchar Memo
**DIF**
Creates a VisiCalc® .dif (Data Interchange Format) file. Fields from the Visual FoxPro table become vectors (columns) and records become tuples (rows). The new file name is assigned a .dif extension if you do not include an extension in FileName .
**MOD**
Creates a Microsoft Multiplan® version 4.01 file. The new Microsoft Multiplan file name is assigned a .mod extension if an extension is not included.
**SDF**
Creates an SDF (System Data Format) file. An SDF file is an ASCII text file in which records have a fixed length and end with a carriage return and line feed. Fields are not delimited. The SDF file name is assigned a .txt file extension if you do not include an extension. The SET CENTURY setting is ignored when creating SDF files with COPY TO . If SDF files include date data, it should be in YYYYMMDD format to allow effective reconversion into Visual FoxPro tables. If date information is stored in ambiguous formats, you should make sure that the dates are in YYYYMMDD format before you perform the COPY TO operation.
**SYLK**
Creates a SYLK (Symbolic Link) interchange file. SYLK files are used in Microsoft MultiPlan. Each field from the currently selected table becomes a column in the spreadsheet, and each record becomes a row. SYLK file names have no extension.
**WK1**
Creates a Lotus® 1-2-3® version 2.x spreadsheet file. Each field from the currently selected table becomes a column in the spreadsheet and each record becomes a row. A .wk1 file name extension is assigned to the new spreadsheet.
**WKS**
Creates a Lotus 1-2-3 version 1a spreadsheet file. Each field from the currently selected table becomes a column in the spreadsheet and each record becomes a row. A .wks file name extension is assigned to the new spreadsheet.
**WR1**
Creates a Lotus Symphony® version 1.1 or 1.2 spreadsheet file. Each field from the currently selected table becomes a column in the spreadsheet and each record becomes a row. A .wr1 file name extension is assigned to the new spreadsheet.
**WRK**
Creates a Lotus Symphony version 1.0 spreadsheet file. Each field from the currently selected table becomes a column in the spreadsheet and each record becomes a row. A .wr1 file name extension is assigned to the new spreadsheet.
**CSV**
Creates a comma separated value file. A CSV file has the field names as the first line in the file, and the field values in the remainder of the file are separated with commas.
**XLS**
Creates a Microsoft Excel version 2.0 worksheet file. Each field from the currently selected table becomes a column in the spreadsheet, and each record becomes a row. If you do not include a file extension, an .xls extension is assigned to the new worksheet. Note Though you can export a maximum of 65,535 rows, which includes one row reserved for the field header, versions of Excel earlier than 8.0 (Excel 97) display only the first 16,384 rows and cannot import files containing more than 32,767 rows.
**XL5**
Creates a Microsoft Excel version 5.0 workbook file. Each field from the currently selected table becomes a column in the spreadsheet, and each record becomes a row. If you do not include a file extension, an .xls extension is assigned to the new workbook. Note Though you can export a maximum of 65,535 rows, which includes one row reserved for the field header, versions of Excel earlier than 8.0 (Excel 97) display only the first 16,384 rows and cannot import files containing more than 32,767 rows.
**DELIMITED**
Creates a delimited file. A delimited file is an ASCII text file in which each record ends with a carriage return and line feed. The default field separator is a comma. Because character data can include commas, character fields are additionally delimited with double quotation marks. Unless you specify otherwise, a .txt extension is assigned to all newly created DELIMITED files.
**DELIMITED WITH Delimiter**
Creates a delimited file with character fields delimited by a character other than a quotation mark. The character that delimits character fields is specified with Delimiter .
**DELIMITED WITH BLANK**
Creates a delimited file with fields separated by spaces instead of commas.
**DELIMITED WITH TAB**
Creates a delimited file with fields separated by tabs instead of commas.
**DELIMITED WITH CHARACTER Delimiter**
Creates a delimited file with all fields enclosed by the character specified with Delimiter . If Delimiter is a semicolon (;), used in Visual FoxPro to indicate command line continuation, enclose the semicolon in quotation marks. You can also specify the BLANK and TAB keywords for Delimiter. You can combine the WITH Delimiter clause with the WITH CHARACTER clause. For example, the following command creates a text file with character fields enclosed by underscores and all fields delimited from each other with semicolons: COPY TO mytxt.txt DELIMITED WITH _ WITH CHARACTER ';'
**AS nCodePage**
Especifica a página de código para a tabela ou arquivo que COPY TO cria. Visual FoxPro copies the contents of the currently selected table, and, as it copies the data, automatically converts the data to the code page you specify for the new table or file. If possible, Visual FoxPro marks the newly created table or file with the code page you specify. If you omit AS nCodePage , the newly created table or file is converted to the current Visual FoxPro code page.

# Observações

O esqueleto de campo Skeleton suporta curingas. For example, to specify that all fields that begin with the letters A and P are included in the new file, use the following:

```foxpro
COPY TO mytable FIELDS LIKE A*,P*
```

The LIKE clause can be combined with the EXCEPT clause:

```foxpro
COPY TO mytable FIELDS LIKE A*,P* EXCEPT PARTNO*
```

A Rushmore Query Optimization otimiza COPY TO com uma cláusula FOR lExpression1 se lExpression1 for uma expressão otimizável. Para obter o melhor desempenho, use uma expressão otimizável na cláusula FOR lExpression1. For information on Rushmore optimizable expressions, see SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access.

Se uma ordem de índice estiver definida, os registros são copiados na ordem do índice mestre.

Se você especificar um valor para nCodePage que não é suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar a função GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para a tabela ou arquivo que o Visual FoxPro cria.

O comando COPY TO preserva configurações de autoincremento, exceto nas seguintes condições:
 - Quando a lista de campos especificada usando COPY TO...FIELDS não inclui o campo que usa autoincremento.
- Ao usar a cláusula TYPE no comando COPY TO, independentemente do tipo especificado pela cláusula.

A tabela de destino começa a autoincrementar a partir do NextValue da tabela de origem. Por exemplo, suponha que o NextValue na tabela de origem seja 1000 com um valor Step de 1. A primeira linha da tabela de destino então tem um valor de campo autoincrementado de 1001; a segunda linha tem um valor de 1002, e assim por diante.

Ao usar o comando COPY TO, esteja ciente de que o SET VARCHARMAPPING Command afetará campos calculados (expressões de caractere de comprimento variável) definidos pelo SET FIELDS Command.

# Exemplo

No exemplo a seguir, a tabela Customer é aberta e os próximos três registros são copiados para um novo arquivo de dados DELIMITED chamado Temp.txt.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer  && Opens Customer table.
COPY NEXT 3 TO Temp TYPE DELIMITED
WAIT WINDOW 'This is the delimited text file' NOWAIT
MODIFY FILE Temp.txt
DELETE FILE Temp.txt
```
