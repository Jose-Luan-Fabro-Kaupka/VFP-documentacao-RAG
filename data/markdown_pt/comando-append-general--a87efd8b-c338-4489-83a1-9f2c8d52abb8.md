# Comando APPEND GENERAL

Importa um objeto OLE de um arquivo e o coloca em um campo general.

```foxpro
APPEND GENERAL GeneralFieldName [FROM FileName]
   [DATA cExpression] [LINK] [CLASS OLEClassName]
```

#### Parâmetros
 **GeneralFieldName**
Especifica o nome do campo general no qual o objeto OLE é colocado. Você pode especificar um campo general em uma tabela aberta em uma área de trabalho não atual incluindo o alias da tabela com o nome do campo.
**FROM FileName**
Especifica o arquivo que contém o objeto OLE. Você deve incluir o nome completo do arquivo, incluindo sua extensão. Se o arquivo estiver localizado em um diretório diferente do diretório padrão atual, inclua o caminho com o nome do arquivo.
**DATA cExpression**
Especifica uma expressão de caracteres que é avaliada e passada como uma cadeia de caracteres para o objeto OLE no campo general. O objeto OLE deve ser capaz de receber e processar a cadeia de caracteres. Por exemplo, você não pode enviar uma cadeia de caracteres para um objeto gráfico como um criado usando Paintbrush.
**LINK**
Cria um vínculo entre o objeto OLE e o arquivo que contém o objeto. O objeto OLE aparece no campo general, mas a definição do objeto permanece no arquivo. Se você omitir LINK, o objeto OLE é incorporado no campo general.
**CLASS OLEClassName**
Especifica uma classe OLE para um objeto OLE diferente da classe padrão. Você pode especificar um nome de classe quando a extensão do arquivo que contém o objeto OLE for diferente da extensão padrão e você desejar forçar o comportamento da classe. Se a extensão padrão puder ser usada por vários Automation servers, inclua a classe para especificar um servidor específico.

# Observações

Se um objeto OLE já existir no campo general, ele é substituído pelo objeto OLE do arquivo. Para remover um objeto OLE de um campo general, emita APPEND GENERAL GeneralFieldName (GeneralFieldName é o nome do campo general a limpar) sem argumentos adicionais.

Para informações adicionais sobre objetos OLE no Visual FoxPro, consulte Sharing Information and Adding OLE.

# Exemplo

O exemplo a seguir importa um gráfico Microsoft Excel no diretório Excel para um campo general chamado `mygenfield`.

```foxpro
CREATE TABLE MyGenTbl (mygenfield G)
APPEND BLANK  && Add a blank record
APPEND GENERAL mygenfield FROM C:\EXCEL\BOOK1.XLS CLASS EXCELCHART
```
