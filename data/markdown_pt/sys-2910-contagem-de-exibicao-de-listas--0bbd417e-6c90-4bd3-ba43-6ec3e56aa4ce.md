# SYS(2910) — Contagem de exibição de listas

Define ou retorna o número de itens a exibir em caixas de listagem suspensas.

```foxpro
SYS(2910 [, nValue])
```

#### Parâmetros
**nValue**
O parâmetro nValue determina quantos itens ficam visíveis em uma caixa de listagem suspensa. Isso inclui caixas de listagem suspensas de AutoComplete, IntelliSense, Method Editor, a lista suspensa de objetos da janela Properties etc. O intervalo de nValue é de 5 a 200. O valor padrão é 15. Omitir nValue retorna a configuração atual.

# Valor de retorno

Caractere. A contagem de exibição atual da caixa de listagem suspensa é retornada como uma cadeia de caracteres.

# Observações

Em tempo de design, o valor da contagem de exibição é armazenado no Registro quando você escolhe o botão Set As Default na caixa de diálogo Options (Visual FoxPro) e é restaurado na próxima vez que o Visual FoxPro é executado. Definir um valor com esta função não grava o valor no Registro, a menos que você escolha o botão Set As Default na caixa de diálogo Options.
