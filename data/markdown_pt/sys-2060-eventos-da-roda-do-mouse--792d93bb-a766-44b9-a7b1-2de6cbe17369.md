# SYS(2060) - Eventos da roda do mouse

Habilita ou desabilita o acúmulo de eventos da roda do mouse na fila de eventos.

```foxpro
SYS(2060 [, 0 | 1])
```

#### Parâmetros
 **0**
Habilita a combinação de eventos da roda do mouse na fila de eventos. (Padrão)
**1**
Desabilita a combinação de eventos da roda do mouse na fila de eventos.

# Valor de retorno

Tipo de dados Character. Retorna o valor atual de SYS(2060).

# Observações

Quando SYS(2060) está definido como 0, os eventos da roda do mouse são somados na fila de eventos, em vez de adicionar um novo evento. Isso cria uma rolagem mais suave em computadores mais lentos.
