# Função GETCOLOR( )

Exibe a caixa de diálogo Cor do Windows e retorna o número da cor escolhida.

```foxpro
GETCOLOR([nDefaultColorNumber])
```

#### Parâmetros
 **nDefaultColorNumber**
Especifica a cor que é selecionada inicialmente quando a caixa de diálogo Cor é exibida. Se nDefaultColorNumber não corresponde a uma cor na caixa de diálogo Cor, a primeira cor na caixa de diálogo Cor é selecionada. Se você omitir nDefaultColorNumber, o preto é selecionado.

# Valor de retorno

Numeric

# Observações

GETCOLOR( ) retorna – 1 se você sair da caixa de diálogo Cor pressionando ESC, escolhendo o botão Cancelar ou escolhendo Fechar no menu Controle.

# Exemplo

O exemplo a seguir exibe a caixa de diálogo Cor do Windows com a cor vermelha selecionada. Um número correspondente à cor que você escolhe é exibido quando você sai da caixa de diálogo.

```foxpro
CLEAR
? GETCOLOR(255)
```
