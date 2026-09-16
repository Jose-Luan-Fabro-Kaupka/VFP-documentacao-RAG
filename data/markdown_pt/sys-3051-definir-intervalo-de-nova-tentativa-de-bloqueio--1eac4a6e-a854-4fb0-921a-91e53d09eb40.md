# SYS(3051) - Definir intervalo de nova tentativa de bloqueio

Especifica o tempo, em milissegundos, que o Visual FoxPro aguarda antes de tentar bloquear um registro, uma tabela, um arquivo de memo ou um arquivo de índice após uma tentativa de bloqueio malsucedida.

```foxpro
SYS(3051, [nWaitMilliseconds])
```

#### Parâmetros
**nWaitMilliseconds**
Especifica o tempo de espera em milissegundos; pode ser um valor de 100 a 1000 milissegundos. Especifique 0 para nWaitMilliseconds a fim de restaurar o intervalo entre tentativas de bloqueio para o valor padrão de inicialização do Visual FoxPro (333 milissegundos). Se nWaitMilliseconds for omitido, SYS(3051) retornará o intervalo atual entre tentativas de bloqueio.

# Valor de retorno

Character

# Observações

SYS(3051) retorna um valor numérico como uma cadeia de caracteres que indica o intervalo entre tentativas de bloqueio.

O valor é aplicado globalmente.
