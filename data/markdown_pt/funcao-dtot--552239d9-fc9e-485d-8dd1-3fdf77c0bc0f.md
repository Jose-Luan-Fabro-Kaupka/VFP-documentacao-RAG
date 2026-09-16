# Função DTOT( )

Retorna um valor DateTime de uma expressão Date.

```foxpro
DTOT(dDateExpression)
```

#### Parâmetros
 **dDateExpression**
Especifica a expressão Date da qual um valor DateTime é retornado.

# Valor de retorno

DateTime

# Observações

O formato do valor DateTime que DTOT( ) retorna depende das configurações atuais de SET DATE e SET MARK. Se um século não for fornecido, o século vinte é assumido.

DTOT( ) adiciona um horário padrão de 12:00:00 AM (se SET HOURS é 12) ou 00:00:00 (se SET HOURS é 24) à data para produzir um valor DateTime válido.

# Exemplo

```foxpro
SET HOURS TO 12
? DTOT({^2004-02-16}) && Displays 02/16/2004 12:00:00 AM
```
