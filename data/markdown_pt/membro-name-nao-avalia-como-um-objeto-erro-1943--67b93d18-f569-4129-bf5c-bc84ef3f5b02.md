# Membro "name" não avalia como um objeto (Erro 1943)

Sintaxe inválida. A sintaxe indica que o próximo elemento a ser avaliado deve ser um objeto, mas não é.

Por exemplo, se você tivesse um formulário chamado `myform` com uma caixa de texto chamada `text1`, o comando `myform.txt.value = "help"` geraria esse erro. O comando deveria ser `myform.text1.value = "help"`.
