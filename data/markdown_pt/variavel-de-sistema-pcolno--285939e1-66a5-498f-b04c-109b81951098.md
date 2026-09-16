# Variável de sistema _PCOLNO

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Retorna ou define o número da coluna atual.

```foxpro
_PCOLNO = expN
```

# Observações

_PCOLNO contém a posição numérica da coluna atual e pode ser usada para determinar o próximo endereço de coluna da saída. O FoxPro incrementa seu valor automaticamente ao enviar saída à impressora.

Você pode atribuir qualquer inteiro de 0 a 255 para posicionar a saída na coluna desejada. Isso equivale à cláusula AT do comando ?.
