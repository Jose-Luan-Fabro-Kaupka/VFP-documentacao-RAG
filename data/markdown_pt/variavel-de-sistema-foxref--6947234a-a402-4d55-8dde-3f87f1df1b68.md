# Variável de sistema _FOXREF

Contém o nome do aplicativo que fornece a ferramenta Code References.

```foxpro
_FOXREF = cFoxRefApplication
```

#### Parâmetros
 **cFoxRefApplication**
Especifica o nome do programa Visual FoxPro usado para lidar com pesquisas de Code Reference.

# Observações

Por padrão, a variável de sistema _FOXREF aponta para o seguinte arquivo:

HOME( ) + "FoxRef.app"

Você pode alterar essa configuração na guia File Locations da caixa de diálogo Options.

Você pode chamar este aplicativo diretamente da seguinte forma:

```foxpro
DO (_FOXREF) WITH oAction
```

oAction é um objeto com as seguintes propriedades: Mode, Word, FileName, LineNo, Class, Proc e hWnd. Consulte a origem FoxRef no diretório Tools/XSource para obter mais informações sobre como esses parâmetros devem ser preenchidos.
