# Uma chave deve ser especificada ao adicionar um item a esta coleção. (Erro 2063)

Você deve especificar uma chave ao adicionar um novo item a uma coleção em que todos os itens têm chaves. Todos os itens em uma coleção têm chaves ou não têm chaves. Para determinar se uma coleção requer chaves, use `GetKey(1)` e a função EMPTY( ) da seguinte forma:

```foxpro
? EMPTY(Collection.GetKey(1))
```
