# DMY( ) Função

Retorna uma expressão de caracteres em formato dia-mês-ano (por exemplo, 31 de maio de 1998) a partir de uma expressão Data ou DateTime. O nome do mês não está abreviado.

```foxpro
DMY(dExpression | tExpression)
```

Parâmetros
**dExpression**
Especifica a expressão Data da qual DMY( ) retorna uma string de caracteres no formato dia-mês-ano.
**tExpression**
Especifica a expressão DateTime da qual DMY( ) retorna uma string de caracteres no formato dia- mês- ano.

# Valor de Retorno

Caracter

Observações

Se SET CENTURY é OFF, DMY( ) retorna uma string de caracteres em um formato dd-Month-yy (por exemplo, 16 de fevereiro de 98). Se SET CENTURY for ON, o formato é dd-Month-yyyyy (por exemplo, 16 de fevereiro de 1998).

Exemplo

```foxpro
CLEAR
SET CENTURY OFF
? DMY(DATE())
SET CENTURY ON
? DMY(DATE())
```

Veja também
- MDY( ) Function
- SET CENTURY Command
- SET DATE Command
- Funções
- Referência linguística (Visual FoxPro)
