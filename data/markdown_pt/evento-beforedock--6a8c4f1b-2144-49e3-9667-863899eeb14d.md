# Evento BeforeDock

Ocorre antes de encaixar um objeto ToolBar ou um objeto Form, por exemplo, ao arrastar uma barra de ferramentas ou formulário para uma área de encaixe ou ao chamar o método Dock.

```foxpro
PROCEDURE Object.BeforeDock
LPARAMETERS nLocation
```

#### Parâmetros
 **nLocation**
Retorna a posição de encaixe para a barra de ferramentas ou formulário. A tabela a seguir lista os valores de nLocation. nLocation Descrição Constante FoxPro.h -1 Form ou barra de ferramentas será desencaixado. TOOL_NOTDOCKED 0 Form ou barra de ferramentas será encaixado na parte superior da janela principal do Visual FoxPro. TOOL_TOP 1 Form ou barra de ferramentas será encaixado na borda esquerda da janela principal do Visual FoxPro. TOOL_LEFT 2 Form ou barra de ferramentas será encaixado na borda direita da janela principal do Visual FoxPro. TOOL_RIGHT 3 Form ou barra de ferramentas será encaixado na borda inferior da janela do Visual FoxPro. TOOL_BOTTOM 4 Form será encaixado em guia com outro formulário. TOOL_TAB 5 Form será encaixado em link com outro formulário. Observação Para determinar informações adicionais sobre o destino e a posição, você precisa chamar o método GetDockState após a conclusão da operação de encaixe. Para obter mais informações, consulte Método GetDockState. TOOL_LINK

# Observações

Aplica-se a: Form Object | ToolBar Object

BeforeDock ocorre antes que o Visual FoxPro redesenhe o formulário ou a barra de ferramentas, para que você possa alterar a aparência do formulário ou da barra de ferramentas. Por exemplo, suponha que você deseja substituir um controle ComboBox no formulário por um controle CommandButton, que tem proporções diferentes. Você pode inserir código no evento BeforeDock que substitui o controle ao encaixar o formulário.

Retornar .F. (False) do código no evento ou adicionar o comando NODEFAULT não impede o encaixe. Para obter mais informações, consulte Comando NODEFAULT.
