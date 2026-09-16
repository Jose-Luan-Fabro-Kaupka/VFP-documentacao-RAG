# Função MRKBAR( )

Determina se um item de menu em um menu definido pelo usuário ou no menu do sistema do Microsoft Visual FoxPro está marcado.

```foxpro
MRKBAR(cMenuName, nMenuItemNumber | cSystemMenuItemName)
```

#### Parâmetros
 **cMenuName**
Especifica o nome do menu que contém o item de menu. O menu pode ser um menu do sistema do Visual FoxPro (como _MFILE, MEDIT ou _MDATA).
**nMenuItemNumber**
Especifica o número de um item de menu em um menu definido pelo usuário. O número de um item de menu é especificado quando o item de menu é criado com DEFINE BAR.
**cSystemMenuItemName**
Especifica o nome de um item de menu do sistema do Visual FoxPro. Por exemplo, o seguinte comando exibe um valor lógico especificando se o item de menu New no menu File está marcado. ? MRKBAR('_MFILE', _MFI_NEW)

# Valor de retorno

Logical

# Observações

Use SET MARK OF para marcar ou desmarcar um item de menu.

Se o item de menu especificado estiver marcado, MRKBAR( ) retorna verdadeiro (.T.); caso contrário, MRKBAR( ) retorna falso (.F.).

Para um exemplo de uso de MRKBAR( ), consulte CNTBAR( ) Function.
