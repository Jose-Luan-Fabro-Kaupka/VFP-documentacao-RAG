# SYS(3) - Nome de arquivo válido

Retorna um nome de arquivo válido que pode ser usado para criar arquivos temporários.

```foxpro
SYS(3)
```

# Valor de retorno

Character

# Observações

SYS(3) retorna nomes de arquivo que começam com números. Se seu código usa SYS(3) com comandos como CREATE TABLE, CREATE CURSOR, SELECT INTO CURSOR, o código pode falhar porque cursores ou nomes de alias do FoxPro não podem começar com números. Você pode usar SYS(2015) em vez disso.

SYS(3) pode retornar um nome não exclusivo quando emitido sucessivamente em um computador rápido.
