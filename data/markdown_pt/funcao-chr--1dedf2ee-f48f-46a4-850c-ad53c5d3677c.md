# Função CHR( )

Retorna o caractere associado ao código ANSI numérico especificado.

```foxpro
CHR(nANSICode)
```

#### Parâmetros
 **nANSICode**
Especifica um número entre 0 e 255 cujo caractere ANSI equivalente CHR( ) retorna. Use ASC( ) para retornar o valor ANSI de um caractere.

# Valor de retorno

Character

# Observações

CHR( ) retorna um único caractere correspondente à posição numérica na tabela de caracteres da página de código atual. Pode ser usada para enviar códigos de controle a uma impressora.

# Exemplo

O exemplo exibe os números de 65 a 75 e usa CHR( ) para exibir os caracteres correspondentes de A a K.

```foxpro
CLEAR
FOR nCOUNT = 65 TO 75
   ? nCount && Display numeric value
   ?? ' ' + CHR(nCount) && Display character
ENDFOR
```
