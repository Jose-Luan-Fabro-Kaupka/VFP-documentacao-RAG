# Comando GATHER

Substitui os dados do registro atual da tabela selecionada por dados de uma matriz, um conjunto de variáveis ou um objeto.

```foxpro
GATHER FROM ArrayName | MEMVAR | NAME ObjectName
   [FIELDS FieldList | FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton]
   [MEMO]
```

#### Parâmetros
 **FROM ArrayName**
Especifica a matriz cujos dados substituem os do registro atual. A partir do primeiro elemento, cada conteúdo substitui o campo correspondente. Se houver menos elementos que campos, os campos adicionais serão ignorados; se houver mais elementos, os elementos adicionais serão ignorados.
**MEMVAR**
Especifica as variáveis ou a matriz das quais os dados são copiados. Os dados são transferidos da variável para o campo de mesmo nome. O campo não é substituído se não existir uma variável correspondente. Dica: você pode criar variáveis com os mesmos nomes dos campos incluindo MEMVAR ou BLANK em SCATTER.
**NAME ObjectName**
Especifica um objeto cujas propriedades têm os mesmos nomes dos campos da tabela. Cada campo é substituído pelo valor da propriedade correspondente. Se ela não existir, o campo não será substituído.
**FIELDS FieldList**
Especifica os campos cujo conteúdo será substituído pelos elementos da matriz ou pelas variáveis. Somente os campos de FieldList são substituídos.
**FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton**
Permite substituir campos seletivamente com LIKE, EXCEPT ou ambos. LIKE Skeleton substitui os campos correspondentes a Skeleton; EXCEPT Skeleton substitui todos exceto os correspondentes. Skeleton aceita os curingas * e ?. Por exemplo: GATHER FROM gamyarray FIELDS LIKE A*,P*
**MEMO**
Especifica que campos memo ou Blob sejam substituídos por elementos da matriz ou variáveis. Se MEMO for omitido, esses campos serão ignorados. Campos General e de imagem são sempre ignorados, mesmo com MEMO.

# Exemplo

Este exemplo usa GATHER para copiar dados para um novo registro. Após criar a tabela `Test`, SCATTER cria variáveis com base nos campos. Cada campo recebe um valor e um registro vazio é adicionado.

```foxpro
CREATE TABLE Test FREE ;
   (Object C(10), Color C(16), SqFt n(6,2))
SCATTER MEMVAR BLANK
m.Object="Box"
m.Color="Red"
m.SqFt=12.5
APPEND BLANK
GATHER MEMVAR
BROWSE
```

O exemplo a seguir usa GATHER com NAME. SCATTER cria um objeto com propriedades baseadas nos campos; as propriedades recebem valores e um registro vazio é adicionado.

```foxpro
CREATE TABLE Test FREE ;
   (Object C(10), Color C(16), SqFt n(6,2))
SCATTER NAME oTest BLANK
oTest.Object="Box"
oTest.Color="Red"
oTest.SqFt=12.5
APPEND BLANK
GATHER NAME oTest
RELEASE oTest
BROWSE
```
