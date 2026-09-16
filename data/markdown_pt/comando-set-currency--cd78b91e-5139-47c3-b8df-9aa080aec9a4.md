# Comando SET CURRENCY

Define o símbolo de moeda e especifica sua posição na exibição de expressões numéricas, de moeda, float e double.

```foxpro
SET CURRENCY TO [cCurrencySymbol]
-or-
SET CURRENCY LEFT | RIGHT
```

#### Parâmetros
 **cCurrencySymbol**
Especifica uma cadeia de caracteres que representa o símbolo de moeda; pode ter de um a nove caracteres. Emita SET CURRENCY TO sem cCurrencySymbol para redefinir o símbolo de moeda para o cifrão padrão ($). Você também pode especificar um símbolo de moeda usando Alt+nnn. Especifique o símbolo de moeda Euro () com Alt+0128 se você instalou fontes Windows compatíveis. Você também pode definir o símbolo de moeda padrão na guia Regional da caixa de diálogo Options .
**LEFT**
(Padrão) Posiciona o símbolo de moeda à esquerda do valor de moeda.
**RIGHT**
Posiciona o símbolo de moeda à direita do valor de moeda.

# Observações

O símbolo de moeda é exibido na saída criada com @ ... SAY e em caixas de texto criadas com @ ... GET quando o código $ é incluído na cláusula FUNCTION ou PICTURE.

SET CURRENCY tem escopo na sessão de dados atual.

# Exemplo

O exemplo a seguir exibe o símbolo de moeda DM em qualquer lado do valor de moeda. Se você usar PICTURE para exibir o símbolo de moeda, certifique-se de incluir @ antes do cifrão.

```foxpro
STORE SET('CURRENCY') TO gcCurrPosit
STORE 1234.56 TO gnDollarAmnt
CLEAR
SET CURRENCY TO 'DM'
@ 2,2 SAY gnDollarAmnt PICTURE '@$99,999.99'
IF gcCurrPosit = 'LEFT'
   SET CURRENCY RIGHT
ELSE
   SET CURRENCY LEFT
ENDIF
@ 4,2 SAY gnDollarAmnt FUNCTION '$99,999.99'
```
