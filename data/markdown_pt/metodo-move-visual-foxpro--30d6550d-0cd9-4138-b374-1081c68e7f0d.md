# Método Move (Visual FoxPro)

Move um objeto.

```foxpro
Object.Move (nLeft [, nTop [, nWidth [, nHeight]]])
```

#### Parâmetros
 **nLeft**
Especifica a coordenada horizontal da borda esquerda do objeto. nLeft é um valor de precisão simples.
**nTop**
Especifica a coordenada vertical da borda superior do objeto. nTop é um valor de precisão simples.
**nWidth**
Especifica a nova largura do objeto. nWidth é um valor de precisão simples.
**nHeight**
Especifica a nova altura do objeto. nHeight é um valor de precisão simples.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

Somente o argumento nLeft é obrigatório. No entanto, para incluir qualquer outro argumento, você também deve incluir todos os argumentos na sintaxe anteriores ao argumento que deseja incluir. Por exemplo, não é possível especificar nWidth sem especificar nLeft e nTop. Quaisquer argumentos finais não especificados permanecem inalterados.

Mover um Form na tela ou mover um controle em um formulário é sempre relativo à origem (0,0), que é o canto superior esquerdo. Ao mover controles em um contêiner, o sistema de coordenadas do contêiner é usado.
