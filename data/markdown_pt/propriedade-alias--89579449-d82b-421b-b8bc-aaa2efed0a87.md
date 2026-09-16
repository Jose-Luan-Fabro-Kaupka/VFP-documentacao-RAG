# Propriedade Alias

Especifica um nome de alias para o objeto apropriado. Leitura/gravação em tempo de design e em tempo de execução.

A propriedade Alias imita o comportamento da cláusula ALIAS no comando USE. Existem várias versões desta sintaxe.

```foxpro
DataEnvironment.Cursor.Alias [= cText]
```

```foxpro
CursorAdapter.Alias [= cText]
```

```foxpro
XMLTable.Alias [= cText]
```

```foxpro
XMLTable.XMLField.Alias [= cText]
```

# Valor de retorno
 **cText**
Tipo de dados caractere. A tabela a seguir descreve os valores para cText , dependendo do objeto. Objeto cText Cursor Nome de alias para cada tabela ou view associada ao cursor. CursorAdapter Nome de alias para o cursor gerado pela propriedade SelectCmd. XMLTable Nome de alias para o cursor do Visual FoxPro. Se cText for uma cadeia vazia (""), o método ToXML do XMLAdapter adiciona o esquema da tabela, mas não adiciona nenhum dado. XMLField Nome de alias para o nome do campo no cursor do Visual FoxPro. Se cText for uma cadeia vazia (""), os métodos ToCursor e ApplyDiffGram do XMLTable desconsideram o campo.

# Observações

Aplica-se a: Objeto Cursor | Classe CursorAdapter | Classe XMLTable | Classe XMLField

Para objetos Cursor, quando o Visual FoxPro carrega o ambiente de dados, ele atribui um nome de alias que é o mesmo que o nome da tabela ou view a cada tabela ou view associada ao cursor por padrão. Você pode alterar a propriedade Alias para substituir o nome de alias padrão.

Para objetos CursorAdapter, o Visual FoxPro usa a propriedade Alias para resolver o nome de alias correto para tabelas e campos que você arrasta e solta no formulário do ambiente de dados em tempo de design. Se você não especificar valores para Alias, o Visual FoxPro gera um erro e, em tempo de execução, usa os aliases padrão para as tabelas e campos.

Para objetos XMLTable e XMLField, o Visual FoxPro carrega o valor da propriedade XMLName na propriedade Alias correspondente para esses objetos por padrão. Se a propriedade Alias do XMLField estiver vazia, o método ToCursor do XMLTable desconsidera os objetos XMLField e cria um cursor que não inclui nenhum campo especificado por esses objetos XMLField.

Se você alterar a propriedade Alias, o Visual FoxPro também renomeia o cursor criado pelo método ToCursor e as propriedades Alias para objetos XMLTable e XMLField.

Ao executar o método ToXML, o Visual FoxPro usa a propriedade XMLName em vez da propriedade Alias.
