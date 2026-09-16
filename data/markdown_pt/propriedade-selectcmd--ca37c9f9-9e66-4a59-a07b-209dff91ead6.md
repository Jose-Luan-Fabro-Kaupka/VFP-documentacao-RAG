# Propriedade SelectCmd

Especifica o comando para recuperar dados da fonte de dados na propriedade CursorAdapter DataSourceType Property. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.SelectCmd [ = cCommand ]
```

# Valor de retorno
 **cCommand**
Especifica uma cadeia de caracteres ou expressão que avalia para uma cadeia de comando válida. Para fontes de dados XML, cCommand deve ser um dos seguintes: Uma expressão que avalia para uma fonte XML válida para a função XMLTOCURSOR( ). XMLTOCURSOR( ) recupera os dados. Uma expressão que avalia para um objeto XMLTable. O método ToCursor do XMLTable recupera os dados.

# Observações

Aplica-se a: Classe CursorAdapter

Se a propriedade CursorAdapter UseDeDataSource é True (.T.) e o cursor adapter é membro do ambiente de dados, as propriedades DataSource e DataSourceType do DataEnvironment substituem as propriedades relevantes do CursorAdapter.
