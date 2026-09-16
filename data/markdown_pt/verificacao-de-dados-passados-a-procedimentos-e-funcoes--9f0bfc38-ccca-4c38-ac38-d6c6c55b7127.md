# Verificação de Dados Passados a Procedimentos e Funções

Ao passar dados ou "argumentos" para parâmetros em procedimentos e funções, é recomendável verificar se os dados que os procedimentos e funções recebem são os esperados. Você pode usar as funções TYPE( ) e PARAMETERS( ) para verificar o tipo e o número de argumentos passados a procedimentos e funções.

# Verificação do Tipo de Dados Passado a Parâmetros

Você pode usar a função TYPE( ) para verificar se os dados passados aos parâmetros possuem o tipo correto. No exemplo a seguir, a função aceita um valor de data por meio do parâmetro `dDate`. A função retorna uma data que é 14 dias posterior à data que foi passada:

```foxpro
FUNCTION plus2weeks( dDate )
   PARAMETERS dDate
   RETURN dDate + 14
ENDFUNC
```

O parâmetro na função requer um valor do tipo Data. A versão a seguir da função inclui código que usa a função TYPE( ) para garantir que o valor passado possua o tipo correto:

```foxpro
FUNCTION plus2weeks( dDate )
   IF TYPE("dDate") = "D"
      RETURN dDate + 14
   ELSE
      MESSAGEBOX( "Function requires a date value." )
      RETURN { - - }      && Return an empty date.
   ENDIF
ENDFUNC
```

# Verificação do Número Correto de Argumentos

Quando um programa passa mais argumentos do que o procedimento ou a função espera, o Visual FoxPro gera uma mensagem de erro. Quando um programa passa menos argumentos do que o procedimento ou a função espera, os parâmetros restantes são inicializados como False (.F.).

Por exemplo, suponha que você inclua dois parâmetros em uma definição de procedimento, mas chame o procedimento com três argumentos; o Visual FoxPro gera uma mensagem de erro. No entanto, se você chamar o procedimento com apenas um argumento, o parâmetro restante é inicializado como False (.F.). No entanto, não há forma de saber se o argumento do último parâmetro foi realmente omitido ou apenas avaliado como .F. Portanto, o código de exemplo a seguir usa a função PARAMETERS( ) para verificar o número apropriado de argumentos:

```foxpro
FUNCTION SaveValue( cStoreTo, cNewVal, lIsInTable )
   IF PARAMETERS() < 3
      MESSAGEBOX( "Too few parameters passed." )
      RETURN .F.
   ENDIF
   IF lIsInTable
      REPLACE (cStoreTo) WITH (cNewVal)
   ELSE
      &cStoreTo = cNewVal
   ENDIF
   RETURN .T.
ENDFUNC
```
