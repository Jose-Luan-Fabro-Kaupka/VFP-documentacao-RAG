# Variável de sistema _TRIGGERLEVEL

Contém um valor numérico somente leitura que indica o nível atual de aninhamento do procedimento de gatilho.

```foxpro
_TRIGGERLEVEL = nExpression
```

#### Parâmetros
 **nExpression**
Contém o nível atual de aninhamento do procedimento de gatilho. _TRIGGERLEVEL contém 1 quando o procedimento de gatilho inicial está em execução. Se um procedimento de gatilho fizer com que outro procedimento de gatilho seja acionado, _TRIGGERLEVEL será incrementado em 1. _TRIGGERLEVEL contém 0 se nenhum procedimento de gatilho estiver em execução.

# Observações

Use CREATE TRIGGER para criar um gatilho Delete, Insert ou Update para uma tabela. Você pode usar APPEND PROCEDURES e MODIFY PROCEDURES para criar procedimentos armazenados que são executados quando ocorre um gatilho Delete, Insert ou Update.

_TRIGGERLEVEL contém um valor numérico somente leitura. Se você usar STORE ou = para atribuir um valor a _TRIGGERLEVEL, o valor será ignorado.
