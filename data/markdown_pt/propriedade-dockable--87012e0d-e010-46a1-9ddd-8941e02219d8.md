# Propriedade Dockable

Determina se um formulário pode ser encaixado. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Form.Dockable [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor que determina se um formulário pode ser encaixado. A tabela a seguir lista os valores de nValue . nValue Descrição 0 O formulário não suporta encaixe. (Padrão) 1 O formulário suporta encaixe e é encaixável. A propriedade HalfHeightCaption é definida como True (.T.) . 2 O formulário suporta encaixe, mas não é encaixável. A propriedade HalfHeightCaption é definida como True (.T.) . Observação Antes de definir Dockable como 1 ou 2 , a propriedade ScrollBars deve ser 0 (None) , a propriedade ShowWindow deve ser 0 (In Screen) e Desktop deve ser False (.F.) . As propriedades ScrollBars , ShowWindow e Desktop são somente leitura em tempo de execução. Para obter mais informações, consulte Propriedade ScrollBars e Propriedade ShowWindow .

# Observações

Aplica-se a: Objeto Form

Formulários que fazem parte de um conjunto de formulários não suportam encaixe.

Se a propriedade Dockable mudar quando um formulário está encaixado, o formulário é desencaixado automaticamente.

Quando o formulário suporta encaixe, ou seja, Dockable está definido como 1 ou 2, você pode definir interativamente o formulário como encaixável usando um de dois métodos:
 - No menu Window, clique em Dockable .

-OU-
 - Clique com o botão direito na barra de título do formulário e clique em Dockable no menu de atalho.

Executar qualquer uma dessas ações alterna a configuração de Dockable entre 1 e 2.

Quando Dockable é definido como um valor maior que 0, o Visual FoxPro define as propriedades na tabela a seguir automaticamente e ignora alterações feitas a essas propriedades. Definir Dockable como 0 não reverte essas propriedades para seus valores anteriores.

| Propriedade | Configuração | Observações |
| --- | --- | --- |
| Propriedade AlwaysOnBottom | .F. | |
| Propriedade AlwaysOnTop | .F. | |
| Propriedade BorderStyle | 3 | |
| Propriedade Closable | .T. | |
| Propriedade Desktop | .F. | Somente leitura em tempo de execução. |
| Propriedade Enabled (Visual FoxPro) | .T. | |
| Propriedade HalfHeightCaption | .T. | |
| Propriedade MaxButton | .F. | Usada apenas quando Dockable está definido como 2. |
| Propriedade MDIForm | .F. | |
| Propriedade MinButton | .F. | Usada apenas quando Dockable está definido como 2. |
| Propriedade Movable | .T. | |
| Propriedade ScrollBars | 0. | Somente leitura em tempo de execução. |
| Propriedade ShowWindow | 0. | Somente leitura em tempo de execução. |
| Propriedade TitleBar | 1 | |
| Propriedade Visible (Visual FoxPro) | .T. | |
| Propriedade WindowState (Visual FoxPro) | 0 | |
| Propriedade WindowType | 0 | |

Quando Dockable é definido como um valor maior que 0, o Visual FoxPro ignora completamente as seguintes propriedades:
 - Propriedade MaxLeft
- Propriedade MaxTop
- Propriedade MaxWidth
- Propriedade MinHeight
- Propriedade MinWidth

Quando um formulário está encaixado, as seguintes propriedades são somente leitura:
 - Propriedade Left
- Propriedade Top
- Propriedade Width
- Propriedade Height

# Exemplo

O exemplo a seguir usa a função CREATEOBJECT( ) para criar um formulário, define as propriedades Dockable e Visible para que o formulário seja encaixável e visível, e usa o método Dock para encaixar o formulário no lado esquerdo da janela principal do Visual FoxPro.

```foxpro
omyForm = CREATEOBJECT("Form")
omyForm.Dockable = 1
omyForm.Visible = .T.
omyForm.Dock(1)
```
