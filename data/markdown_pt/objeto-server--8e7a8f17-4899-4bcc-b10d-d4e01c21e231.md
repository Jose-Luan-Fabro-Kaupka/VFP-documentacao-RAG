# Objeto Server

Uma referência de objeto a um servidor em um projeto.

```foxpro
Server
```

# Observações

Um objeto server é criado e instanciado para cada servidor em um projeto após a construção de um arquivo executável (.exe) ou biblioteca de vínculo dinâmico (.dll) a partir do projeto. O objeto server fornece uma referência de objeto a um servidor no projeto e permite determinar informações sobre o servidor e manipulá-lo por meio das propriedades do objeto server.

A coleção servers de um projeto é composta por todos os objetos server no projeto.

Observe que um objeto server é um objeto COM, portanto atribuir uma referência de objeto server a uma variável de memória cria uma variável de memória da classe "Unknown Type."
