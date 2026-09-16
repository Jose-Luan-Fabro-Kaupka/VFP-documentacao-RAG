# Propriedade LanguageOptions

Esta propriedade do objeto de aplicativo fornece a capacidade de controlar configurações gerais de linguagem do Visual FoxPro. Isso inclui a capacidade de verificar variáveis de memória declaradas incorretamente.

```foxpro
_VFP.LanguageOptions [= eValue]
```

# Valor de retorno
 **eValue ,**
Bit Valor Descrição 1 Declaração de tipo estrita é necessária para variáveis de memória.

# Observações

Aplica-se a: Application Object | Variável de sistema _VFP

Quando LanguageOptions está definido como 1, você deve declarar todas as variáveis de memória e matrizes como LOCAL ou PUBLIC antes de usá-las. Uma tentativa de usar uma variável ou matriz não declarada gerará saída na janela DEBUG OUTPUT. Nenhum erro é gerado. Você pode registrar essa saída em um arquivo como no código a seguir:

```foxpro
   SET DEBUGOUT TO MyErrorFile
```

A saída de variáveis não declaradas em LanguageOptions é delimitada por vírgulas no seguinte formato:

`LangOptionsErr, DateTime, cLineNo, cProcedure|cMethod, cFileName, cVarName`

| Item | Descrição |
| --- | --- |
| LangOptionsErr | Especifica o nome do tipo de saída para pesquisas e filtros |
| DateTime | Especifica o carimbo de data/hora da execução (= DATETIME( )) |
| cLineNo | Especifica o número da linha onde o erro ocorreu (=LINENO( )) |
| cProcedure | cMethod | Especifica o nome do procedimento ou método em que o erro ocorreu ( = PROGRAM( )) |
| cFileName | Especifica o nome do arquivo em que o erro ocorreu. (=SYS(16( )) |
| cVarName | Especifica o nome da variável não declarada |

Declarar variáveis PRIVATE não cria uma variável (diferente de declarar variáveis PUBLIC ou LOCAL), portanto o código a seguir gera uma entrada de log:

```foxpro
   PRIVATE myvar
   myvar = 1
```

Comandos que criam variáveis dinamicamente, como SCATTER ... NAME, REPORT ... NAME e outros, gerarão entradas de log, porque essas variáveis são criadas como PRIVATE.

# Exemplo

O código a seguir mostra a saída de depuração resultante da entrada de uma variável não declarada, myvar.

```foxpro
_VFP.LanguageOptions=1
myvar=4
```

A tipagem estrita no Visual FoxPro é aplicada apenas em tempo de execução, portanto você deve executar o código para detectar erros. A tipagem estrita afeta as versões de desenvolvimento e de tempo de execução do Visual FoxPro.

> **Observação:** O uso de variáveis private, como as declaradas com o comando PRIVATE ou as criadas usando a cláusula NAME de certos comandos, gerará erros. Se você estiver distribuindo código que pode ser afetado por desenvolvedores que potencialmente definem essa propriedade como 1, você deve proteger seu código redefinindo essa propriedade como 0 quando necessário.
