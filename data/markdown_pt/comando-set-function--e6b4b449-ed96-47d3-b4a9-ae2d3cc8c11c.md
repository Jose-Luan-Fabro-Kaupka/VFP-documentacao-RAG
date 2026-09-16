# Comando SET FUNCTION

Atribui uma expressão (macro de teclado) a uma tecla de função ou combinação de teclas.

```foxpro
SET FUNCTION nFunctionKeyNumber | KeyLabelName TO [eExpression]
```

#### Parâmetros
 **nFunctionKeyNumber**
Especifica o número da tecla de função atribuída à macro. Por exemplo, use SET FUNCTION 2 para especificar a tecla de função F2.
**KeyLabelName**
Especifica uma combinação de teclas, incluindo uma tecla de função, à qual atribuir a macro. O Visual FoxPro suporta combinações de teclas que incluem teclas de função. Você pode usar a tecla CTRL ou SHIFT em combinação com uma tecla de função para criar teclas programáveis adicionais. Para uma lista de expressões de rótulo de tecla, consulte ON KEY LABEL .
**TO [ eExpression ]**
Especifica a série de pressionamentos de tecla armazenada na tecla de função ou combinação de teclas. O Visual FoxPro interpreta um ponto e vírgula (;) na expressão como retorno de carro. Definições de teclas de função podem ser limpas com CLEAR MACROS.
