# Como: Teste uma conexão para disponibilidade

When a connection is busy, such as when Visual FoxPro is progressively fetching data into a cursor, you don't want to start another fetch or send updates on the same connection. You can determine whether a connection is busy with the ConnectBusy property, which returns a value of true (.T.) if the connection is busy. You can use this property in your application to test a connection before sending a request over a shared connection to a remote data source.

# # # Para determinar se uma ligação está ocupada
- Use a propriedade ConnectBusy do SQLGETPROP( ) Função .

Você precisa do punho de conexão para usar a função SQLGETPROP( ). Você pode identificar o identificador de conexão para uma visão ativa com a propriedade ConnectHandle do CURSORGETPROP( ) Função. O seguinte código identifica um identificador de conexão e usa o identificador de conexão para testar se a conexão está ocupada:

```foxpro
nConnectionHandle=CURSORGETPROP('ConnectHandle')
SQLGETPROP(nConnectionHandle, "ConnectBusy")
```

Veja também
- Como: Otimizar o desempenho da visualização
- Como: Otimizar Filtros e Juntar
- Como: Criar Consultas (Visual FoxPro)
- Como: Compartilhar conexões para várias vistas remotas
