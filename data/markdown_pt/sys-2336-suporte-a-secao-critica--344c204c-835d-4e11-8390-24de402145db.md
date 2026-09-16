# SYS(2336) - Suporte a seção crítica

Controla entradas ou saídas de uma seção crítica em servidores MTDLL.

```foxpro
SYS(2336 [, nAction])
```

#### Parâmetros
 **nAction**
Especifica a ação executada pela função SYS(2336) conforme a tabela a seguir. nAction Descrição (nenhum) Retorna a contagem de referência atual. (Padrão) 1 Chama EnterCriticalSection. 2 Chama LeaveCriticalSection. 3 Chama LeaveCriticalSection quantas vezes for necessário para reduzir a contagem de referência a 0, liberando assim a seção crítica.

# Valor de retorno

Character. SYS(2336) retorna a contagem de referência para todos os valores de nAction.

# Observações

SYS(2336) acessa as chamadas de API do Windows EnterCriticalSection e LeaveCriticalSection. Você pode encontrar detalhes dessas funções na referência Platform SDK da biblioteca MSDN em http://msdn.microsoft.com/library.
