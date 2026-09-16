# Propriedade AutoCloseTables

Especifica se as tabelas ou views especificadas pelo data environment são fechadas quando o form set, formulário ou relatório é liberado. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
DataEnvironment.AutoCloseTables[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade AutoCloseTables são: Configuração Descrição True (.T.) (Padrão) Fecha as tabelas e views quando o form set, formulário ou relatório é liberado. False (.F.) Tabelas e views permanecem abertas quando o form set, formulário ou relatório é liberado.

# Observações

Aplica-se a: DataEnvironment Object

Se AutoCloseTables estiver definida como false (.F.) e o form set, formulário ou relatório não estiver executando em uma sessão de dados privada, as tabelas e views associadas a Cursors no data environment permanecem abertas depois que o form set, formulário ou relatório é liberado. Em todos os outros casos, as tabelas e views associadas a Cursors no data environment são fechadas.
