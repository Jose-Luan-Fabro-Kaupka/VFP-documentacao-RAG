# Comando COPY STRUCTURE EXTENDED

Cria uma nova tabela com campos contendo a estrutura da tabela selecionada no momento.

```foxpro
COPY STRUCTURE EXTENDED TO FileName
   [DATABASE DatabaseName [NAME LongTableName]] [FIELDS FieldList]
```

#### Parâmetros
 **FileName**
Especifica a nova tabela a ser criada.
**DATABASE DatabaseName**
Especifica um banco de dados ao qual a nova tabela será adicionada.
**NAME LongTableName**
Especifica um nome longo para a nova tabela. Nomes longos podem conter até 128 caracteres e podem ser usados em vez de nomes de arquivo curtos no banco de dados.
**FIELDS FieldList**
Especifica que somente os campos em FieldList são incluídos em um registro na nova tabela. Se você omitir FIELDS FieldList, todos os campos terão um registro na nova tabela.

# Observações

Informações sobre cada campo na tabela selecionada no momento são copiadas para um registro na nova tabela. A estrutura da nova tabela tem um formato fixo e consiste em 18 campos. A tabela a seguir lista os nomes dos campos e seus conteúdos.

| Campo | Tipo de campo | Conteúdo |
| --- | --- | --- |
| FIELD_NAME | Character | Nomes de campos da tabela selecionada (128 caracteres de largura) |
| FIELD_TYPE | Character | Tipos de campo: Blob Character Currency Date DateTime Double Float General Integer Logical Memo Numeric Varchar e Varchar (Binary) Varbinary |
| FIELD_LEN | Numeric | Larguras de campo |
| FIELD_DEC | Numeric | Número de casas decimais em campos numéricos |
| FIELD_NULL | Logical | Suporte a valor nulo de campo |
| FIELD_NOCP | Logical | Tradução de página de código não permitida (somente campos character e memo) |
| FIELD_DEFA | Memo | Valores padrão de campo |
| FIELD_RULE | Memo | Regras de validação de campo |
| FIELD_ERR | Memo | Texto de validação de campo |
| TABLE_RULE | Memo | Regra de validação de tabela |
| TABLE_ERR | Memo | Texto de validação de tabela |
| TABLE_NAME | Character | Nome longo da tabela (somente no primeiro registro) |
| INS_TRIG | Memo | Expressão de trigger de inserção (somente no primeiro registro) |
| UPD_TRIG | Memo | Expressão de trigger de atualização (somente no primeiro registro) |
| DEL_TRIG | Memo | Expressão de trigger de exclusão (somente no primeiro registro) |
| TABLE_CMT | Memo | Comentário da tabela (somente no primeiro registro) |
| FIELD_NEXT | Numeric | Próximo valor para campo AUTOINC, se habilitado. |
| FIELD_STEP | Numeric | Valor de incremento para campo AUTOINC. Se o valor é 0, o autoincremento não está habilitado para o campo. |

A largura do campo FIELD_NAME é de 10 caracteres em versões anteriores do Visual FoxPro, FoxPro for Windows e FoxPro for MS-DOS. Para usar CREATE FROM com uma tabela criada por COPY STRUCTURE EXTENDED no Visual FoxPro 5.0 e anteriores, você deve alterar a largura do campo FIELD_NAME para 10 caracteres. Alguns tipos de campo não são suportados no Visual FoxPro 3.0 e versões anteriores.

Se os campos na tabela de origem usam autoincremento, FIELD_STEP é um valor diferente de zero.

Você pode modificar a tabela recém-criada e usar o comando CREATE FROM para criar uma nova tabela com uma estrutura diferente. Os comandos COPY STRUCTURE e CREATE FROM permitem alterar programaticamente a estrutura de uma tabela.

# Exemplo

O exemplo a seguir exibe a estrutura da tabela `Orders`, copia a estrutura extendida para uma tabela `Temp`, navega em `Temp`, cria uma tabela chamada `Backup` a partir de `Temp` e exibe a estrutura de `Backup`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Orders  && Opens Orders table.
CLEAR
DISPLAY STRUCTURE
WAIT WINDOW 'Structure of the Orders table' NOWAIT
COPY STRUCTURE EXTENDED TO Temp
USE Temp
WAIT WINDOW 'The Temp table - 1 row per field in orders' NOWAIT
BROWSE
CREATE Backup FROM Temp
USE Backup
DISPLAY STRUCTURE
WAIT WINDOW 'Backup.dbf has the same structure as Orders' NOWAIT
USE
DELETE FILE Temp.dbf
DELETE FILE Backup.dbf
```
