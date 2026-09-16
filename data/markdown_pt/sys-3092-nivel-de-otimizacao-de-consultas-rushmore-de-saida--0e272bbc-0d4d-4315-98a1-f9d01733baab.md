# SYS(3092) — Nível de otimização de consultas Rushmore de saída

Especifica um arquivo para o qual são enviados os níveis de otimização Rushmore das consultas.

```foxpro
SYS(3092 [,cFileName [, lAdditive]])
```

#### Parâmetros
 **cFileName**
O nome do arquivo para o qual são enviados os níveis de otimização Rushmore. Especifique a cadeia de caracteres vazia ("") para desativar a saída e fechar um arquivo criado anteriormente com esta função.
**lAdditive**
Um valor lógico que especifica se o arquivo é sobrescrito quando uma nova consulta é executada. Se lAdditive for definido como verdadeiro (.T.), os níveis de otimização da consulta serão acrescentados à saída anterior. Se lAdditive for definido como falso (.F.) (a configuração padrão), toda saída anterior será sobrescrita.

# Valor de retorno

SYS(3092) retorna a cadeia de caracteres vazia se os níveis de otimização Rushmore das consultas não estiverem sendo enviados para um arquivo. Se os níveis de otimização estiverem sendo enviados para um arquivo, SYS(3092) retornará o caminho e o nome do arquivo ao qual a saída é direcionada.

# Observações

Use SYS(3054) — Nível de otimização de consultas Rushmore para especificar o tipo de informação de otimização Rushmore enviada ao arquivo de saída.

SYS(3092) tem escopo de thread em um aplicativo de tempo de execução multithread. SYS(3092) e SYS(3054) não estão disponíveis no Provedor OLE DB para Visual FoxPro.
