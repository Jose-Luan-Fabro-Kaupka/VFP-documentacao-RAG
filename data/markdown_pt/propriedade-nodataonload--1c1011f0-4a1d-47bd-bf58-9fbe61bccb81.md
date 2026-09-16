# Propriedade NoDataOnLoad

Faz com que a view associada a um Cursor seja ativada sem baixar dados. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
DataEnvironment.Cursor.NoDataOnLoad[ = lExpr]
```

# Valor de retorno
 **lExpr**
Configurações: True (.T.), abre a view associada ao Cursor sem baixar dados. False (.F.) (Padrão), abre a view associada ao Cursor com dados.

# Observações

Aplica-se a: objeto Cursor

> **Observação:** Quando o objeto Cursor é acessado por CURSORSETPROP(), a propriedade NoDataOnLoad é somente leitura em tempo de execução.

Use NoDataOnLoad para garantir que o FormSet ou Form associado à view seja carregado rapidamente, pois baixar dados de um servidor de backend pode ser demorado. Você pode usar REQUERY( ) com NoDataOnLoad para baixar dados na view ativa depois que o Form for carregado.

NoDataOnLoad reproduz o comportamento da cláusula NODATA de USE.
