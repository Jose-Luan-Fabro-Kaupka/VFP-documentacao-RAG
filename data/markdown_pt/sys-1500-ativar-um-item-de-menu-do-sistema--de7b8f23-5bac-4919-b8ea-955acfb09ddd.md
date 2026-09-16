# SYS(1500) - Ativar um item de menu do sistema

Ativa um item de menu do sistema do Visual FoxPro.

```foxpro
SYS(1500, cSystemItemName, cMenuName)
```

#### Parâmetros
 **cSystemItemName**
Especifica o nome do item de menu do sistema do Visual FoxPro a ser ativado.
**cMenuName**
Especifica o nome do menu ou submenu do sistema do Visual FoxPro que contém o item de menu.

# Valor de retorno

Character

# Observações

Consulte System Menu Names para obter uma lista de nomes de menus e itens de menu do Visual FoxPro. Você também pode usar SYS(2013) - System Menu Name String para exibir uma lista de nomes de menus e itens de menu do Visual FoxPro.

Itens de menu definidos pelo usuário e itens de menu do sistema desabilitados não podem ser ativados com SYS(1500).

SYS(1500) retorna a cadeia de caracteres vazia.

# Exemplo

O exemplo a seguir usa SYS(1500) para colar um comando em um arquivo de programa.

```foxpro
_CLIPTEXT = "MESSAGEBOX('TEST')"  && Command to paste
MODIFY COMMAND myprog NOWAIT  && Open a program file
SYS(1500, '_MED_PASTE', '_MEDIT')  && Paste menu item
```
