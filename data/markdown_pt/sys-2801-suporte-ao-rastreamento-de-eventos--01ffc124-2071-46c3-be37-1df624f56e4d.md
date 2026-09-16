# SYS(2801) - Suporte ao rastreamento de eventos

Estende o rastreamento de eventos de mouse e teclado.

```foxpro
SYS(2801 [, 1 | 2 | 3 ] )
```

#### Parâmetros
 **1**
Registra somente eventos de objetos do Visual FoxPro.
**2**
Registra somente eventos de mouse e teclado do Windows.
**3**
Registra eventos do Visual FoxPro e do Windows.

# Observações

Você pode usar SYS(2801) para especificar quais eventos do usuário serão rastreados durante a execução do código. Configure o rastreamento no depurador do Visual FoxPro ou use o comando SET EVENTTRACKING.
