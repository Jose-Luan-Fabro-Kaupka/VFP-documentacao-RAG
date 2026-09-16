# Evento DragOver

Ocorre quando um controle está sendo arrastado sobre um objeto de destino.

```foxpro
PROCEDURE Object.DragOver
LPARAMETERS oSource, nXCoord, nYCoord, nState
```

#### Parâmetros

Você deve incluir uma instrução LPARAMETERS ou PARAMETERS no procedimento do evento e especificar um nome para cada parâmetro; caso contrário, ocorre um erro. O Visual FoxPro passa os parâmetros do evento DragOver na seguinte ordem:
 **oSource**
Contém uma referência ao controle que está sendo arrastado. Você pode fazer referência a propriedades e métodos do controle com este parâmetro.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) do ponteiro do mouse no Form quando os dados são arrastados sobre um destino de soltar. Essas coordenadas são expressas em termos do sistema de coordenadas do Form na unidade de medida especificada pela propriedade ScaleMode do Form. '
**nState**
Contém um número que representa o estado de transição do controle que está sendo arrastado em relação ao objeto de destino: Configuração Descrição 0 Enter. O controle está sendo arrastado dentro do intervalo de um destino. 1 Leave. O controle está sendo arrastado para fora do intervalo de um destino. 2 Over. O controle se moveu de uma posição no destino para outra.
**Use nState para determinar ações em pontos-chave de transição. Por exemplo, você pode destacar um possível destino em nState = 0 (Enter) e restaurar a aparência do objeto em nState = 1 (Leave).**

Quando um objeto recebe um evento DragOver com nState = 0 (Enter):
 - Um evento DragDrop é disparado se o controle de origem for solto em um objeto de destino.
- Outro evento DragOver é disparado com nState = 1 (Leave) se o controle de origem não for solto em um destino válido.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

O objeto sob o ícone de arrastar é o objeto de destino e responde ao evento DragOver. Você pode usar este evento para monitorar quando o ponteiro do mouse entra, sai ou está diretamente sobre um objeto de destino.

Use um evento DragOver para determinar o que acontece depois que a operação de arrastar é iniciada e antes que um controle seja solto em um destino. Por exemplo, você pode verificar um intervalo de destino válido destacando o destino, definindo a propriedade BackColor ou ForeColor ou exibindo um ponteiro especial.
