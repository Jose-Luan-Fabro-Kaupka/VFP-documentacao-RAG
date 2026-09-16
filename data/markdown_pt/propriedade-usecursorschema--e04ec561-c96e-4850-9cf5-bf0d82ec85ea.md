# Propriedade UseCursorSchema

Especifica uma configuração padrão a ser usada para o parâmetro lUseCursorSchema no método CursorFill. Disponível em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UseCursorSchema [ = lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir especifica os valores de lValue . lValue Descrição False (.F.) (Padrão) Um False (.F.) lógico é usado por padrão para o parâmetro lUseCursorschema no método CursorFill. CursorFill cria o cursor usando os tipos de dados normalmente determinados pelo Visual FoxPro de acordo com a propriedade DataSourceType do CursorAdapter . True (.T.) Um True (.T.) lógico é usado por padrão para o parâmetro lUseCursorschema no método CursorFill.

# Observações

Aplica-se a: classe CursorAdapter.

O valor especificado por esta propriedade é usado pelo método CursorFill quando o parâmetro lUseCursorSchema é omitido no método. Esta propriedade é ignorada se o parâmetro lUseCursorSchema estiver incluído no método CursorFill.
