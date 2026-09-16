# SYS(2410) - Manipulador de erros

Retorna o tipo de manipulador de erros para um erro. Você pode usar SYS(2410) em seu código TRY...CATCH...FINALLY para determinar um curso de ação, por exemplo, usando uma estrutura DO CASE, dependendo do tipo de manipulador que trata a exceção.

```foxpro
SYS(2410)
```

# Valor de retorno

Tipo de dados caractere. A tabela a seguir lista os valores possíveis retornados por SYS(2410).

| Valor | Descrição |
| --- | --- |
| 0 | Manipulador do sistema |
| 1 | TRY...CATCH...FINALLY |
| 2 | Evento Error |
| 3 | Comando ON ERROR |

# Observações

Se uma estrutura TRY...CATCH...FINALLY não contiver instruções CATCH ou instruções CATCH em que WHEN lExpression avalia como True (.T.), SYS(2410) pode retornar erroneamente um valor incorreto.
