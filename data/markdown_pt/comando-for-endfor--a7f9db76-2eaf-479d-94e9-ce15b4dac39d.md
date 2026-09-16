# Comando FOR ... ENDFOR

Executa um conjunto de comandos um número especificado de vezes.

```foxpro
FOR VarName = nInitialValue TO nFinalValue [STEP nIncrement]
      Commands
   [EXIT]
   [LOOP]
ENDFOR | NEXT
```

#### Parâmetros
 **VarName**
Especifica o nome da variável que atua como contador. O contador acompanha o número de vezes que os comandos Visual FoxPro são executados dentro do loop FOR ... ENDFOR. A variável não precisa existir antes de executar FOR ... ENDFOR.
**nInitialValue TO nFinalValue**
Especifica os valores inicial e final do contador. Tanto nInitialValue quanto nFinalValue podem ser elementos de matriz.
**[STEP nIncrement ]**
Especifica a quantidade para incrementar ou decrementar o valor do contador. Se nIncrement for negativo, o valor do contador é decrementado. Se você omitir a cláusula STEP, VarName incrementa em 1.
**Commands**
Especifica os comandos Visual FoxPro a executar. Commands pode incluir qualquer número de comandos.
**[EXIT]**
Transfere o controle de dentro do loop FOR ... ENDFOR para o comando imediatamente após ENDFOR. Você pode colocar EXIT em qualquer lugar entre FOR e ENDFOR. Para obter mais informações, consulte EXIT Command.
**[LOOP]**
Retorna o controle para a cláusula FOR sem executar as instruções entre as palavras-chave LOOP e ENDFOR. O valor do contador incrementa ou decrementa como se ENDFOR tivesse sido alcançado. Para obter mais informações, consulte LOOP Command.
**ENDFOR**
Especifica o fim do loop FOR ... ENDFOR.
**NEXT**
Especifica o local para continuar a execução do programa depois que o valor do contador excede nFinalValue.

# Observações

Os comandos Visual FoxPro que aparecem no loop FOR são executados até que ENDFOR ou NEXT seja alcançado. O valor no contador VarName então incrementa ou decrementa pelo valor de nIncrement. O valor do contador é então comparado com nFinalValue. Se o contador for menor ou igual a nFinalValue, os comandos após a cláusula FOR são executados novamente. Se o contador for maior que nFinalValue, o loop FOR ... ENDFOR termina e a execução do programa continua com o primeiro comando após ENDFOR ou NEXT.

> **Observação:** Os valores de nInitialValue, nFinalValue e nIncrement são lidos apenas inicialmente. No entanto, alterar o valor do contador VarName dentro do loop afeta o número de vezes que o loop é executado. Alterar o valor de nFinalValue em um loop FOR não tem efeito.

# Exemplo

### Exemplo 1

No exemplo a seguir, o loop FOR ... ENDFOR exibe os números de 1 a 10 usando o comando ?:

```foxpro
FOR gnCount = 1 TO 10
   ? gnCount
ENDFOR
```

Para obter mais informações, consulte ? | ?? Command.

### Exemplo 2

O exemplo a seguir abre a tabela Customer no banco de dados de amostra TestData do Visual FoxPro, localizado no diretório Microsoft Visual FoxPro ..\Samples\Data. O loop FOR ... ENDFOR especifica um valor inicial de 1, um valor de incremento de 2 e um valor final de 10. O comando GOTO move o ponteiro de registro para o número de registro especificado pela variável `gnCount` e o comando DISPLAY exibe o nome da empresa do campo Company na tabela. O loop FOR ... ENDFOR exibe todos os registros de número ímpar dos primeiros 10 registros.

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
FOR gnCount = 1 TO 10 STEP 2
   GOTO gnCount
   DISPLAY Company
ENDFOR
```

Para obter mais informações, consulte GO | GOTO Command e DISPLAY Command.
