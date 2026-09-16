# Como: passar dados a parâmetros por referência

Você pode passar dados a parâmetros por referência em todo o programa ou em locais específicos.

### Para passar parâmetros por referência em todo o programa
- Anteceda o código onde deseja passar dados a parâmetros por referência com a seguinte linha de código: SET UDFPARMS TO REFERENCE

Para obter mais informações, consulte Comando SET UDFPARMS.

### Para passar parâmetros por referência em locais específicos
- Anteceda o nome da variável ou do array com um sinal de arroba (@) conforme mostrado no exemplo a seguir: myFunc(@var1, var2)
