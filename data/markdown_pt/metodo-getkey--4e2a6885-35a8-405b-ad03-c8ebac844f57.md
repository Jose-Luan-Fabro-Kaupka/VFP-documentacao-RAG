# Método GetKey

Retorna a chave ou o índice de um item em uma coleção dependendo do valor que é passado.

```foxpro
Collection.GetKey(eIndex)
```

#### Parâmetros
 **eIndex**
Especifica uma expressão obrigatória que representa uma posição de um item na coleção. Esta expressão pode ser de um dos dois tipos: Numérico. A expressão eIndex deve ter um valor de 1 ao valor da propriedade Count da coleção. Cadeia de caracteres. A expressão eIndex deve corresponder ao cKey que foi especificado para o item quando foi adicionado à coleção.

# Valor de retorno

A tabela a seguir lista os valores de retorno para GetKey.

| Valor de retorno | Condição |
| --- | --- |
| Cadeia de caracteres (chave) | Ao passar um índice ou valor inteiro |
| Inteiro (índice) | Ao passar uma chave ou cadeia de caracteres |
| Cadeia de caracteres vazia ("") | Ao passar um índice que não existe ou se itens foram adicionados à coleção sem chaves |
| 0 | Ao passar uma chave que não existe |

# Observações
 - Como o método GetKey retorna um valor, você precisa adicionar uma instrução RETURN ao final de GetKey no código-fonte de qualquer subclasse que tenha modificado. Por exemplo: RETURN DODEFAULT( eIndex ) Se você não deseja retornar o valor, use o comando RETURN sem a função DODEFAULT(). 
- Para determinar se chaves foram especificadas quando itens foram adicionados à coleção, você pode usar a instrução GetKey(1) e a função EMPTY() para verificar um valor de retorno vazio da seguinte forma: ? !EMPTY(Collection.GetKey(1))
- Para derivar o índice ou a chave de um item em uma coleção de dentro de um loop FOR EACH, use um loop FOR normal em vez de um loop FOR EACH.
- O Visual FoxPro gera um erro se o tipo errado ou nenhum parâmetro é passado a GetKey .

# Exemplo

O exemplo a seguir ilustra as seguintes tarefas após criar uma coleção e adicionar itens:
 - Verificar se os itens têm chaves.
- Recuperar e exibir a chave do segundo item.

```foxpro
CLEAR
LOCAL oItems AS Collection
oItems = NEWOBJECT("Collection")
oItems.Add("Daffodils", "flower2")
oItems.Add("Roses", "flower1", "flower2")
oItems.Add("Daisies", "flower3")
? !EMPTY(oItems.GetKey(1))
? oItems.GetKey(2)
```
