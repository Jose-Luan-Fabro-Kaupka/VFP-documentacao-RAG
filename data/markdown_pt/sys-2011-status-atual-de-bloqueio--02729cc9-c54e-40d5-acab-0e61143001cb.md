# SYS(2011) - Status atual de bloqueio

Retorna o status de bloqueio do registro ou da tabela na área de trabalho atual.

```foxpro
SYS(2011)
```

# Valor de retorno

Caractere

# Observações

Ao contrário das funções FLOCK( ), LOCK( ) e RLOCK( ), SYS(2011) não tenta bloquear a tabela ou o registro.

A cadeia de caracteres retornada por SYS(2011) é idêntica à mensagem exibida na barra de status (Exclusive, Record Unlocked, Record Locked ...).

SYS(2011) retorna Exclusive somente na sessão de dados que abriu a tabela exclusivamente e Record Locked somente na sessão que aplicou o bloqueio de registro.
