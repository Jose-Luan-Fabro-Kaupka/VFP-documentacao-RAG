# Propriedade CursorSchema

Especifica a estrutura do cursor associado a um objeto CursorAdapter. Leitura/gravação em tempo de design e em tempo de execução.

CursorSchema é essencialmente a porção "entre os parênteses" dos comandos SQL CREATE TABLE - SQL Command e CREATE CURSOR - SQL Command. No Visual FoxPro 8.0, você pode usar CursorSchema para definir uma fonte de dados XML. No Visual FoxPro 9.0, você pode usar CursorSchema para definir fontes de dados XML, Native, ADO e ODBC.

> **Observação:** No Visual FoxPro 9.0, valores DEFAULT e restrições CHECK em nível de tabela e de campo são suportados para fontes de dados XML, Native, ADO e ODBC. No Visual FoxPro 8.0, valores DEFAULT e restrições CHECK em nível de tabela e de campo são suportados apenas para uma fonte de dados XML. Para que os valores DEFAULT e as restrições CHECK sejam aplicados a um cursor, chame o método CursorFill com o parâmetro lUseSchema definido como True (.T.).

O Visual FoxPro usa a propriedade CursorSchema em tempo de design para determinar a estrutura do cursor a ser colocado na superfície do Data Environment Designer. O Visual FoxPro usa CursorSchema em tempo de execução se especificado pelo método CursorFill.

> **Observação:** Você deve garantir que CursorSchema corresponda e mapeie as colunas da fonte de dados de maneira aceitável.

```foxpro
CursorAdapter.CursorSchema [ = cList ]
```

# Valor de retorno
 **cList**
Tipo de dados Character. O parâmetro cList especifica uma cadeia de caracteres ou expressão que avalia para uma lista válida separada por vírgulas de nomes e tipos de campo. Por exemplo: CursorAdapter.CursorSchema = ; "col1 I, col2 Character(25), col3 M, col4 Currency, col5 n(12,3)" Consulte CREATE CURSOR - SQL Command para uma lista de nomes e tipos de campo. Se CursorSchema estiver vazio ou definido como null (.NULL.), o Visual FoxPro usa a fonte de dados do objeto CursorAdapter para determinar a estrutura do cursor.

# Observações

Aplica-se a: CursorAdapter Class

Quando o parâmetro lUseCursorSchema no método CursorFill avalia para True (.T.), ou quando você adiciona um cursor baseado em CursorAdapter à superfície do Data Environment Designer, um objeto CursorAdapter usa CursorSchema como modelo para o cursor criado por CursorFill.

Para fontes de dados ADO, CursorSchema suporta mapeamento de tipos ADO para tipos de dados do Visual FoxPro. Para obter mais informações, consulte Data Type Conversion Control.
