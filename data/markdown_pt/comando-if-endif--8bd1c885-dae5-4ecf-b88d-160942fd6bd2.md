# Comando IF ... ENDIF

Executa condicionalmente um conjunto de comandos com base no valor de uma expressão lógica.

```foxpro
IF lExpression [THEN]
      Commands
[ELSE
      Commands]
ENDIF
```

#### Parâmetros
 **lExpression**
Especifica a expressão lógica que é avaliada. Se lExpression avaliar como true (.T.), quaisquer comandos após IF ou THEN e antes de ELSE ou ENDIF (o que ocorrer primeiro) são executados. Se lExpression for false (.F.) e ELSE estiver incluído, quaisquer comandos após ELSE e antes de ENDIF são executados. Se lExpression for false (.F.) e ELSE não estiver incluído, todos os comandos entre IF e ENDIF são ignorados. Neste caso, a execução do programa continua com o primeiro comando após ENDIF.

# Observações

Você pode aninhar um bloco IF ... ENDIF dentro de outro bloco IF ... ENDIF.

Comentários precedidos por && podem ser colocados na mesma linha após IF, THEN, ELSE e ENDIF. Esses comentários são ignorados durante a compilação e a execução do programa.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open customer table
GETEXPR 'Enter condition to locate ' TO gcTemp;
   TYPE 'L' DEFAULT 'COMPANY = ""'
LOCATE FOR &gcTemp  && Enter LOCATE expression
IF FOUND()  && Was it found?
   DISPLAY  && If so, display the record
ELSE  && If not found
   ? 'Condition ' + gcTemp + ' was not found '   && Display a message
ENDIF
USE
```
