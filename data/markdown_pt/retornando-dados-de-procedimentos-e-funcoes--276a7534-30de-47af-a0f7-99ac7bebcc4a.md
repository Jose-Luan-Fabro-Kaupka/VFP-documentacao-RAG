# Retornando dados de procedimentos e funções

Convencionalmente, funções retornam valores ao programa chamador. Entretanto, no Visual FoxPro, você pode retornar valores de procedimentos e funções. Quando procedimentos e funções não incluem instruções RETURN explícitas que retornem um valor especificado, o Visual FoxPro inclui automaticamente uma instrução RETURN implícita que retorna o valor padrão True (.T.). Em geral, use o comando RETURN para retornar um valor específico de funções, por exemplo, como resultado de processamento ou para indicar se a operação da função foi bem-sucedida.

> **Observação:** O comando RETURN também devolve ao programa chamador o controle da execução do código. Para obter mais informações, consulte Comando RETURN.

No exemplo a seguir, suponha que você passe uma data à função. Ela retorna uma data 14 dias posterior:

```foxpro
FUNCTION plus2weeks
   PARAMETERS dDate
   RETURN dDate + 14
ENDFUNC
```

Você pode atribuir o valor retornado pela função a uma variável, conforme mostrado:

```foxpro
dDeadLine = plus2weeks(DATE())
```

# Atribuindo valores retornados por procedimentos e funções

Você pode atribuir explicitamente valores retornados por procedimentos e funções, por exemplo, a uma variável usando o operador de igualdade (=), ou passar o valor retornado diretamente, por exemplo, para outra função.

No exemplo a seguir, suponha que a função `myFunc` retorne um valor específico. A primeira linha atribui o valor retornado por `myFunc` à variável `myVar`. A segunda passa esse valor diretamente à função STR( ) do Visual FoxPro, cujo resultado é exibido na janela de saída ativa atual usando o comando ?:

```foxpro
myVar = myFunc()
? STR( myFunc() )
```
