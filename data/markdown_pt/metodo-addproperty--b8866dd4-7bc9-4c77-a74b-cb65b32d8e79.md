# Método AddProperty

Adiciona uma nova propriedade a um objeto.

```foxpro
Object.AddProperty(cPropertyName [, eNewValue [, nVisibility [, cDescription]]])
```

#### Parâmetros
 **cPropertyName**
Especifica o nome da nova propriedade a ser adicionada ao objeto.
**eNewValue**
Especifica o valor ao qual a nova propriedade é definida. Se eNewValue for omitido, o valor da nova propriedade permanece inalterado se a propriedade já existir ou é definido como False (.F.) para uma nova propriedade.
**nVisibility**
Especifica a visibilidade da nova propriedade. Disponível para uso em tempo de design; no entanto, um valor de 1 pode ser especificado em tempo de execução. nVisibility Visibilidade 1 Public 2 Protected 3 Hidden
**cDescription**
Especifica uma descrição para a nova propriedade. Disponível apenas em tempo de design. A descrição da propriedade é limitada a 255 caracteres.

# Valor de retorno

Logical

# Observações

Aplica-se a: CheckBox Control | Collection Class | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Cursor Object | CursorAdapter Class | Custom Object | DataEnvironment Object | EditBox Control | Exception Class (Visual FoxPro) | Form Object | FormSet Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | ProjectHook Object | Relation Object | ReportListener Object | _SCREEN System Variable | Separator Object | Session Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

O método AddProperty( ) permite adicionar uma propriedade a um objeto em tempo de execução. A nova propriedade é adicionada como uma propriedade PUBLIC.

Você também pode criar matrizes de propriedades para um objeto. Cada elemento na matriz de propriedades é inicializado com eNewValue se estiver incluído; caso contrário, cada elemento da matriz de propriedades contém False (.F.). O código a seguir demonstra como você pode criar uma matriz de propriedades para um objeto:

```foxpro
oMyForm = CREATEOBJECT('Form')
oMyForm.AddProperty('MyArray(2)', 1)  && Add an array as a property
oMyForm.MyArray(2) = 'Two'
CLEAR
? oMyForm.MyArray(1)  && Displays 1
? oMyForm.MyArray(2)  && Displays Two
```

Se uma propriedade com o nome que você especificar não existir, a propriedade é criada e um True (.T.) lógico é retornado.

Se uma propriedade já existir com o nome que você especificar, então AddProperty( ) retorna o seguinte:
 - True (.T.) se a nova propriedade é uma propriedade de matriz e a propriedade existente também é uma propriedade de matriz. O tamanho da matriz é redimensionado para o da nova matriz. Se um valor for especificado com eNewValue , todos os elementos na matriz são definidos com seu valor. Se eNewValue for omitido, todos os elementos da matriz são definidos como False (.F.).
- True (.T.) se a nova propriedade não é uma propriedade de matriz e a propriedade existente é uma propriedade de matriz. A propriedade permanece uma propriedade de matriz. Se um valor for especificado com eNewValue , todos os elementos na matriz são definidos com seu valor. Se eNewValue for omitido, os elementos da matriz permanecem inalterados.
- True (.T.) se a nova propriedade não é uma propriedade de matriz e a propriedade existente não é uma propriedade de matriz ou não é uma propriedade nativa somente leitura do Visual FoxPro. Se um valor for especificado com eNewValue , a propriedade existente é definida com seu valor. Se eNewValue for omitido, o valor da propriedade existente permanece inalterado.
- False (.F.) se a nova propriedade é uma propriedade de matriz e a propriedade existente não é uma propriedade de matriz. A propriedade existente permanece inalterada.
- Um erro "Property < PropertyName > is read-only" é gerado se a propriedade existente é uma propriedade nativa somente leitura do Visual FoxPro, como a propriedade BaseClass.
- Um erro "Incorrect property name" é gerado se o nome da propriedade não é válido (o nome da propriedade contém um espaço ou outros caracteres ilegais).

O método AddProperty( ) funciona apenas com alguns objetos nativos do Visual FoxPro. Você pode usar a função ADDPROPERTY( ) para adicionar uma propriedade a qualquer objeto com o qual o Visual FoxPro trabalha, como objetos COM ou aqueles criados com SCATTER...NAME. Para obter mais informações, consulte ADDPROPERTY( ) Function.
