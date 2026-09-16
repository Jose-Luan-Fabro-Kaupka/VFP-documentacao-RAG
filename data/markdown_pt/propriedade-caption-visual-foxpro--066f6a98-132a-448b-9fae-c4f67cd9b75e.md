# Propriedade Caption (Visual FoxPro)

Especifica o texto exibido na legenda de um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Caption[ = cText]
```

# Valor de retorno
 **cText**
Especifica o texto exibido com um objeto. O número máximo de caracteres da propriedade Caption é 255. A tabela a seguir descreve como as legendas são exibidas dependendo do objeto. Objeto Exibição da legenda Form A legenda é exibida na barra de título do formulário. Quando o formulário é minimizado, a legenda é exibida à direita do ícone do formulário. PageFrame A legenda é exibida na guia de cada página do quadro de páginas. Controles A legenda é exibida sobre o controle ou ao lado dele. Se o controle exibir um ícone, a configuração da propriedade PicturePosition determinará o posicionamento do ícone e, portanto, o posicionamento da legenda.

# Observações

Aplica-se a: Controle CheckBox | Controle CommandButton | Objeto Form | Objeto Header | Controle Label (Visual FoxPro) | Controle OptionButton | Objeto Page | Variável de sistema _SCREEN | Objeto ToolBar

Quando você cria um novo formulário ou controle, o valor padrão da propriedade Name define o valor padrão da propriedade Caption. Essa legenda padrão inclui o nome da classe do objeto e um inteiro, por exemplo, Command1, Combo1 ou Form1.

Use a propriedade Name para referenciar corretamente um objeto no código. A propriedade Caption descreve apenas o texto que aparece na tela para identificar o controle. Essas duas propriedades começam com o mesmo valor, mas depois são definidas de forma independente.

Se você não especificar uma configuração para a propriedade Width de um controle, o controle será dimensionado automaticamente para conter a legenda.

Para redimensionar automaticamente um controle Label de modo que se ajuste à legenda, defina a propriedade AutoSize como True (.T.).

Para atribuir uma tecla de acesso a um controle, inclua uma barra invertida e um sinal de menor que (\<) na legenda imediatamente antes do caractere que deseja designar como tecla de acesso. O usuário poderá então pressionar ALT e o caractere especificado para mover o foco para esse controle. Se o controle for um botão de comando, caixa de seleção ou botão de opção, pressionar ALT e o caractere especificado também terá o efeito de clicar no controle.

Para adicionar um sublinhado a um caractere na legenda do cabeçalho de uma coluna, anteceda o caractere com um E comercial (&). Se quiser incluir o caractere "&" na legenda do cabeçalho de uma coluna, use dois caracteres & consecutivos. Observe que isso não faz com que a letra se comporte como tecla de acesso; apenas sublinha o caractere da legenda do cabeçalho.

# Exemplo

Este exemplo demonstra o uso da propriedade Caption para alterar a legenda da janela principal do Visual FoxPro de Microsoft Visual FoxPro para o número da versão atual do Visual FoxPro.

```foxpro
_SCREEN.Caption=VERSION()
```
