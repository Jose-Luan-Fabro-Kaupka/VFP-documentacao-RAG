# Método Add (Classe Collection)

Usado para adicionar um membro a uma coleção.

O objeto membro pode ter qualquer tipo válido que possa ser atribuído a uma variável de memória. Isso inclui tipos de dados simples, como cadeias de caracteres, números, datas, valores lógicos, ou tipos mais complexos, como objetos Visual FoxPro e Component Object Model (COM).

```foxpro
Collection.Add( eItem [, cKey [, [eBefore |, eAfter ]]] )
```

#### Parâmetros
 **eItem**
Especifica uma expressão de qualquer tipo que representa um membro a adicionar à coleção. Geralmente, é um objeto, mas pode ser um número, cadeia de caracteres ou membro que tenha um tipo válido.
**cKey**
Especifica uma expressão alfanumérica opcional e exclusiva (tipo character) que representa uma cadeia de chave, em vez de um índice posicional, que pode ser usada para acessar um membro da coleção. Para coleções que usam chaves, cKey é um parâmetro que diferencia maiúsculas de minúsculas e não pode estar vazio ou ter um valor nulo (.NULL.). Todos os itens adicionados à coleção devem ter o parâmetro cKey especificado ou não especificado por motivos de desempenho. O primeiro item adicionado determina o comportamento da coleção. Você pode testar a presença de chaves em uma coleção usando o seguinte código: GetKey(1) Se a chave já existir para um membro na coleção, ocorre um erro. No entanto, como cKey diferencia maiúsculas de minúsculas, nenhum erro de duplicação ocorre se as mesmas chaves com maiúsculas diferentes forem adicionadas. Uma chave inclui quaisquer espaços à direita presentes em cKey .
**[, [ eBefore |, eAfter ]]**
Especifica uma expressão opcional que representa uma posição onde um novo membro deve ser inserido antes ou depois de outro item na coleção. Você pode especificar uma expressão eBefore ou eAfter, mas não ambas, o que gera a mensagem apropriada. Esta expressão pode ser de dois tipos: Numérico. A expressão eBefore e eAfter deve ter um valor de 1 até o valor da propriedade Count da coleção. Cadeia de caracteres. A expressão eBefore e eAfter deve corresponder ao cKey que foi especificado para o item referenciado quando foi adicionado à coleção. Inserir um novo item em uma coleção antes ou depois de um existente requer que a coleção seja uma coleção com chave. Quando você especifica um valor cKey com um parâmetro eBefore ou eAfter, o novo item é adicionado antes ou depois do valor de índice da chave especificada. Neste caso, o valor de Collection KeySort não tem efeito. Por exemplo, suponha que cKey para um novo item é "ZZZ" e para um item existente cKey é "YYY" e seu valor de índice é 15. O novo item receberia um valor de índice 15 e o item existente receberia um novo valor de índice 16. Para inserir um novo item antes de um item existente, inclua a chave do item antes do qual deseja inserir o novo item, conforme mostrado no exemplo a seguir: loItems.Add("Roses", "flower1", "flower2") Para inserir um novo item depois de um item existente, inclua a chave do item depois do qual deseja inserir o novo item. Além disso, você deve passar um terceiro parâmetro vazio para eBefore, conforme mostrado no exemplo a seguir: loItems.Add("Orchids", "flower3",, "flower2") Se eBefore e eAfter não se referirem a um membro existente da coleção, ocorre um erro. O Visual FoxPro adiciona um item ao final de uma coleção quando eBefore ou eAfter não são especificados.

# Observações

Ao adicionar objetos a coleções, o Visual FoxPro aumenta a contagem de referências desse objeto. De acordo com o comportamento usual de objetos do Visual FoxPro, você pode liberar um objeto apenas quando sua contagem de referências é 0. Portanto, você deve garantir que a referência ao objeto na coleção seja liberada ao liberar o objeto; caso contrário, o Visual FoxPro não remove o objeto completamente da memória.

Você não está limitado ao número de itens que pode adicionar a uma coleção. No entanto, o tamanho de uma coleção pode afetar o desempenho de operações como acessar, pesquisar e enumerar itens na coleção. Por exemplo, criar uma coleção grande baseada em registros de uma tabela muito grande (.dbf) não é recomendado porque você não pode usar otimização de consulta e outros recursos associados ao mecanismo de dados nativo do Visual FoxPro.

Você pode ter uma coleção de coleções porque coleções são objetos. No entanto, evite criar referências circulares, como tentar adicionar uma coleção externa a uma coleção interna.

Adicionar matrizes como itens a uma coleção instanciada da classe base tem uso limitado porque não há uma forma fácil de referenciar todos os elementos na matriz. Considere o exemplo a seguir:

```foxpro
DIMENSION x[3]
x[1] = 1
x[2] = 22
x[3] = 333
y = CREATEOBJECT("collection")
y.Add(@x)
z = y.item(1)   && Returns just the first element
? z[2]         && Error
```

Portanto, você deve criar uma subclasse com tratamento especial para este cenário.

Você pode passar um valor NULL como tipo de item e usar as funções TYPE( ) e VARTYPE( ) para consultar o tipo do item na coleção.

Você pode adicionar itens de tipo misto. No entanto, o Visual FoxPro não impõe segurança de tipo, portanto você deve fornecê-la para a classe se necessário. Se um tipo incorreto for passado para um parâmetro específico, ocorre um erro.

Inclua o comando NODEFAULT no método Add para objetos de coleção para impedir a adição de um item específico à coleção.

# Exemplo

O exemplo a seguir ilustra as seguintes tarefas:
 - Adiciona quatro itens a uma coleção usando o parâmetro cKey.
- Adiciona um segundo item com uma chave que precede o primeiro item usando o parâmetro eBefore.
- Adiciona um quarto item com uma chave que segue o primeiro item adicionado usando o parâmetro eAfter.
- Itera por todos os itens exibindo na tela.

```foxpro
CLEAR
LOCAL loItems, lcFlower
loItems = NEWOBJECT("Collection")
loItems.Add("Daffodils", "flower2")
* Add "Roses" with "flower1" key before "flower2".
loItems.Add("Roses", "flower1", "flower2")
loItems.Add("Daisies", "flower4")
* Add "Orchids" with "flower4" key after "flower2".
loItems.Add("Orchids","flower3",,"flower2")
FOR EACH lcFlower IN loItems
   ? lcFlower
ENDFOR
```

O exemplo a seguir gera um erro. Você não pode especificar tanto eBefore quanto eAfter.

```foxpro
* Generates an error. Cannot specify both eBefore and eAfter.
loItems.Add("Violets","flower5","flower2","flower1")
```
