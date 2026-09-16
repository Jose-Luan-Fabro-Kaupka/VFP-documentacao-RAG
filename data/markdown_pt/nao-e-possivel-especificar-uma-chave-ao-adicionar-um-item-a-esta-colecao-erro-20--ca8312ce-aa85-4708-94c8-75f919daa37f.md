# Não é possível especificar uma chave ao adicionar um item a esta coleção. (Erro 2064)

Você não pode especificar uma chave ao adicionar um novo item a uma coleção em que todos os itens não possuem chaves. Todos os itens em uma coleção possuem chaves ou não possuem chaves. Para determinar se uma coleção requer chaves, use `GetKey(1)` e a função EMPTY( ) da seguinte forma:

```foxpro
? EMPTY(Collection.GetKey(1))
```
