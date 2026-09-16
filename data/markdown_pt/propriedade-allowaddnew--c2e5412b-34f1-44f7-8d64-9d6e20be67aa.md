# Propriedade AllowAddNew

Especifica se novos registros podem ser adicionados a uma tabela a partir de um grid. Disponível em tempo de design e em tempo de execução.

```foxpro
Grid.AllowAddNew[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: Configuração Descrição True (.T.) Novos registros podem ser adicionados a uma tabela a partir de um grid. False (.F.) (Padrão) Novos registros não podem ser adicionados a uma tabela a partir de um grid.

# Observações

Aplica-se a: Grid Control

Se AllowAddNew estiver definido como True (.T.), você pode adicionar um novo registro a uma tabela em um grid pressionando a seta para baixo enquanto estiver posicionado no último registro do grid, desde que o grid seja de leitura/gravação. Novos registros não podem ser adicionados a partir do grid se o grid for somente leitura (se o RecordSourceType for uma consulta, uma tabela for somente leitura, e assim por diante).
