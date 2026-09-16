# Como: criar procedimentos e funções

Você pode criar procedimentos e funções programaticamente.

### Para criar um procedimento
- Inicie a definição do procedimento com o comando PROCEDURE e o nome do procedimento.
- Para definir parâmetros, na segunda linha da definição do procedimento, inclua uma instrução LPARAMETERS ou PARAMETERS com uma lista de parâmetros. -OU- Na mesma linha da instrução PROCEDURE e imediatamente após o nome do procedimento, inclua uma lista de parâmetros entre parênteses.
- Nas linhas seguintes, inclua as instruções de código que deseja executar no procedimento.
- Encerre a definição do procedimento com a palavra-chave ENDPROC.

Por exemplo, as linhas de código a seguir mostram um exemplo básico de procedimento:

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

Por padrão, os valores são passados aos procedimentos por referência. Portanto, alterações feitas nos valores passados no procedimento são retornadas ao programa chamador.

Para obter mais informações, consulte Comando PROCEDURE, Comando PARAMETERS e Comando LPARAMETERS.

### Para criar uma função
- Inicie a definição da função com o comando FUNCTION e o nome da função.
- Para definir parâmetros, na segunda linha da definição do procedimento, inclua uma instrução LPARAMETERS ou PARAMETERS com uma lista de parâmetros. -OU- Na mesma linha da instrução FUNCTION e imediatamente após o nome da função, inclua uma lista de parâmetros entre parênteses.
- Nas linhas seguintes, inclua as instruções de código que deseja executar na função.
- Inclua uma instrução RETURN quando desejar retornar um valor da função e devolver o controle da execução de código ao programa chamador.
- Encerre a definição do procedimento com a palavra-chave ENDFUNC.

Por exemplo, as linhas de código a seguir mostram um exemplo básico de função:

```foxpro
FUNCTION myFunction
  LPARAMETERS myPar1, myPar2
  myFuncReturnValue = myPar1 + myPar2
  RETURN myFuncReturnValue
ENDFUNC
```

-OU-

```foxpro
FUNCTION myFunction(myPar1, myPar2)
  myFuncReturnValue = myPar1 + myPar2
  RETURN myFuncReturnValue
ENDFUNC
```

Por padrão, os valores são passados a funções definidas pelo usuário por valor. Portanto, alterações feitas nos valores passados na função não são retornadas ao programa chamador.

Para obter mais informações, consulte Comando FUNCTION, Comando PARAMETERS e Comando LPARAMETERS.
