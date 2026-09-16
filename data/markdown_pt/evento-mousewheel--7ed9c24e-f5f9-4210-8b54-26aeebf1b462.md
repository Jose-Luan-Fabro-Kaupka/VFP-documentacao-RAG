# Evento MouseWheel

Ocorre quando o usuário gira a roda do mouse em um dispositivo de mouse que possui roda.

```foxpro
PROCEDURE Object.MouseWheel
LPARAMETERS nDirection, nShift, nXCoord, nYCoord
```

#### Parâmetros

Você deve incluir uma instrução LPARAMETERS ou PARAMETERS no procedimento do evento e especificar um nome para cada parâmetro. O Visual FoxPro passa os parâmetros do evento MouseWheel na seguinte ordem.
 **nDirection**
Contém um número dependente do dispositivo de mouse que indica a direção em que a roda do mouse é girada. Um valor negativo indica que a roda do mouse é girada para trás; um valor positivo indica que a roda do mouse é girada para frente.
**nShift**
Contém um número que especifica o estado das teclas modificadoras quando a roda do mouse é girada. As teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas modificadoras individuais estão listados na tabela a seguir. Value Key 1 SHIFT 2 CTRL 4 ALT Se mais de uma tecla modificadora for mantida pressionada quando a roda do mouse é girada, o argumento nShift contém a soma dos valores das teclas modificadoras. Por exemplo, se o usuário mantém CTRL pressionado enquanto gira a roda do mouse, o argumento nShift contém 2. Mas se o usuário mantém CTRL+ALT pressionado enquanto gira a roda do mouse, o argumento nShift contém 6.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) atual do ponteiro do mouse dentro do formulário. Essas coordenadas são sempre expressas em termos do sistema de coordenadas do formulário, na unidade de medida especificada na configuração da propriedade ScaleMode.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object
