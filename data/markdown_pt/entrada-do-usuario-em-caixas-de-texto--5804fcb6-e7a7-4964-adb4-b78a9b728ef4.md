# Entrada do usuário em caixas de texto

A caixa de texto é um controle básico que permite aos usuários adicionar ou editar dados armazenados em um campo não memo em uma tabela.

A tabela a seguir descreve algumas das tarefas que você pode realizar com caixas de texto definindo as propriedades apropriadas.

| Propriedade | Ação |
| --- | --- |
| Propriedade SelectOnEntry | Seleciona todo o texto quando o usuário entra na caixa de texto usando o teclado. |
| Propriedade InputMask | Determina os valores que podem ser digitados na caixa de texto. |
| Propriedade Format | Determina como os valores são exibidos na caixa de texto. |
| Propriedade Value | Referencia ou altera o texto exibido na caixa de texto em código. |
| Propriedade ControlSource | Armazena o valor exibido na caixa de texto na propriedade Value e na variável ou campo especificado pela propriedade ControlSource. |
| Propriedade AutoComplete | Exibe uma lista dinâmica de valores inseridos anteriormente para escolha. |
| Propriedade AutoCompTable | Especifica a tabela que preenche a lista dinâmica para a caixa de texto. |
| Propriedade AutoCompSource | Especifica um campo na tabela de preenchimento automático para associar à caixa de texto. |

O arquivo Solution.app no diretório ...\Samples\Solution do Visual FoxPro contém exemplos de como usar caixas de texto. Depois de abrir Solution.app, na exibição em árvore, clique em Controls e, em seguida, em Text boxes.

# Valores de data em caixas de texto

Caixas de texto têm várias propriedades que facilitam a entrada de valores de data pelos usuários. A tabela a seguir lista propriedades que você pode definir para controlar como as datas podem ser inseridas em caixas de texto.

| Propriedade | Descrição |
| --- | --- |
| Century | Define se os dois primeiros dígitos do ano são exibidos ou não. |
| DateFormat | Formata a data na caixa de texto em um dos quinze formatos predefinidos, como alemão ou japonês. |
| StrictDateEntry | Define StrictDateEntry como 0 - Loose. Isso permite que o usuário insira datas em formatos mais flexíveis do que o padrão 99/99/99. |

# Validando dados em caixas de texto

Você pode verificar ou validar valores em caixas de texto incluindo código dentro do evento Valid da caixa de texto. Se o valor na caixa de texto for inválido, retorne False (.F.) ou 0 do código que você usa para avaliar o valor da caixa de texto no evento Valid. Se o evento Valid retornar False (.F.), o Visual FoxPro exibe a mensagem "Invalid input".

> **Observação:** O controle não perde o foco se o evento Valid retornar False (.F.) ou 0.

Por exemplo, suponha que você tenha uma caixa de texto em que um usuário pode digitar uma data de compromisso. Você pode verificar se a data já passou incluindo o seguinte código de exemplo no evento Valid da caixa de texto:

```foxpro
IF CTOD(THIS.Value) < DATE()
   = MESSAGEBOX("You need to enter a future date",1)
   RETURN 0
ENDIF
```

Se você quiser exibir sua própria mensagem, inclua o comando WAIT WINDOW ou a função MESSAGEBOX( ) no código do evento Valid e retorne 0. Para obter mais informações, consulte o comando WAIT e a função MESSAGEBOX( ).
