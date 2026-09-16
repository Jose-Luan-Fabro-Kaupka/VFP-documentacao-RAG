# SYS(18) - Controle atual

Incluído para compatibilidade com versões anteriores. Use a propriedade ActiveControl em vez disso.

Retorna em maiúsculas o nome da variável de memória, elemento de matriz ou campo usado para criar o controle @ ... GET atual.

```foxpro
SYS(18)
```

# Valor de retorno

Valor de retorno - Caractere

# Observações

Controles são caixas de seleção, campos, invisíveis, botões push ou de opção, listas, popups, spinners ou regiões de edição de texto. Se uma janela Browse, Change ou Edit está ativa, o nome do campo atual é retornado.

SYS(18) é idêntico a VARREAD(). Ambos podem ser usados para passar o nome do controle atual a uma procedure.
