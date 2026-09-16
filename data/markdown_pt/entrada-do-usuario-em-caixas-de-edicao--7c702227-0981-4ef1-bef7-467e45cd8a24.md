# Entrada do usuário em caixas de edição

Você pode permitir que os usuários editem texto de campos de caracteres longos ou campos memo em caixas de edição. As caixas de edição permitem quebra automática de palavras e a capacidade de mover-se pelo texto usando as teclas de seta, page up e page down e barras de rolagem.

Para ver exemplos de uso de caixas de edição, execute Solution.app no diretório Visual FoxPro ...\Samples\Solution. Na exibição em árvore, clique em Controls e depois em Edit boxes.

# Permitir que usuários editem um campo memo em uma caixa de edição

Tudo o que você precisa fazer para permitir que um usuário edite um campo memo em uma caixa de edição é definir a propriedade ControlSource Property da caixa de edição para o campo memo. Por exemplo, se você tem um campo memo chamado `comments` em uma tabela chamada `log`, pode definir a propriedade ControlSource de uma caixa de edição como `log.comments` para permitir que um usuário edite o campo memo na caixa de edição.

# Permitir que usuários editem um arquivo de texto em uma caixa de edição

Você também pode permitir que um usuário edite um arquivo de texto em uma caixa de edição. O formulário a seguir demonstra isso.
 Formulário de exemplo para editar um arquivo de texto em uma caixa de edição

Um botão OK no formulário fecha o formulário com o seguinte comando no código do evento Click:

```foxpro
RELEASE THISFORM
```

Os outros dois botões neste exemplo, `cmdOpenFile` e `cmdSave`, permitem que um usuário abra um arquivo de texto e salve o arquivo após as edições.
 Código associado ao evento Click de cmdOpenFile
| Código | Comentários |
| --- | --- |
| CREATE CURSOR textfile ; (filename c(35), mem m) APPEND BLANK | Cria um cursor com um campo de caracteres para armazenar o nome do arquivo de texto e um campo memo para armazenar o conteúdo do arquivo de texto. Adiciona um registro em branco ao cursor. |
| REPLACE textfile.FileName WITH ; GETFILE("TXT") | Usa a função GETFILE( ) para retornar o nome do arquivo a abrir. Armazena o nome no campo FileName do cursor. |
| IF EMPTY(textfile.FileName) RETURN ENDIF | Se o usuário escolher Cancel na caixa de diálogo Get File, o campo FileName ficará vazio e não haverá arquivo para abrir. |
| APPEND MEMO mem FROM ; (textfile.FileName) OVERWRITE | Preenche o campo memo com o texto no arquivo. |
| THISFORM.edtText.ControlSource = ; "textfile.mem" THISFORM.Refresh | Define o ControlSource da caixa de edição no formulário. |
| THISFORM.cmdSave.Enabled = .T. | Habilita o botão Save. |

Quando o arquivo foi aberto e editado, o botão Save permite que um usuário grave as alterações de volta no arquivo.
 Código associado ao evento Click de cmdSave
| Código | Comentários |
| --- | --- |
| COPY MEMO textfile.mem TO ; (textfile.filename) | Substitui o valor antigo no arquivo pelo texto no campo memo. |

# Manipular texto selecionado em uma caixa de edição

Caixas de edição e caixas de texto têm três propriedades que permitem trabalhar com texto selecionado: SelLength, SelStart e SelText.

Você pode selecionar texto programaticamente usando as propriedades SelStart Property e SelLength Property. Por exemplo, as linhas de código a seguir selecionam a primeira palavra em uma caixa de edição.

```foxpro
Form1.edtText.SelStart = 0
Form1.edtText.SelLength = AT(" ", Form1.edtText.Text) - 1
```

> **Dica:** Quando você altera a propriedade SelStart, a caixa de edição rola para exibir o novo SelStart. Se você alterar o SelStart em um loop, por exemplo ao pesquisar texto, seu código será executado mais rapidamente se incluir THISFORM.LockScreen = .T. antes do processamento e THISFORM.LockScreen = .F. após o processamento.

Você pode acessar texto selecionado em uma caixa de edição ou caixa de texto com a propriedade SelText Property. Por exemplo, a linha de código a seguir torna o texto selecionado todo em maiúsculas:

```foxpro
Form1.edtText.SelText = UPPER(Form1.edtText.SelText)
```

# Propriedades comuns de caixa de edição

As propriedades de caixa de edição a seguir são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| AllowTabs | Se o usuário pode inserir tabulações na caixa de edição em vez de mover para o próximo controle. Se você permitir tabulações, certifique-se de indicar que os usuários podem mover para o próximo controle pressionando CTRL+TAB. |
| HideSelection | Se o texto selecionado na caixa de edição está visivelmente selecionado quando a caixa de edição não tem o foco. |
| ReadOnly | Se o usuário pode alterar o texto na caixa de edição. |
| ScrollBars | Se há barras de rolagem verticais. |
