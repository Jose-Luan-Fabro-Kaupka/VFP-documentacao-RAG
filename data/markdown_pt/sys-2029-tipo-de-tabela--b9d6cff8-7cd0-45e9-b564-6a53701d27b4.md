# SYS(2029) - Tipo de tabela

Retorna um valor correspondente ao tipo de tabela.

```foxpro
SYS(2029 [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho na qual a tabela está aberta.
**cTableAlias**
Especifica o alias da tabela. Se você omitir nWorkArea e cTableAlias, SYS(2029) retorna um valor para a tabela aberta na área de trabalho atualmente selecionada.

# Valor de retorno

Caractere

# Observações

A tabela a seguir lista os valores retornados por SYS(2029) e o tipo de tabela correspondente:

| Valor de retorno | Tipo de tabela |
| --- | --- |
| 0 | Nenhuma tabela aberta. |
| 3 | Versões anteriores do FoxPro, FoxBASE+, dBASE III PLUS e dBASE IV sem campo memo. |
| 48 | Visual FoxPro com ou sem campo memo. |
| 49 | Visual FoxPro com campo Autoinc (Visual FoxPro 8 e superior). |
| 50 | Visual FoxPro com campo Varchar, Varbinary ou Blob (Visual FoxPro 9 e superior). |
| 67 | Tabela dBASE IV SQL sem campo memo. |
| 99 | Tabela de sistema dBASE IV SQL sem campo memo. |
| 131 | Tabela FoxBASE+ e dBASE III PLUS com campo memo. |
| 139 | Tabela dBASE IV com campo memo. |
| 203 | Tabela dBASE IV SQL com campo memo. |
| 245 | Versões anteriores do FoxPro com campo memo. |

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open customer table
CLEAR
DO CASE
   CASE SYS(2029) = '3'
      ? 'Previous versions of FoxPro'
   CASE SYS(2029) = '48'
      ? 'Visual FoxPro Table'
   CASE SYS(2029) = '67'
      ? 'dBASE IV SQL table, no memo fields'
   CASE SYS(2029) = '99'
      ? 'dBASE IV SQL System table with no memo field'
   CASE SYS(2029) = '131'
      ? 'FoxBASE+ table with a memo field'
   CASE SYS(2029) = '139'
      ? 'dBASE IV table with a memo field'
   CASE SYS(2029) = '203'
      ? 'dBASE IV SQL table with a memo field'
   CASE SYS(2029) = '245'
      ? 'Previous versions of FoxPro with a memo field'
ENDCASE
```
