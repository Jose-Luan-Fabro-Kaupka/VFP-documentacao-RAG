# Como: passar dados a parâmetros por valor

Você pode passar parâmetros por valor em todo o programa ou em locais específicos.

### Para passar parâmetros por valor em todo o programa
- Antes do código em que deseja passar dados a parâmetros por valor, inclua a seguinte linha de código: SET UDFPARMS TO VALUE

> **Observação:** Usar SET UDFPARMS TO VALUE não afeta a cláusula WITH no comando DO, que, por padrão, passa argumentos a parâmetros por referência.

Para obter mais informações, consulte Comando SET UDFPARMS.

### Para passar parâmetros por valor em locais específicos
- Coloque o nome da variável ou matriz entre parênteses (()) conforme mostrado no exemplo a seguir: DO myProcedure WITH (myVar), (myVar2)
