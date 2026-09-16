# Como: suspender a execução do programa

Pontos de interrupção permitem suspender a execução do programa. Uma vez que a execução do programa foi suspensa, você pode verificar os valores de variáveis e propriedades, ver configurações de ambiente e examinar seções de código linha por linha sem precisar percorrer todo o seu código.

> **Dica:** Você também pode suspender a execução de um programa em execução na janela Trace pressionando ESC.

# Suspendendo a execução em uma linha de código

Você pode definir pontos de interrupção em seu código para suspender a execução do programa de várias maneiras diferentes. Se você sabe onde deseja suspender a execução do programa, pode definir um ponto de interrupção diretamente nessa linha de código.

### Para definir um ponto de interrupção em uma linha de código específica
- Na janela Trace Window , localize a linha de código na qual deseja definir o ponto de interrupção.
- Posicione o cursor na linha.
- Execute uma das seguintes ações: Clique duas vezes na área cinza à esquerda da linha de código. Na barra de ferramentas Debugger, clique no botão Toggle Breakpoints. Pressione F9.

Um ponto sólido é exibido na área cinza à esquerda da linha de código para indicar que um ponto de interrupção foi definido nessa linha.

> **Dica:** Se você estiver depurando objetos, pode localizar linhas de código específicas na janela Trace escolhendo o objeto na lista Object e o método ou evento na lista Procedure.

Você também pode definir pontos de interrupção especificando locais e arquivos na caixa de diálogo Breakpoints.
 Exemplos de locais e arquivos para pontos de interrupção
| Local | Arquivo | Onde a execução é suspensa |
| --- | --- | --- |
| ErrHandler | C:\Myapp\Main.prg | A primeira linha executável em um procedimento chamado ErrHandler em Main.prg. |
| Main,10 | C:\Myapp\Main.prg | A décima linha no programa chamado Main . |
| Click | C:\Myapp\Form.scx | A primeira linha executável de qualquer procedimento, função, método ou evento chamado Click em Form.scx. |
| cmdNext.Click | C:\Myapp\Form.scx | A primeira linha executável associada ao evento Click de cmdNext em Form.scx. |
| cmdNext::Click | A primeira linha executável no evento Click de qualquer controle cuja ParentClass é cmdNext em qualquer arquivo. | |

# Suspendendo a execução quando valores mudam

Se você quiser saber quando o valor de uma variável ou propriedade muda, ou quando uma condição de tempo de execução muda, pode definir um ponto de interrupção em uma expressão.

### Para suspender a execução do programa quando o valor de uma expressão mudar
- No menu Tools na janela Debugger Window , escolha Breakpoints para abrir a caixa de diálogo Breakpoints Dialog Box .
- Na lista Type, escolha Break when expression has changed .
- Insira a expressão na caixa Expression.
 Exemplos de expressões de ponto de interrupção
| Expressão | Uso |
| --- | --- |
| RECNO( ) | Suspender a execução quando o ponteiro de registro se move na tabela. |
| PROGRAM( ) | Suspender a execução na primeira linha de qualquer novo programa, procedimento, método ou evento. |
| myform.Text1.Value | Suspender a execução sempre que o valor desta propriedade é alterado interativamente ou programaticamente. |

# Suspendendo a execução condicionalmente

Muitas vezes você desejará suspender a execução do programa, não em uma linha específica, mas quando uma certa condição é verdadeira.

### Para suspender a execução do programa quando uma expressão avalia como verdadeira
- No menu Tools na janela Debugger Window , escolha Breakpoints para abrir a caixa de diálogo Breakpoints Dialog Box .
- Na lista Type, escolha Break when expression is true .
- Insira a expressão na caixa Expression.
- Escolha Add para adicionar o ponto de interrupção à lista Breakpoints.
 Exemplos de expressões de ponto de interrupção
| Expressão | Uso |
| --- | --- |
| EOF( ) | Suspender a execução quando o ponteiro de registro passou do último registro em uma tabela. |
| 'CLICK'$PROGRAM( ) | Suspender a execução na primeira linha de código associada a um evento Click ou DblClick. |
| nReturnValue = 6 | Se o valor de retorno de uma caixa de mensagem é armazenado em nReturnValue , suspender a execução quando um usuário escolhe Yes na caixa de mensagem. |

# Suspendendo a execução condicionalmente em uma linha de código

Você pode especificar que a execução do programa seja suspensa em uma linha específica somente quando uma condição específica é verdadeira.

### Para suspender a execução do programa em uma linha específica quando uma expressão avalia como verdadeira
- No menu Tools na janela Debugger Window , escolha Breakpoints para abrir a caixa de diálogo Breakpoints Dialog Box .
- Na lista Type, escolha Break at location if expression is true .
- Insira o local na caixa Location.
- Insira a expressão na caixa Expression.
- Escolha Add para adicionar o ponto de interrupção à lista Breakpoints.
- Escolha OK . Dica Às vezes é mais fácil localizar a linha de código na janela Trace, definir um ponto de interrupção e depois editar esse ponto de interrupção na caixa de diálogo Breakpoints. Para fazer isso, altere o Type de Break at location para Break at location if expression is true e depois adicione a expressão.

# Removendo pontos de interrupção

Você pode desabilitar pontos de interrupção sem removê-los na caixa de diálogo Breakpoints. Você pode excluir pontos de interrupção "break at location" na janela Trace.

### Para remover um ponto de interrupção de uma linha de código
- Na janela Trace Window , localize o ponto de interrupção e faça uma das seguintes ações: Posicione o cursor na linha de código e, em seguida, escolha Toggle Breakpoints na barra de ferramentas Debugger. -ou- Clique duas vezes na área cinza à esquerda da linha de código.
