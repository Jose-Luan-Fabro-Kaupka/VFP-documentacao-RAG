# Propriedade AllowSimultaneousFetch

Especifica se deve permitir busca simultânea para cursores Open Database Connectivity (ODBC) ao usar uma conexão compartilhada. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** AllowSimultaneousFetch se aplica somente quando a propriedade CursorAdapter DataSourceType está definida como "ODBC". Se a conexão associada não for compartilhada, definir AllowSimultaneousFetch não tem efeito.

```foxpro
CursorAdapter.AllowSimultaneousFetch [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir especifica os valores de lValue . lValue Descrição False (.F.) Ao usar uma conexão compartilhada, cursores configurados de forma semelhante que compartilham a conexão não têm permissão para buscar registros simultaneamente. (Padrão) True (.T.) Ao usar uma conexão compartilhada, cursores configurados de forma semelhante que compartilham a conexão têm permissão para buscar registros simultaneamente.

# Observações

Aplica-se a: CursorAdapter Class
