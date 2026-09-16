# Função RGB( )

Retorna um único valor de cor a partir de um conjunto de componentes de cor vermelho, verde e azul.

```foxpro
RGB(nRedValue, nGreenValue, nBlueValue)
```

#### Parâmetros
 **nRedValue**
Especifica a intensidade do componente de cor vermelho. nRedValue pode variar de 0 a 255. Zero é a intensidade mínima de cor; 255 é a intensidade máxima de cor.
**nGreenValue**
Especifica a intensidade do componente de cor verde. nGreenValue pode variar de 0 a 255.
**nBlueValue**
Especifica a intensidade do componente de cor azul. nBlueValue pode variar de 0 a 255.

# Observações

O valor retornado por RGB( ) pode ser usado para definir propriedades de cor como BackColor e ForeColor.

# Exemplo

O exemplo a seguir usa RGB( ) para alterar a cor de fundo de um Form para azul.

```foxpro
goMyForm = CREATEOBJECT('FORM')  && Create a form
goMyForm.Show  && Display the form
WAIT WINDOW 'Press a key to change the form color'
goMyForm.BackColor=RGB(0,0,255)  && Change the form background color
WAIT WINDOW 'Press a key to release the form'
RELEASE goMyForm  && Release the form from memory
```
