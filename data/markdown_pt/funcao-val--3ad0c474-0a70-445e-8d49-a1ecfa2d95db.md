# Função VAL( )

Retorna um valor numérico ou de moeda de uma expressão de caractere composta por números. Você pode usar VAL( ) para converter as cadeias de caracteres retornadas pelas funções SYS( ) do Visual FoxPro em valores numéricos.

```foxpro
VAL(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica uma expressão de caractere composta por até 16 números. Ocorre arredondamento se mais de 16 números estiverem incluídos em cExpression. Se o primeiro caractere de cExpression for um cifrão ($), VAL( ) retorna um valor de moeda. Em todas as outras situações, VAL( ) retorna um valor numérico.

# Valor de retorno

Tipo de dados Numeric ou Currency. VAL( ) retorna os números na expressão de caractere da esquerda para a direita até que um caractere não numérico seja encontrado. Espaços à esquerda são ignorados. VAL( ) retorna 0 se o primeiro caractere da expressão de caractere não for um número, um cifrão ($), um sinal de mais (+) ou um sinal de menos (-). Você pode controlar o resultado de VAL( ) emitindo o comando SET DECIMALS antes de usar a função VAL( ).

# Exemplo

```foxpro
CLEAR
STORE '12' TO A
STORE '13' TO B
? VAL(A) + VAL(B)  && Displays 25.00
STORE '1.25E3' TO C
? 2 * VAL(C)  && Displays 2500.00
```
