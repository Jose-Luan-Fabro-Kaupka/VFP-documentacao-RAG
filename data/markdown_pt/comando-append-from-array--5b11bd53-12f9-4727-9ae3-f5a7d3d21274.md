# Comando APPEND FROM ARRAY

Adiciona um registro à tabela atualmente selecionada para cada linha em um array e preenche cada registro com dados da linha correspondente do array.

```foxpro
APPEND FROM ARRAY ArrayName [FOR lExpression]
   [FIELDS FieldList | FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton]
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array que contém os dados a serem copiados para os novos registros. Novos registros são adicionados à tabela até que todas as linhas do array sejam anexadas.
**FOR lExpression**
Especifica uma condição para anexar registros do array. lExpression deve conter o nome de um campo de destino em sua expressão condicional. Antes de uma linha do array ser anexada a um registro na tabela, o elemento do array correspondente ao campo de destino especificado em lExpression é verificado para determinar se esse elemento do array atende à condição em lExpression. Se o elemento do array satisfizer a condição, um registro é anexado. Se o elemento do array não satisfizer a condição, a linha do array não é anexada e a próxima linha do array é verificada para determinar se atende à condição.
**FIELDS FieldList**
Especifica que somente os campos em FieldList são atualizados a partir do array. O primeiro campo na lista é atualizado com o conteúdo do primeiro elemento no array, o segundo campo é atualizado a partir do segundo elemento, e assim por diante.
**FIELDS LIKE Skeleton**
Especifica que os campos que correspondem ao esqueleto de campo Skeleton são atualizados a partir do array.
**FIELDS EXCEPT Skeleton**
Especifica que todos os campos, exceto aqueles que correspondem ao esqueleto de campo Skeleton, são atualizados a partir do array. O esqueleto de campo Skeleton suporta curingas. Por exemplo, para especificar que todos os campos que começam com as letras A e P são atualizados a partir do array, use o seguinte: APPEND FROM ARRAY aMyArray FIELDS LIKE A*,P* A cláusula LIKE pode ser combinada com a cláusula EXCEPT: APPEND FROM ARRAY aMyArray FIELDS LIKE A*,P* EXCEPT PARTNO*

# Observações

Campos Memo, General e Blob são ignorados em APPEND FROM ARRAY.

Quando uma tabela está aberta para uso compartilhado, APPEND FROM ARRAY bloqueia o cabeçalho da tabela enquanto os registros estão sendo adicionados.

Se o array é unidimensional, APPEND FROM ARRAY adiciona um registro à tabela. O conteúdo do primeiro elemento do array preenche o primeiro campo do registro recém-adicionado, o conteúdo do segundo elemento do array preenche o segundo campo do registro, e assim por diante.

Se o array unidimensional tem mais elementos do que a tabela tem campos, os elementos adicionais são ignorados. Se a tabela tem mais campos do que o array tem elementos, os campos adicionais são inicializados com o valor vazio padrão. A seguir estão os valores vazios padrão para cada tipo de campo:

| Tipo de campo | Valor padrão |
| --- | --- |
| Character | Espaços |
| Currency | 0 |
| Date | Data vazia (por exemplo, CTOD("")) |
| DateTime | DateTime vazio (por exemplo, CTOT("")) |
| Double | 0 |
| Float | 0 |
| Integer | 0 |
| Logical | False (.F.) |
| Memo | Vazio (sem conteúdo) |
| Numeric | 0 |

Se o array é bidimensional, APPEND FROM ARRAY adiciona um novo registro à tabela para cada linha no array. Por exemplo, se o array tem quatro linhas, quatro novos registros são anexados à tabela.

O conteúdo da primeira coluna do array preenche o primeiro campo dos registros recém-adicionados, a segunda coluna do array preenche o segundo campo dos novos registros, e assim por diante. Por exemplo, se o array tem quatro linhas e três colunas, os elementos da primeira coluna do array preenchem o primeiro campo em cada um dos quatro novos registros anexados à tabela.

Se o array bidimensional tem mais colunas do que a tabela tem campos, as colunas adicionais são ignoradas. Se a tabela tem mais campos do que o array tem colunas, os campos adicionais são inicializados com valores vazios.

APPEND FROM ARRAY pode preencher um campo mesmo se o tipo de dados do elemento correspondente do array não corresponder ao tipo de dados do campo, desde que os dados do elemento do array sejam compatíveis com o tipo de dados do campo correspondente. Se os dados não são compatíveis, o campo é inicializado com um valor vazio.

Se a tabela de destino usa autoincremento, APPEND FROM ARRAY falha se o comando SET AUTOINCERROR estiver ON, a menos que a opção FIELDS seja usada para omitir a coluna AUTOINC. Definir AUTOINCERROR como OFF ou desativar o autoincremento na tabela de destino usando a função CURSORSETPROP( ) permite que APPEND FROM ARRAY seja bem-sucedido. O campo ou campos de autoincremento da tabela de destino são incrementados de acordo com os valores especificados, e os valores na tabela de origem não são aplicados.

# Exemplo

Este exemplo cria uma tabela e depois usa APPEND FROM ARRAY para anexar um registro à nova tabela.

```foxpro
LOCAL ARRAY aNewRec(3)
* Create the table
CREATE TABLE Test FREE  (Object C(10), Color C(16), SqFt n(6,2))
SCATTER TO aNewRec BLANK  && Create a new array from the table
aNewRec[1]="Box"         && Fill the array
aNewRec[2]="Red"
aNewRec[3]=12.5
APPEND FROM ARRAY aNewRec   && Add record containing array contents
          && to the table
```
