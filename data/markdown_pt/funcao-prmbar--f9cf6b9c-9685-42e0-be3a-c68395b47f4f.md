# Função PRMBAR( )

Retorna o texto de um item de menu.

```foxpro
PRMBAR(cMenuName, nMenuItemNumber)
```

#### Parâmetros
 **cMenuName**
Especifica o nome do menu.
**nMenuItemNumber**
Especifica o número do item de menu cujo texto PRMBAR( ) retorna. Por exemplo, se nMenuItemNumber for 1, o texto do primeiro item de menu é retornado; se nMenuItemNumber for 2, o texto do segundo item de menu é retornado, e assim por diante. A expressão deve ser pelo menos 1 e não maior que o número de itens de menu no menu.

# Valor de retorno

Character

# Observações

Menus são criados com DEFINE POPUP, que cria o menu, e DEFINE BAR, que cria os itens de menu no menu. PRMBAR( ) também funciona com um menu de sistema do Visual FoxPro. PRMBAR( ) retorna o texto que aparece no item de menu. O menu não precisa estar ativo.

Se um item de menu foi criado usando os caracteres barra invertida e menor que (\<) para criar uma tecla de acesso, ou uma barra invertida (\) para desabilitar o item de menu, PRMBAR( ) retorna somente o texto do item de menu; não inclui esses caracteres especiais. PRMBAR( ) retorna uma cadeia de caracteres vazia quando um item de menu é um separador criado com os caracteres barra invertida e hífen (\-).
