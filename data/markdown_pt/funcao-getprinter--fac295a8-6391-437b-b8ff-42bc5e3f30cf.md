# Função GETPRINTER( )

Exibe a caixa de diálogo Printer e retorna o nome da impressora selecionada.

```foxpro
GETPRINTER()
```

# Valor de retorno

Character. GETPRINTER( ) retorna o nome da impressora selecionada. Se você sair da caixa de diálogo Printer pressionando ESC ou clicando em Cancel ou Close, GETPRINTER( ) retorna uma cadeia de caracteres vazia.

# Observações

O conteúdo da caixa de diálogo Printer pode diferir entre versões do Windows. Por exemplo, a caixa de diálogo Printer pode conter somente o nome da impressora ou incluir um caminho de rede.

# Exemplo

O exemplo a seguir limpa a janela principal do Visual FoxPro usando o comando CLEAR. A variável `cPrinter` armazena o valor de retorno de GETPRINTER( ), que exibe a caixa de diálogo Printer, e o comando WAIT WINDOW exibe o nome da impressora selecionada ou "No printer chosen" se nenhuma impressora foi escolhida.

```foxpro
CLEAR
cPrinter = GETPRINTER()
WAIT WINDOW IIF(EMPTY(cPrinter), 'No printer chosen', cPrinter)
```
