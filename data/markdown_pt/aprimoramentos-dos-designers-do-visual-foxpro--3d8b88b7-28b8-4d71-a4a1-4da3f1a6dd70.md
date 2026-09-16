# Aprimoramentos dos designers do Visual FoxPro

Você pode querer abrir os designers a seguir e encontrar os aprimoramentos.

# Report and Label Designers

Você pode usar o Report Builder disponível no Report Designer e no Label Designer para executar tarefas de relatório, configurar opções e definir propriedades para recursos de relatório, como layout de relatório, faixas de relatório, grupos de dados, controles de relatório e variáveis de relatório. Por exemplo, você pode executar as seguintes tarefas:
 - Impedir que usuários modifiquem relatórios, controles de relatório e faixas de relatório ao editar o relatório no modo protegido.
- Exibir legendas em vez de expressões para controles Field em tempo de design.
- Exibir ToolTips definidos pelo usuário para controles de relatório.
- Definir o script de linguagem para relatórios.
- Salvar o ambiente de dados do relatório como uma classe.

Por padrão, o Report Builder é ativado quando você interage com os designers Report e Label. No entanto, você pode usar a variável de sistema _REPORTBUILDER para especificar ReportBuilder.app. O Report Builder consolida, substitui e adiciona à funcionalidade encontrada nos elementos de interface do usuário anteriores do Report Designer, que permanecem no produto e estão disponíveis definindo _REPORTBUILDER. Você pode escrever report builders personalizados para ampliar a funcionalidade e a saída de relatórios ou executar relatórios com objetos de relatório. Para obter mais informações, consulte Working with Reports e a variável de sistema _REPORTBUILDER.

# Menu Designer

Você pode definir a variável de sistema _MENUDESIGNER para chamar seu próprio designer personalizado para criar menus.

```foxpro
_MENUDESIGNER = cProgramName
```

Para obter mais informações, consulte a variável de sistema _MENUDESIGNER.

# Table Designer

O Table Designer acomoda os seguintes aprimoramentos de dados:
 - Novos tipos de dados: Varchar, Varbinary e Blob
- Índices binários
- Para obter mais informações, consulte Data and XML Feature Enhancements .

# Query and View Designers

Você pode usar espaços em nomes de tabelas especificados em instruções SQL nos designers Query e View se fornecer um alias. Por exemplo, editar a seguinte instrução é válido nos designers View e Query:

```foxpro
SELECT * from dbo."Order Details" Order_Details
```

Para obter mais informações, consulte o comando SELECT - SQL.

# Data Environment Designer

O caminho completo para o banco de dados (DBC) aparece na barra de status quando você seleciona um banco de dados na caixa de diálogo Add Table or View.

# Class and Form Designers

O nome da classe que você está modificando aparece na barra de título das seguintes caixas de diálogo:
 - Edit Property/Method Dialog Box
- New Property Dialog Box
- New Method Dialog Box
- Class Info Dialog Box

O menu View do Form Designer oferece ambas as opções para especificar a ordem de tabulação em formulários: Assign Interactively ou Assign by List.

Nos designers Class, Form e Report, você pode usar os seguintes comandos de atalho de teclado para ajustar o espaçamento entre itens selecionados.

| Shortcut | Description |
| --- | --- |
| ALT+Arrow Key | Ajusta o espaçamento entre os objetos selecionados em um pixel na direção da tecla de seta. |
| ALT+CTRL+Arrow Key | Ajusta o espaçamento entre os objetos selecionados em uma unidade de grade na direção da tecla de seta. |

Para obter mais informações, consulte Interactive Development Environment (IDE) Enhancements.
