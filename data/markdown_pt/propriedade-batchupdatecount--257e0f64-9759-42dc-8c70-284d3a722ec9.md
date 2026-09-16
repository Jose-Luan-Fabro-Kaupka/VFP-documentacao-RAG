# Propriedade BatchUpdateCount

Especifica o número de instruções de atualização enviadas à fonte de dados remota para tabelas com buffer. Ao trabalhar com esta propriedade em cursores comuns, use as funções CURSORSETPROP() e CURSORGETPROP(). Leitura/gravação.

Ajustar BatchUpdateCount pode aumentar drasticamente o desempenho da atualização automática.

> **Observação:** Definir BatchUpdateCount para objetos CursorAdapter substitui a configuração da propriedade de um cursor anexado a um objeto CursorAdapter. Portanto, alterar as configurações do cursor com CURSORSETPROP() não produz efeito.

```foxpro
CursorAdapter.BatchUpdateCount [ = nValue]
```

# Valor de retorno
 **nValue**
Tipo de dado Numeric. O parâmetro nValue tem valor padrão 1. Observação Ao atualizar dados com Table Buffering e atualizar a(s) tabela(s) da fonte de dados a partir de vários clientes, evite definir BatchUpdateCount com valor maior que 1. Nesses cenários, TABLEUPDATE( ) sempre retorna True (.T.). Você pode definir BatchUpdateCount com segurança como um valor maior que 1 para operações INSERT, UPDATE e DELETE quando lForce em TABLEUPDATE( ) estiver definido como True (.T.).

# Observações

Aplica-se a: classe CursorAdapter

BatchUpdateCount aplica-se a objetos CursorAdapter somente quando o tipo da fonte de dados dos comandos SQL INSERT, UPDATE e DELETE é um dos seguintes:
 - "ODBC" Além disso, o mesmo identificador de conexão deve ser usado como fonte de dados dos comandos SQL INSERT, UPDATE e DELETE. Observação A fonte e o tipo da fonte de dados podem ser herdados das propriedades DataSource e DataSourceType do objeto CursorAdapter ou DataEnvironment.
- "ADO" O mesmo objeto ADODB Command deve ser usado como fonte de dados dos comandos SQL INSERT, UPDATE e DELETE. Recomenda-se definir explicitamente as propriedades InsertCmdDataSource, InsertCmdDataSourceType, UpdateCmdDataSource, UpdateCmdDataSourceType, DeleteCmdDataSource e DeleteCmdDataSourceType, pois a herança não funciona nesse cenário.
- "XML" Recomenda-se definir explicitamente as propriedades InsertCmdDataSource, InsertCmdDataSourceType, UpdateCmdDataSource, UpdateCmdDataSourceType, DeleteCmdDataSource e DeleteCmdDataSourceType, pois a herança não funciona nesse cenário.

Se BatchUpdateCount for maior que 1, o Visual FoxPro atualizará o lote executando a propriedade UpdateCmd uma vez por lote.

> **Observação:** Se a atualização em lote for usada, os eventos BeforeInsert, AfterInsert, BeforeUpdate, AfterUpdate, BeforeDelete e AfterDelete não serão disparados. Se uma atualização de lote falhar, o Visual FoxPro tentará enviar uma atualização separada para cada linha do lote; no entanto, os eventos continuarão sem ser disparados.
