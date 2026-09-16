# Função GETBAR( )

Retorna o número de um item em um menu definido com DEFINE POPUP ou no menu do sistema Visual FoxPro.

```foxpro
GETBAR(MenuItemName, nMenuPosition)
```

#### Parâmetros
 **MenuItemName**
Especifica o item de menu.
**nMenuPosition**
Especifica uma posição no menu. nMenuPosition pode variar de 1 até o número de itens no menu. 1 corresponde ao primeiro item do menu, 2 ao segundo item e assim por diante.

# Valor de retorno

Numérico

# Observações

Use GETBAR( ) para determinar qual item ocupa uma posição específica em um menu. Esta função é útil quando itens em um menu são adicionados, removidos ou reorganizados. Use DEFINE BAR para adicionar um item a um menu ou RELEASE BAR para remover um item. A posição dos itens em um menu pode ser alterada se MOVER for incluído quando o menu é criado com DEFINE POPUP.

# Exemplo

O exemplo a seguir cria um menu chamado `popDemo`. A palavra-chave MOVER é incluída para que os itens do menu possam ser reorganizados. Para obter informações sobre como reorganizar itens de menu, consulte a cláusula MOVER no Comando DEFINE POPUP.

O menu é ativado e uma série de funções GETBAR( ) são usadas em PRMBAR( ) para retornar as legendas de cada item. Depois de reorganizar os itens, pressione CTRL+Z para exibir a nova ordem dos itens.

```foxpro
CLEAR
ON KEY LABEL CTRL+Z DO showorder
WAIT WINDOW "Press CTRL+Z to refresh." NOWAIT
DEFINE POPUP popDemo MOVER FROM 2,2
DEFINE BAR 1 OF popDemo PROMPT 'One'
DEFINE BAR 2 OF popDemo PROMPT 'Two'
DEFINE BAR 3 OF popDemo PROMPT 'Three'
DEFINE BAR 4 OF popDemo PROMPT 'Four'
DO showorder
ACTIVATE POPUP popDemo
PROCEDURE showorder
CLEAR
@ 3,12 SAY  '1 ' + PRMBAR('popDemo', GETBAR('popDemo',1))
@ 4,12 SAY  '2 ' + PRMBAR('popDemo', GETBAR('popDemo',2))
@ 5,12 SAY  '3 ' + PRMBAR('popDemo', GETBAR('popDemo',3))
@ 6,12 SAY  '4 ' + PRMBAR('popDemo', GETBAR('popDemo',4))
RETURN
```
