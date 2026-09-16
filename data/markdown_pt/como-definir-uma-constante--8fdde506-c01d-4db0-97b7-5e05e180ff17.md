# Como: definir uma constante

Uma constante pode conter um valor de qualquer tipo de dados.

### Para atribuir um valor a uma constante
- Use a diretiva de pré-processador #DEFINE.

No exemplo a seguir, a constante `TABLERR1` é definida como uma cadeia de caracteres.

```foxpro
#DEFINE TABLERR1 "This table is not available. Please try later."
```

Em um aplicativo, onde você normalmente especificaria a cadeia de caracteres "This table is not available. Please try later.", você pode usar `TABLERR1` em vez disso.

### Para liberar uma constante definida
- Use a diretiva de pré-processador #UNDEFINE. #UNDEF TABLERR1
