# Exemplo de criação de menus de atalho dinâmicos

Arquivo: ...\Samples\Solution\Menus\Dynshort.scx

Este exemplo ilustra uma maneira alternativa de criar menus de atalho.

Os menus de atalho do exemplo Display Shortcut Menus Sample foram criados no Menu Designer. As vantagens de usar o Menu Designer são a facilidade de criação, a capacidade de criar menus em cascata e a integração simples a um formulário. Contudo, é necessário um arquivo .mnx, .mnt e .mpr separado para cada menu de atalho. Após uma alteração, é preciso gerar e compilar novamente o código do menu.

O mecanismo de menu de atalho dinâmico é uma classe personalizada que pode ser adicionada a qualquer formulário: menulib em ...\Samples\Classes\Utility.vcx. O método ShowMenu dessa classe define um menu e o exibe na posição de MousePointer determinada pelas funções MROW( ) e MCOL( ).

No evento RightClick dos objetos para os quais deseja criar um menu de atalho:
 - Crie um array com os itens do menu de atalho.
- Passe o array para o método ShowMenu da classe menulib.
- Processe a escolha do usuário verificando o valor de BAR( ).

Por exemplo, o código a seguir está associado ao evento RightClick do formulário:

```foxpro
LOCAL laMenu[5]
laMenu=""
laMenu[1]="\<Center"
laMenu[2]="\<Font..."
laMenu[3]="\<Minimize"
laMenu[4]="\-"
laMenu[5]="E\<xit"
THISFORM.oMenuShortcut.ShowMenu(@laMenu)
DO CASE
   CASE BAR()=1
      THISFORM.AutoCenter=.T.
   CASE BAR()=2
      THISFORM.SetFont
   CASE BAR()=3
      THISFORM.WindowState=1
   CASE BAR()=5
      THISFORM.Release
ENDCASE
```
