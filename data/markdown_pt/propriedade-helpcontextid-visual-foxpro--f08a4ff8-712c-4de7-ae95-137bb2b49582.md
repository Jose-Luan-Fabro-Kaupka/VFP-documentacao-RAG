# Propriedade HelpContextID (Visual FoxPro)

Especifica um ID de contexto para um tópico em um arquivo de Ajuda para fornecer Ajuda sensível ao contexto para o objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.HelpContextID[ = nContextID]
```

# Valor de retorno
 **nContextID**
Especifica o número de ID de contexto de um tópico em um arquivo de Ajuda. O intervalo válido para números de ID de contexto é de 0 a 268.435.455.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | _SCREEN System Variable | Server Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

Para criar Ajuda sensível ao contexto para um objeto em seu aplicativo, você deve atribuir o mesmo número de contexto tanto ao objeto quanto ao tópico de Ajuda associado quando criar o arquivo de Ajuda.

Se você criou Ajuda para seu aplicativo, o Visual FoxPro chama o arquivo de Ajuda e solicita o tópico identificado pelo número de ID de contexto atual. Você pode especificar um arquivo de Ajuda com SET HELP TO e pode especificar uma tecla para ativar o arquivo de Ajuda com ON KEY LABEL. O compilador de Ajuda necessário para criar ajuda no estilo gráfico está incluído com o Visual FoxPro.

O número de ID de contexto atual é a configuração da propriedade HelpContextID para o objeto que tem o foco. Se um número de contexto atual diferente de zero não for encontrado, a tela de conteúdo principal do arquivo de Ajuda é exibida.

Para um objeto servidor, a propriedade HelpContextID especifica o ID de contexto para a biblioteca de tipos criada para o servidor. A propriedade ServerHelpFile especifica o arquivo de Ajuda que contém o tópico de ajuda correspondente ao ID de contexto.
