# Variável de sistema _BOX

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Imprime caixas.

```foxpro
_BOX = expL
```

# Observações

_BOX está incluída para compatibilidade com versões anteriores. Use o Report Writer.

_BOX contém um valor lógico que determina se caixas (conforme especificado com o comando DEFINE BOX) são impressas ao redor de linhas de texto. Se _BOX estiver definida como .T., o padrão, as caixas são impressas; caso contrário, não são.

Esta variável de memória do sistema afeta somente caixas que você cria com DEFINE BOX.

Você pode desenhar caixas na tela ou em uma janela com @ ... BOX ou @ ... TO.
