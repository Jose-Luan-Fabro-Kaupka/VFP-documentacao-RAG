# Propriedade WhatsThisHelpID

Especifica o ID de contexto correspondente a um tópico de Ajuda What's This ou a um tópico de Ajuda HTML para um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.WhatsThisHelpID[ = nContextID]
```

# Valor de retorno
 **nContextID**
Especifica o número do ID de contexto do tópico correspondente em um arquivo de Ajuda. A tabela a seguir lista os valores de nContextID e a ação executada ao clicar no botão What's This Help na barra de título. nContextID Descrição Negativo Exibe a janela pop-up What's This Help com o texto "No Help topic is associated with this item" ou a página principal de Ajuda de um arquivo de Ajuda HTML, se disponível. (Padrão, –1) Zero Pesquisa a hierarquia de objetos pelo primeiro objeto com um valor positivo de WhatsThisHelpID. Se encontrado, o Visual FoxPro exibe o tópico What's This Help ou tópico de Ajuda HTML correspondente, se disponível. Se não encontrado, o Visual FoxPro não exibe um tópico What's This Help nem um tópico de Ajuda HTML. Positivo Exibe o tópico What's This Help ou tópico de Ajuda HTML correspondente ao nContextID especificado. Se nenhum tópico de Ajuda corresponder ao nContextID especificado, o Visual FoxPro exibe a janela pop-up What's This Help com o texto "No Help topic is associated with this item" ou a página principal de Ajuda de um arquivo de Ajuda HTML, se disponível.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Objeto Header | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Controle Timer | Objeto ToolBar
