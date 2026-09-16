# Método Item (classe Collection)

Retorna um objeto membro específico na coleção por posição numérica ou chave de cadeia de caracteres.

O objeto membro pode ter qualquer tipo válido que possa ser atribuído a uma variável de memória. Isso inclui tipos de dados simples, como cadeias de caracteres, números, datas, valores lógicos, ou tipos mais complexos, como objetos do Visual FoxPro e Component Object Model (COM). O método Item para objetos de coleção é normalmente usado com enumerações FOR EACH...ENDFOR para fazer referência a membros da coleção.

```foxpro
Collection.Item( eIndex )
```

#### Parâmetros
 **eIndex**
Especifica uma expressão obrigatória que representa uma posição de um item na coleção. Esta expressão pode ser de um dos dois tipos: Numeric. A expressão eIndex deve ter um valor de 1 até o valor da propriedade Count da coleção. String. A expressão eIndex deve corresponder ao cKey especificado para o item quando ele foi adicionado à coleção.

Se eIndex não corresponder a um membro existente da coleção, ocorre um erro.

# Valor de retorno

Retorna o item específico.

# Observações

Se um tipo incorreto for passado para um parâmetro específico, ocorre um erro.

O método Item para objetos de coleção retorna um valor, que é o próprio item. Portanto, você precisa adicionar uma instrução RETURN ao final do método Item no código-fonte de qualquer subclasse que tenha modificado:

```foxpro
RETURN DODEFAULT(eIndex)
```

Se você não quiser retornar o item, use a instrução RETURN sem a função DODEFAULT().

O método Item para objetos de coleção é o método padrão de uma coleção. Por exemplo, suponha que você tenha o seguinte código:

```foxpro
Public MyCollection AS Collection
MyCollection = CREATEOBJECT("Collection")
MyCollection.Add(CREATEOBJECT("Form"),"myKey")
```

As linhas de código a seguir são equivalentes:

```foxpro
? MyCollection(1)
? MyCollection.Item(1)
? MyCollection("myKey")
```

# Exemplo

O exemplo a seguir ilustra estas tarefas em tempo de execução:
 - Cria formulários e uma coleção.
- Adiciona formulários à coleção.
- Exibe o nome de cada formulário na coleção.
- Exibe o número de formulários na coleção.
- Exibe o nome do primeiro item na coleção.
- Exibe o nome do primeiro item na coleção usando o método Item para coleções.

```foxpro
loForm1 = CREATEOBJECT("myForm1")
loForm2 = CREATEOBJECT("myForm2")
loCol = CREATEOBJECT("myCollection")
loCol.Add(loForm1)
loCol.Add(loForm2)
? loCol(1).Name
? loCol.Item(1).Name
```
