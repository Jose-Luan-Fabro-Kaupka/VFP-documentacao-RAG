# Propriedade NoData

Especifica o valor padrão para o parâmetro lNoData do método CursorFill. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.NoData [ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade NoData são: Configuração Descrição True (.T.) Define o valor padrão do parâmetro lNoData do método CursorFill como um valor lógico True (.T.). Se o método CursorFill é chamado sem o parâmetro lNoData, o cursor é criado, mas não é preenchido com dados. False (.F.) (Padrão) Define o valor padrão do parâmetro lNoData do método CursorFill como um valor lógico False (.F.). Se o método CursorFill é chamado sem o parâmetro lNoData, o cursor é criado e é preenchido com dados.

# Observações

Aplica-se a: CursorAdapter Class.

O valor especificado por esta propriedade é usado pelo método CursorFill quando o parâmetro lNoData é omitido no método. Esta propriedade é ignorada se o parâmetro lNoData estiver incluído no método CursorFill.
