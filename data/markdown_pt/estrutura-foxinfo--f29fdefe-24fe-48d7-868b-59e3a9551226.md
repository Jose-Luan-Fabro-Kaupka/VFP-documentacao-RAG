# Estrutura FoxInfo

A estrutura FoxInfo é usada para comunicar nomes de funções e descrições de parâmetros entre o Visual FoxPro e sua biblioteca FLL.

O código a seguir ilustra a sintaxe de uma estrutura FoxInfo:

```foxpro
FoxInfo arrayname[ ] = {
   {funcName1, FPFI function1, parmCount1, parmTypes1}
   {funcName2, FPFI function2, parmCount2, parmTypes2}
      . . .
   {funcNameN, FPFI functionN, parmCountN, parmTypesN}
};
```

A tabela a seguir descreve os parâmetros nesta estrutura.

| Parameter | Description |
| --- | --- |
| arrayname | Specifies a variable of type FoxInfo. Note You can include several FoxInfo structure lines in this array. |
| funcName | Contains the name that the Visual FoxPro user calls to invoke your function. |
| function | Specifies the address of your C language routine. This is the exact (case-sensitive) name you use to define your function. |
| parmCount | Specifies the number of parameters described in the parmTypes string or one of the following flag values. The following list describes possible flag values: INTERNAL Specifies that the function cannot be called directly from Visual FoxPro. CALLONLOAD Specifies that the routine is to be called when the library is loaded. CALLONLOAD can't call any routine that returns results to Visual FoxPro. CALLONUNLOAD Specifies that the routine is to be called when the library is unloaded or when the Visual FoxPro QUIT command is issued. CALLONUNLOAD cannot call any routine that returns results to Visual FoxPro. |
| parmTypes | Describes the data type of each parameter. The following lists the valid values for parmTypes . " " No parameter. "?" Specifies that any type can be passed. In the body of the function, you'll need to check the type of the passed parameter. "C" Specifies a Character type parameter. "D" Specifies a Date type parameter. "I" Specifies an Integer type parameter. "L" Specifies a Logical type parameter. "N" Specifies a Numeric type parameter. "R" Reference. "T" Specifies a DateTime type parameter. "Y" Specifies a Currency type parameter "O" Specifies an Object type parameter |

> **Observação:** Inclua um valor de tipo para cada parâmetro passado à biblioteca. Para indicar que um parâmetro é opcional, preceda-o com um ponto (.). Somente parâmetros finais podem ser omitidos.

Por exemplo, suponha que você crie uma função que aceita um parâmetro character e um numérico. Ao especificar parmType, use "CN".

O exemplo de estrutura FoxInfo a seguir define uma biblioteca com uma função, que internamente se chama `dates` e externamente é acessada como `DATES`. A estrutura aceita um parâmetro do tipo Character:

```foxpro
FoxInfo myFoxInfo[] = {
   { "DATES", (FPFI) dates, 1, "C" }
};
```

Depois que você compilar sua biblioteca FLL com esta estrutura FoxInfo e carregá-la no Visual FoxPro usando o comando SET LIBRARY, você pode chamar esta função no Visual FoxPro com a seguinte linha de código:

```foxpro
=DATES("01/01/95")
```
