# Operador % (Visual FoxPro)

Retorna o resto (módulo) obtido ao dividir uma expressão numérica por outra.

```foxpro
nDividend % nDivisor
```

#### Parâmetros
 **nDividend**
Especifica o dividendo (expressão numérica sendo dividida). O número de casas decimais em nDividend determina o número de casas decimais no resultado.
**nDivisor**
Especifica o divisor (a expressão numérica que divide o dividendo nDividend ). Um número positivo é retornado se nDivisor for positivo; um número negativo se nDivisor for negativo. nDivisor não pode ser zero.

# Observações

O operador de módulo (%) e MOD( ) retornam resultados idênticos.

O operador de módulo (%) é um operador aritmético. Outros operadores aritméticos são: + (adição), - (subtração), * (multiplicação), / (divisão) e ^ (exponenciação). Quando esses operadores são combinados em uma expressão numérica, % tem a mesma precedência que * e /.

Para uma discussão adicional sobre operadores e sua ordem de precedência, consulte o tópico Operators (Visual FoxPro).

# Exemplo

```foxpro
? 36 % 10         && Displays 6
? (4*9) % (90/9)      && Displays 6
? 25.250 % 5.0      && Displays 0.250
? IIF(YEAR(DATE()) % 4 = 0, 'Summer Olympics this year';
   , 'No Summer Olympics this year')
```
