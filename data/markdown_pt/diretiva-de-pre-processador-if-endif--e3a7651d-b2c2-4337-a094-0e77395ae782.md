# Diretiva de pré-processador #IF ... #ENDIF

Inclui condicionalmente código-fonte em tempo de compilação.

```foxpro
#IF nExpression1 | lExpression1
      Commands
[#ELIF nExpression2 | #ELIF lExpression2
      Commands...
#ELIF nExpressionN | #ELIF lExpressionN
      Commands]
[#ELSE
      Commands]
#ENDIF
```

#### Parâmetros
 **#IF nExpression1 | lExpression1Commands**
nExpression1 especifica a expressão numérica que é avaliada. Se a expressão for diferente de zero, os comandos imediatamente após #IF são incluídos no código compilado. A estrutura #IF ... #ENDIF é encerrada e a primeira linha do programa após #ENDIF é então compilada. Se a expressão for 0, os comandos imediatamente após #IF não são incluídos no código compilado. Quaisquer diretivas #ELIF subsequentes são avaliadas. lExpression1 especifica a expressão lógica que é avaliada. Se a expressão for verdadeira (.T.), os comandos imediatamente após #IF são incluídos no código compilado. A estrutura #IF ... #ENDIF é encerrada e a primeira linha do programa após #ENDIF é então compilada. Se a expressão for falsa (.F.), os comandos imediatamente após #IF não são incluídos no código compilado. Quaisquer diretivas #ELIF subsequentes são avaliadas. Observação Não especifique variáveis de sistema para nExpression1 ou lExpression1. Variáveis de sistema não são avaliadas até o tempo de execução.
**#ELIF nExpression2 | #ELIF lExpression2Commands**
...
**#ELIF nExpressionN | #ELIF lExpressionNCommands**
Se nExpression1 for 0 ou lExpression1 for falsa (.F.), as diretivas #ELIF são avaliadas. A primeira expressão #ELIF nExpression2 ou lExpression2, se presente, é avaliada. Se nExpression2 for diferente de zero ou lExpression2 for verdadeira (.T.), os comandos após #ELIF são incluídos no código compilado. A estrutura #IF ... #ENDIF é encerrada e a primeira linha do programa após #ENDIF é então compilada. Se nExpression2 for 0 ou lExpression2 for falsa (.F.), os comandos após #ELIF não são incluídos no código compilado. A próxima diretiva #ELIF é avaliada.
**#ELSE Commands**
Se nenhuma diretiva #ELIF for incluída, ou se as que estão incluídas forem avaliadas como 0 ou falsa (.F.), a presença ou ausência de #ELSE determina se comandos adicionais são incluídos no código compilado: Se #ELSE for incluído, os comandos após #ELSE são incluídos no código compilado. Se #ELSE não for incluído, nenhum dos comandos entre #IF e #ENDIF é incluído no código compilado. A estrutura #IF ... #ENDIF é encerrada e a compilação continua na primeira linha do programa após #ENDIF.
**#ENDIF**
Indica o fim da instrução #IF.

# Observações

#IF ... #ENDIF pode melhorar a legibilidade do código-fonte, reduzir o tamanho do programa compilado e, em alguns casos, melhorar o desempenho.

Quando a estrutura #IF ... #ENDIF é compilada, expressões lógicas ou numéricas sucessivas dentro da estrutura são avaliadas. Os resultados da avaliação determinam qual conjunto de comandos do Visual FoxPro (se houver) é incluído no código compilado.

# Exemplo

No exemplo a seguir, a estrutura #IF ... #ENDIF determina qual versão do Visual FoxPro compila o programa e então exibe a mensagem apropriada.

```foxpro
#If SYS(3004) = "1033"
? "Locale ID is English"
#Elif SYS(3004) = "1034"
? "Locale ID is Spanish"
#Elif SYS(3004) = "1031"
? "Locale ID is German"
#Elif SYS(3004) = "1036"
? "Locale ID is French"
#Endif
```
