# Estrutura FoxTable

A estrutura FoxTable é uma lista vinculada que controla todas as estruturas FoxInfo de determinada biblioteca.

O código a seguir ilustra sua sintaxe:

```foxpro
FoxTable _FoxTable = {nextLibrary, infoCount,infoPtr};
```

A tabela descreve os parâmetros:

| Parâmetro | Descrição |
| --- | --- |
| nextLibrary | Especifica um ponteiro usado internamente pelo Visual FoxPro e deve ser inicializado com 0. |
| infoCount | Especifica o número de rotinas externas do Visual FoxPro definidas nesta biblioteca. |
| infoPtr | Especifica o endereço do primeiro elemento de um array de estruturas FoxInfo. O nome deve corresponder ao array da instrução FoxInfo. |

O exemplo a seguir ilustra uma instrução FoxTable. Se o array FoxInfo se chamar `myFoxInfo`, você nunca precisará alterar esta instrução:

```foxpro
FoxTable _FoxTable = {
   (FoxTable  *) 0,
   sizeof( myFoxInfo) / sizeof( FoxInfo ),
   myFoxInfo
};
```

O Visual FoxPro captura falhas de proteção geral (GPFs) em controles ActiveX colocados em um formulário ou em objetos COM instanciados nele. Uma GPF passa a ser tratada como um erro interceptável do Visual FoxPro (erro de exceção OLE "name". O objeto OLE pode estar corrompido. (Erro 1440)).
