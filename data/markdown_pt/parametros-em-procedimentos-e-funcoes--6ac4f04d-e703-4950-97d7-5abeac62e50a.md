# Parâmetros em procedimentos e funções

Quando um programa chama um procedimento ou função, ele pode passar dados ao procedimento ou função para processamento. No entanto, quando você cria um procedimento ou função que realiza operações em dados passados a ele pelo programa chamador, o procedimento ou função deve conter parâmetros em sua definição para manipular os dados. As seções a seguir contêm informações sobre como trabalhar com parâmetros:
 - Definindo parâmetros em procedimentos e funções
- Passando dados a procedimentos e funções

# Definindo parâmetros em procedimentos e funções

Quando um programa passa dados a um procedimento ou função, os parâmetros no procedimento ou função manipulam esses dados para que o procedimento ou função possa realizar operações nos dados. Quando você deseja criar procedimentos e funções que processam dados que o programa chamador passa a eles, você precisa incluir parâmetros nas definições de procedimento e função.

As linhas de código a seguir ilustram o formato básico para incluir parâmetros na definição de procedimento:

```foxpro
PROCEDURE myProcedure
   LPARAMETERS Par1, Par2, Par3, ...
   * Insert procedure code.
ENDPROC
```

-OU-

```foxpro
PROCEDURE myProcedure(Par1, Par2, Par3, ...)
  * Insert procedure code.
ENDPROC
```

O primeiro procedimento inclui uma instrução LPARAMETERS que pode conter um ou mais parâmetros. O segundo procedimento lista os mesmos parâmetros entre parênteses (()) imediatamente após o nome do procedimento. Usar a instrução LPARAMETERS ou colocar a lista de parâmetros entre parênteses define os parâmetros com escopo local para o procedimento. Você também pode usar a palavra-chave PARAMETERS em vez de LPARAMETERS para aceitar parâmetros com escopo privado. Você pode passar vários valores a um procedimento ou função separando os valores com vírgulas.

Por exemplo, os exemplos a seguir mostram definições de procedimento que incluem parâmetros. O primeiro procedimento inclui uma instrução LPARAMETERS e dois parâmetros, `myPar1` e `myPar2`. O segundo procedimento lista os mesmos parâmetros entre parênteses (()) imediatamente após o nome do procedimento. Ambos os procedimentos adicionam o valor em `myPar2` a `myPar1` e atribuem o resultado a `myPar1`. Por padrão, os dados são passados aos procedimentos por referência, portanto o novo valor de `myPar1` substitui seu valor original.

```foxpro
PROCEDURE myProcedure
   LPARAMETERS myPar1, myPar2
   myPar1 = myPar1 + myPar2
ENDPROC
```

-OU-

```foxpro
PROCEDURE myProcedure(myPar1, myPar2)
  myPar1 = myPar1 + myPar2
ENDPROC
```

Você pode incluir parâmetros de forma semelhante em uma definição de função. Para obter mais informações, consulte Comando PROCEDURE, Comando FUNCTION, Comando LPARAMETERS e Comando PARAMETERS.

# Passando dados a procedimentos e funções

Você pode passar dados, ou especificamente, "argumentos", do seu programa para procedimentos e funções de diferentes maneiras, dependendo do seguinte:
 - Se você deseja passar dados por referência ou por valor. Para obter mais informações, consulte Passando dados a parâmetros.
- Como você chama o procedimento ou função. Para obter mais informações, consulte Como: chamar procedimentos e funções.

Por exemplo, quando você chama um procedimento com o comando DO, você pode passar dados usando a cláusula WITH e uma lista de parâmetros. No exemplo a seguir, as variáveis `myVar` e `myVar2` contêm os valores 4 e 5. Quando você chama o procedimento `myProcedure` usando o comando DO, a lista de parâmetros na cláusula WITH passa as variáveis ao procedimento:

```foxpro
myVar = 4
myVar2 = 5
DO myProcedure WITH myVar, myVar2
```

Por padrão, variáveis e matrizes são passadas aos procedimentos por referência. Portanto, alterações feitas no procedimento em variáveis e matrizes passadas são retornadas ao programa chamador. Por exemplo, suponha que o procedimento incremente o valor em `myVar` pelo valor em `myVar2`. O valor modificado de `myVar` torna-se o novo valor de `myVar` quando o procedimento retorna o controle ao programa chamador.

Alternativamente, se você deseja usar o comando DO mas passar dados por valor, coloque cada parâmetro entre parênteses (()) como mostrado no exemplo a seguir:

```foxpro
DO myProcedure WITH (myVar), (myVar2)
```

Quando você chama uma função, você pode passar dados usando uma lista de parâmetros entre parênteses (()) como mostrado na linha de código a seguir:

```foxpro
myFunction(myVar, myVar2)
```

Por padrão, variáveis e matrizes são passadas a funções definidas pelo usuário por valor. Portanto, alterações feitas na função em variáveis e matrizes passadas não são retornadas ao programa chamador. No entanto, você pode passar variáveis e matrizes por referência prefixando variáveis e matrizes com o sinal de arroba (@) como mostrado na linha de código a seguir:

```foxpro
myFunction(@var1, @var2, ...)
```

A tabela a seguir resume as maneiras pelas quais você pode passar variáveis a procedimentos e funções no exemplo.

| Chamada de procedimento ou função | Comentários |
| --- | --- |
| DO myProcedure WITH var1, var2, ... | Chama um procedimento e passa variáveis por referência. |
| DO myProcedure WITH (var1), (var2), ... | Chama um procedimento e passa variáveis por valor. |
| myFunction(var1, var2, ...) | Chama uma função e passa variáveis por valor. |
| myFunction(@var1, @var2, ...) | Chama uma função e passa variáveis por referência. |
