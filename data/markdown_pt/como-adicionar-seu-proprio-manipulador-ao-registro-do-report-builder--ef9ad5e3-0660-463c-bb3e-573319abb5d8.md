# Como: adicionar seu próprio manipulador ao registro do Report Builder

O Report Builder usa uma tabela de consulta interna que mapeia tipos de eventos no Report ou Label Designer para classes de manipuladores de eventos específicas. Como essa tabela está incorporada em reportbuilder.app, é somente leitura e não pode ser modificada.

Por padrão, o Report Builder usará uma tabela externa com o nome de arquivo reportbuilder.dbf em preferência à sua tabela de manipuladores interna, se ela atender a um dos seguintes requisitos:
 - Está no SET PATH do Visual FoxPro
- Está na mesma pasta que reportbuilder.app.

O Report Builder tem um mecanismo para criar uma cópia externa da tabela de consulta, disponível na sua caixa de diálogo Options.

Depois que o arquivo existir no disco, você pode fazer alterações na tabela, navegando por ela no diretório do Visual FoxPro ou usando o Report Builder's Handler Registry Table Explorer.

Neste tópico, você aprenderá como:
 - Copiar a tabela de consulta de eventos somente leitura para que você possa fazer alterações.
- Explorar a tabela de consulta de eventos do Report Builder.
- Adicionar e configurar sua própria classe de manipulador de eventos na tabela de consulta.

Consulte Report Builder Event Handler Registry Table para obter mais informações sobre a tabela de consulta.

# Criando uma cópia editável da tabela de consulta interna

### Para copiar a tabela de consulta interna para o disco usando a caixa de diálogo de opções
- Abra a caixa de diálogo Report Builder Options. Para obter mais informações, consulte How to: Display the Report Builder Options Dialog Box.
- Clique em Create copy… para abrir a caixa de diálogo Save as.
- Altere o nome e o local do arquivo, se desejar, e clique em Save para criar a cópia.
- Clique em Close para fechar a caixa de diálogo Options.

O local padrão na caixa de diálogo Save as será o diretório em que reportbuilder.app está localizado, e o nome de arquivo padrão será reportbuilder.dbf. Esta é a tabela que o Report Builder usará em preferência à sua tabela interna.

> **Dica:** Depois de criar e editar sua tabela de consulta de eventos, você pode adicioná-la aos seus aplicativos e dar a ela um nome diferente. Para especificar esta tabela para uso do Report Builder em seus aplicativos, você invoca reportbuilder.app em um modo de configuração especial enquanto realiza tarefas de configuração para seu aplicativo. Para obter mais informações, consulte How to: Specify an Alternate Report Event Handler Table.

### Para copiar a tabela de consulta interna para o disco usando parâmetros de linha de comando
- Abra a janela Command.
- Digite um dos seguintes comandos: DO (HOME() + "reportbuilder.app") WITH 5, cFilename * OU: DO (_REPORTBUILDER) WITH 5

O parâmetro cFilename deve ser uma especificação de arquivo totalmente qualificada de um arquivo de tabela (.dbf). Se o arquivo existir, ele será substituído. Se você omitir o parâmetro cFilename, a caixa de diálogo Save As será exibida.

# Navegando na tabela Event Handler Registry

### Para explorar a tabela de consulta usando o navegador Event Handler Registry do Builder
- Abra a caixa de diálogo Report Builder Options. Para obter mais informações, consulte How to: Display the Report Builder Options Dialog Box.
- Clique em Explore registry… para abrir a caixa de diálogo Event Handler Registry.

Para obter mais informações sobre como ajustar o conteúdo da tabela de consulta, consulte Event Handler Registry Dialog Box (Report Builder).

# Adicionando uma classe de manipulador personalizada à tabela Event Handler Registry

Neste exemplo, você criará uma classe que trata o evento que ocorre quando você pressiona CTRL-E em um controle de etiqueta de relatório.

### Para criar um manipulador de edição de etiqueta CTRL-E
- Crie ou edite uma biblioteca de classes programática: MODIFY COMMAND c:\temp\mylibrary.prg
- Crie sua classe de manipulador digitando o seguinte código e salve suas alterações:

```foxpro
DEFINE CLASS MyLabelEditor AS Custom
    PROCEDURE Execute( oEvent )
        LOCAL cCaption
        cCaption = INPUTBOX("Label caption:",;
                        "Label Properties", TRIM(frx.expr))
        IF NOT EMPTY( m.cCaption )
            REPLACE frx.expr WITH m.cCaption
            oEvent.SetHandledByBuilder(.T.)
            oEvent.SetReloadChanges(.T.)
        ENDIF
    ENDPROC
ENDDEFINE
```

### Para registrar seu manipulador para o evento de builder Ctrl-E
- Abra a caixa de diálogo Report Builder Options. Para obter mais informações, consulte How to: Display the Report Builder Options Dialog Box.
- Se a caixa de texto Current registry table contém "Internal lookup table," siga as etapas acima para copiar a tabela de consulta de eventos somente leitura para que você possa fazer alterações.
- Clique em Explore registry… para abrir a caixa de diálogo Event Handler Registry.
- Localize um registro com Type="H", Event=14, ObjType=5, ObjCode=0.
- Se tal registro não existir na tabela, adicione um novo registro à tabela clicando em Add Record.
- Defina os valores dos campos conforme mostrado na tabela abaixo.
- Clique em Close para fechar a caixa de diálogo Event Handler Registry.
- Clique em Close para fechar a caixa de diálogo Report Builder Options.

| Type | H |
| --- | --- |
| Class | MyLabelEditor |
| Library | c:\temp\mylibrary.prg |
| Description | Sample Ctrl-E on Label handler |
| Event | 14 |
| ObjType | 5 |
| ObjCode | 0 |
| Native | False |
| Debug | False |

### Para testar suas alterações no registro de manipulador de eventos
- Abra um layout de relatório ou etiqueta no designer.
- Selecione um controle de etiqueta
- Pressione CTRL-E. Você deve ver uma caixa de diálogo INPUTBOX() enquanto sua classe é invocada para tratar o evento.
