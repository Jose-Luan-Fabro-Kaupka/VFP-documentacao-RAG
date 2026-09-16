# Comando SET FDOW

Especifica o primeiro dia da semana.

```foxpro
SET FDOW TO [nExpression]
```

#### Parâmetros
 **nExpression**
Especifica o primeiro dia da semana. A tabela a seguir lista os valores que nExpression pode assumir e o primeiro dia da semana correspondente. Nexpression Dia da semana 1 Sunday 2 Monday 3 Tuesday 4 Wednesday 5 Thursday 6 Friday 7 Saturday Se você omitir nExpression , o primeiro dia da semana é redefinido para Sunday (1).

# Observações

O primeiro dia da semana também pode ser definido com a caixa de listagem Week Starts On na guia Regional, Options Dialog Box da caixa de diálogo Options.

# Exemplo

```foxpro
STORE SET('FDOW') TO gnFdow  && Save current value
SET FDOW TO 1  && Sets first day of the week to Sunday, the default
SET FDOW TO 7  && Sets first day of the week to Saturday
SET FDOW TO &gnFdow  && Restore original day
```
