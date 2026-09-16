# Função DDELastError( )

Retorna um número de erro para a última função de troca dinâmica de dados (DDE).

```foxpro
DDELastError()
```

# Valor de retorno

Numérico

# Observações

Você pode usar DDELastError( ) para ajudar a determinar a causa de um erro quando uma função DDE não é executada com sucesso.

DDELastError( ) retorna 0 se a última função DDE foi executada com sucesso. Retorna um valor diferente de zero se a última função DDE não foi bem-sucedida. A tabela a seguir lista os números de erro e suas descrições.

| Número de erro | Descrição |
| --- | --- |
| 1 | Service busy |
| 2 | Topic busy |
| 3 | Channel busy |
| 4 | No such service |
| 5 | No such topic |
| 6 | Bad channel |
| 7 | Insufficient memory |
| 8 | Acknowledge timeout |
| 9 | Request timeout |
| 10 | No DDEInitiate( ) |
| 11 | Client attempted server transaction |
| 12 | Execute timeout |
| 13 | Bad parameter |
| 14 | Low memory |
| 15 | Memory error |
| 16 | Connect failure |
| 17 | Request failure |
| 18 | Poke timeout |
| 19 | Could not display message |
| 20 | Multiple synchronous transactions |
| 21 | Server died |
| 22 | Internal DDE error |
| 23 | Advise timeout |
| 24 | Invalid transaction identifier |
| 25 | Unknown |
