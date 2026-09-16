# Função ISBLANK( )

Determina se uma expressão está em branco.

```foxpro
ISBLANK(eExpression)
```

#### Parâmetros
 **eExpression**
Especifica a expressão que ISBLANK( ) deve avaliar. eExpression pode ser um campo em uma tabela, uma variável ou elemento de array, ou uma expressão.

# Valor de retorno

Logical. ISBLANK( ) retorna True (.T.) se a expressão eExpression estiver em branco; caso contrário, ISBLANK( ) retorna False (.F.).

ISBLANK( ) retorna True (.T.) para campos quando esses campos contêm determinados valores. A tabela a seguir lista os valores que os tipos de campo contêm para ISBLANK( ) retornar True.

| Tipo de dados | Valores que o campo contém |
| --- | --- |
| Blob | Vazio (0h) ou contém apenas bytes zero, por exemplo, 0h00, 0h000000, e assim por diante |
| Character | Cadeia de caracteres vazia, espaços ou nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| Date | Data em branco ({ / / }) ou nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| DateTime | DateTime em branco ({ / / : : }) ou nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| Float | Nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| General | Vazio, por exemplo, nenhum objeto OLE |
| Logical | Nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| Memo | Vazio, por exemplo, nenhum conteúdo de memo |
| Numeric | Nenhum valor, como um registro em branco recém-anexado ou limpo com BLANK |
| Varbinary | Vazio (0h) ou contém apenas bytes zero, por exemplo, 0h00, 0h000000, e assim por diante |

> **Observação:** Expressões com tipo Currency, Integer ou Double nunca estão em branco; portanto, ISBLANK( ) sempre retorna False (.F.) para esses tipos de expressão.

# Observações

Para criar um registro em branco, use os comandos APPEND BLANK e BLANK. Você também pode usar BLANK para limpar dados de campos em um registro.

ISBLANK( ) difere de EMPTY( ) e ISNULL( ). Por exemplo, EMPTY( ) retorna True (.T.) se uma expressão de caracteres avaliar como vazia, por exemplo, contém espaços, tabulações, retornos de carro ou quebras de linha. ISBLANK( ) retorna True (.T.) se a expressão de caracteres contém apenas a cadeia de caracteres vazia ("") ou espaços.

# Exemplo

No exemplo a seguir, uma tabela chamada `mytable` é criada e um registro em branco é anexado. ISBLANK( ) retorna True (.T.) porque `myfield` está em branco. Um valor é colocado em `myfield`, e ISBLANK( ) retorna False (.F.) porque `myfield` não está mais em branco.

```foxpro
CREATE TABLE mytable FREE (myfield C(20))
APPEND BLANK  && Add new blank record
CLEAR
? ISBLANK(myfield)  && Displays .T.
REPLACE myfield WITH 'John Smith'  && Insert a value in the field
? ISBLANK(myfield)  && Displays .F.
```
