# Método Refresh (Visual FoxPro)

Repinta um formulário ou controle e atualiza quaisquer valores, ou atualiza a exibição visual de um projeto. Há duas versões da sintaxe.

```foxpro
[Form.]Object.Refresh
```

```foxpro
Project.Refresh([lUpdateSCCStatus])
```

#### Parâmetros
 **lUpdateSCCStatus**
Tipo de dados lógico. O parâmetro lUpdateSCCStatus especifica, para um projeto, se o status do controle de código-fonte de cada arquivo sob controle de código-fonte é atualizado. O Visual FoxPro ignora lUpdateSCCStatus se nenhum arquivo do projeto estiver sob controle de código-fonte. A tabela a seguir lista os valores de lUpdateSCCStatus. lUpdateSCCStatus Descrição True (.T.) Atualiza o status do controle de código-fonte de cada arquivo do projeto sob controle de código-fonte. False (.F.) ou omitido Não atualiza o status do controle de código-fonte.

# Observações

Aplica-se a: Controle CheckBox | Objeto Column | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Objeto FormSet | Controle Grid | Objeto Header | Controle Label (Visual FoxPro) | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Objeto Project (Visual FoxPro) | Variável de sistema _SCREEN | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

Em geral, o Visual FoxPro gerencia automaticamente a pintura de um formulário ou controle enquanto nenhum evento está ocorrendo. Você pode usar o método Refresh quando quiser atualizar imediatamente o formulário ou controle, forçar a repintura completa de um formulário ou controle ou atualizar o valor de um controle.

Você também pode usar o método Refresh quando quiser exibir um formulário enquanto outro formulário está sendo carregado ou quando quiser atualizar o conteúdo de um controle. Para atualizar o conteúdo de uma caixa de combinação ou caixa de listagem, use o método Requery.

> **Observação:** Quando um formulário é atualizado, todos os controles do formulário também são atualizados. Quando um quadro de páginas é atualizado, somente a página ativa é atualizada.

Quando você chama o método Refresh para um controle Label, o Visual FoxPro atualiza a propriedade Caption e redesenha o rótulo.

Quando você chama o método Refresh para um controle Shape, o Visual FoxPro redesenha a forma.

Quando você chama o método Refresh para projetos, o Visual FoxPro atualiza a exibição visual de um projeto com quaisquer alterações feitas nele. Por exemplo, depois de adicionar arquivos programaticamente ao projeto com o método Add, você pode chamar o método Refresh para exibir no projeto os arquivos recém-adicionados.

O método Refresh do Grid atualiza visualmente o indicador de registro da grade, mesmo que a grade não tenha o foco.
