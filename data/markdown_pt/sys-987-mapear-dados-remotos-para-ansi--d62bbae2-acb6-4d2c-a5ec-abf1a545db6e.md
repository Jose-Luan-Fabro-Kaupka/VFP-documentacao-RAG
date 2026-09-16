# SYS(987) - Mapear dados remotos para ANSI

Mapeia dados Unicode remotos recuperados por SQL pass-through ou views remotas para ANSI.

```foxpro
SYS(987 [, lExpr])
```

#### Parâmetros
 **lExpr**
True (.T.) - Os dados Unicode são sempre buscados como ANSI. O driver ODBC realiza a conversão de Unicode para ANSI. False (.F.) (Padrão) - Os dados Unicode são buscados como Unicode.

# Valor de retorno

Tipo de dados lógico. SYS(987) retorna a configuração anterior.

Se você chamar SYS(987) sem o parâmetro lExpr, retorna a configuração atual.

# Observações

SYS(987) pode ser usado para retornar dados Varchar remotos como ANSI para uso com campos Memo.

A configuração SYS(987) é uma configuração global em todas as sessões de dados. Depois que um cursor remoto é criado, alterar a configuração SYS(987) não afeta buscas de dados subsequentes para o cursor, mesmo se REQUERY( ) for executado.
