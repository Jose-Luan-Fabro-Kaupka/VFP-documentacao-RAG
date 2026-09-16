# Controles para permitir ações específicas

Freqüentemente, você deseja possibilitar que os usuários executem ações específicas que não têm nada a ver com a manipulação de valores. Por exemplo, você pode possibilitar que um usuário feche um formulário, abra outro formulário, percorra uma tabela, salve ou cancele edições, execute um relatório ou consulta, vá para o endereço de um destino na Internet ou intranet, ou qualquer outra ação.

# Using Botões de comando and Grupos de botões de comando

Um dos locais mais comuns para colocar o código para ações específicas é o evento Click do botão de comando a.

# Fazendo do botão de comando a a escolha padrão

Defina a propriedade Default como verdadeira (.T.) para tornar o botão de comando the a escolha padrão. A opção padrão tem uma borda mais grossa que os botões de comando other. Se o botão de comando a for a escolha padrão, quando o usuário pressionar ENTER, o evento Click do botão de comando the será executado.

> **Nota:** Se o objeto selected em um formulário for uma caixa de edição ou grade, o código associado ao evento Click da escolha padrão não será executado quando o usuário pressionar ENTER. Pressionar ENTER em uma caixa de edição adiciona um retorno de carro e avanço de linha ao valor na caixa de edição. Pressionar ENTER em uma grade seleciona um campo adjacente. Para executar o evento Click do botão padrão, pressione CTRL+ENTER.

# Common Propriedades do botão de comando

As propriedades do botão de comando following são normalmente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Cancel | Especifica que o código associado ao evento Click do botão de comando the é executado quando um usuário pressiona ESC. |
| Caption | Texto exibido no botão. |
| DisabledPicture | O arquivo .bmp exibido quando o botão está desabilitado. |
| DownPicture | O arquivo .bmp exibido quando o botão é pressionado. |
| Enabled | Se o botão pode ser escolhido. |
| Picture | O arquivo .bmp exibido no botão. |

Você também pode include botões de comando em um grupo para poder manipulá-los individualmente ou como um grupo.

# Managing Opções de botão de comando no nível do grupo

Se você quiser trabalhar com um procedimento de método single para todo o código dos botões de comando do evento Click of em um grupo, você pode anexar o código ao evento Click do controle CommandGroup. A propriedade Value do grupo de botões de comando the indica qual dos botões foi clicado, conforme demonstrado no exemplo de código a seguir:

```foxpro
DO CASE
   CASE THIS.Value = 1
      WAIT WINDOW "You clicked " + THIS.cmdCommand1.Caption NOWAIT
      * do some action
   CASE THIS.Value = 2
      WAIT WINDOW "You clicked " + THIS.cmdCommand2.Caption NOWAIT
      * do some other action
   CASE THIS.Value = 3
      WAIT WINDOW "You clicked " + THIS.cmdCommand3.Caption NOWAIT
      * do a third action
ENDCASE
```

> **Observação:** Se o usuário clicar no grupo de botões de comando the, mas não em um botão específico, a propriedade Value ainda refletirá o botão de comando last que foi selecionado. Se você escreveu o código para o evento Click de um botão específico no grupo, esse código será executado em vez do código do evento do grupo Click quando o usuário escolher esse botão.

# Common Propriedades do grupo de botões de comando

As propriedades do grupo de botões de comando following são normalmente definidas em tempo de design.| Propriedade | Descrição |
| --- | --- |
| ButtonCount | Número de botões de comando of no grupo. |
| BackStyle | Se o grupo de botões de comando the tem um fundo transparente ou opaco. O fundo transparente A parece ter a mesma cor do objeto underlying, geralmente o formulário ou uma página. |

# Using the Hyperlink Objeto

Você pode usar o objeto Hyperlink para ir para o endereço de um destino na Internet ou intranet. O objeto Hyperlink pode ser usado para iniciar um aplicativo com reconhecimento de hiperlink, normalmente um navegador da Internet, como o Microsoft Internet Explorer, e abrir a página especificada no endereço. O método Hyperlink NavigateTo( ) permite que você especifique o endereço do destino para o qual deseja saltar.

Por exemplo, para navegar até o site da Microsoft na World Wide Web a partir de um formulário, primeiro adicione o controle Hyperlink ao formulário. Adicione o botão de comando a ao formulário e, em seguida, adicione o seguinte código ao evento Click para o botão de comando the:

```foxpro
THISFORM.Hyperlink1.NavigateTo('www.microsoft.com')
```

Quando o formulário for executado, você pode clicar no botão de comando the para acessar o site da Microsoft.
