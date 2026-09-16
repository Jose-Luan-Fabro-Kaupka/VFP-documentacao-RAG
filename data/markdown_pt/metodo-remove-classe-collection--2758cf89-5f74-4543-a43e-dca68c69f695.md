# Método Remove (classe Collection)

Use para remover um objeto membro de uma coleção.

O objeto membro pode ter qualquer tipo válido que possa ser atribuído a uma variável de memória. Isso inclui tipos de dados simples, como cadeias de caracteres, números, datas e valores lógicos, ou tipos mais complexos, como objetos do Visual FoxPro e do Component Object Model (COM).

```foxpro
Collection.Remove( eIndex )
```

#### Parâmetros
 **eIndex**
Especifica uma expressão que representa a posição de um item na coleção. Essa expressão pode ser de dois tipos: Numeric. A expressão eIndex deve ter um valor de 1 até o valor da propriedade Count da coleção. Se você passar -1, o Visual FoxPro removerá todos os itens da coleção. String. A expressão eIndex deve corresponder ao cKey especificado para o item quando ele foi adicionado à coleção. Se eIndex não corresponder a um membro existente, ocorrerá um erro.

# Observações
 - Se um tipo incorreto for passado para um parâmetro específico, ocorrerá um erro.
- Inclua o comando NODEFAULT no método Remove de objetos de coleção para impedir a remoção de determinado item da coleção.

# Exemplo

O exemplo a seguir ilustra estas tarefas em tempo de execução:
 - Cria formulários e uma coleção.
- Adiciona formulários à coleção.
- Exibe o número de formulários na coleção.
- Remove o primeiro formulário da coleção.
- Exibe o número atual de formulários na coleção.

```foxpro
loForm1 = CREATEOBJECT("myForm1")
loForm2 = CREATEOBJECT("myForm2")
loCol = CREATEOBJECT("myCollection")
loCol.Add(loForm1)
loCol.Add(loForm2)
? loCol.Count
loCol.Remove(1)
? loCol.Count
```
