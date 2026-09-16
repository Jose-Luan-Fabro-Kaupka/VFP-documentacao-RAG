# Variável de sistema _CUROBJ

Incluída para compatibilidade com versões anteriores. Use a propriedade ActiveControl para novos formulários.

Retorna ou inicializa o número do objeto @ ... GET atual.

```foxpro
_CUROBJ = expN
```

# Observações

_CUROBJ contém o número expN do objeto GET atualmente selecionado. Objetos GET são criados com @ ... GET e @ ... EDIT e incluem campos, caixas de seleção, botões de pressão e invisíveis, popups, listas e regiões de edição de texto. _CUROBJ é frequentemente consultado ou alterado em uma função definida pelo usuário chamada por uma cláusula VALID ou WHEN, ou por outras cláusulas READ e @ ... GET.

Você pode retornar o valor de _CUROBJ para determinar qual objeto está selecionado ou pode armazenar um valor em _CUROBJ para selecionar um objeto GET específico.

O número do objeto GET é determinado pela ordem em que os GETs são emitidos. Cada botão individual em um conjunto de botões de pressão, botões de opção ou botões invisíveis é considerado um objeto separado.

Você pode alterar o valor de _CUROBJ para posicionar o cursor em outro objeto GET. Isso é normalmente feito em rotinas VALID e WHEN.

# Exemplo

O seguinte programa de exemplo demonstra como os objetos GET são numerados e como _CUROBJ pode ser usado para retornar o número do objeto atual. Pressione Tab ou as teclas de seta para selecionar objetos diferentes.

Pressionar F2 exibe o número do objeto atual.

```foxpro
CLEAR
SET TALK OFF
STORE 1 to x, y, z
ON KEY LABEL F2 @ 12,2 SAY 'Object # ' + STR(_CUROBJ)	 && Show #
@ 4,2 GET x  PICTURE '@*R \
```
