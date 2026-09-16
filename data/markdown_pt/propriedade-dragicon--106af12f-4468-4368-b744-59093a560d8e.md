# Propriedade DragIcon

Especifica o ícone exibido como ponteiro durante uma operação de arrastar e soltar. Disponível em tempo de design e de execução.

```foxpro
Control.DragIcon[ = cIcon]
```

# Valor de retorno
 **cIcon**
Especifica o arquivo que contém o ícone a ser usado como ponteiro do mouse. Normalmente, você especifica o arquivo de ícone pela janela Propriedades em tempo de design. O arquivo deve ter a extensão .cur e ser salvo no formato VGA-Mono de 2 cores, 32 x 32. Se você tentar usar um arquivo .cur colorido, será gerada uma mensagem de erro. Você pode usar ImageEdit para criar um arquivo .cur de duas cores. Se cIcon for omitido, será usado um ponteiro de seta dentro de um retângulo.

# Observações

Aplica-se a: controle CheckBox | controle ComboBox | controle CommandButton | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | controle Grid | controle Image (Visual FoxPro) | controle Label (Visual FoxPro) | controle Line | controle ListBox | controle OLE Bound | controle OLE Container | controle OptionButton | controle OptionGroup | objeto Page | controle Shape | controle Spinner | controle TextBox (Visual FoxPro)

DragIcon é útil para fornecer feedback visual durante uma operação de arrastar — por exemplo, para indicar que o controle de origem está sobre um destino apropriado. DragIcon entra em vigor quando o usuário inicia o arraste. Normalmente, você define DragIcon durante um evento MouseDown ou DragOver.

Se definir DragIcon em tempo de design e o arquivo especificado não existir, o Visual FoxPro exibirá uma mensagem de erro, mas a propriedade permanecerá definida como o arquivo especificado. O Visual FoxPro ignora DragIcon em tempo de execução se ela estiver definida como um arquivo inexistente.
