# Criação de botões de navegação em tabelas

Um recurso comum em muitos aplicativos é uma série de botões de navegação que permite aos usuários percorrer uma tabela. Normalmente, eles incluem botões para mover o ponteiro de registro para o registro seguinte ou anterior da tabela, bem como para o primeiro ou o último registro da tabela.

# Design dos botões de navegação

Cada botão terá algumas características e funcionalidades em comum; portanto, é recomendável criar uma classe de botão de navegação. Assim, os botões individuais podem derivar facilmente essa aparência e funcionalidade comuns. Essa classe pai é a classe `Navbutton` definida mais adiante nesta seção.

Depois que a classe pai for definida, as subclasses a seguir definirão a funcionalidade e a aparência específicas de cada um dos quatro botões de navegação: `navTop, navPrior, navNext, navBottom.`

Por fim, uma classe de contêiner, `vcr`, é criada, e cada um dos botões de navegação é adicionado à classe de contêiner. O contêiner pode ser adicionado a um formulário ou a uma barra de ferramentas para fornecer funcionalidade de navegação em tabelas.

# Definição da classe NAVBUTTON

Para criar `Navbutton`, salve as seis definições de classe a seguir (`Navbutton`, `navTop`, `navBottom`, `navPrior`, `navNext` e `vcr`) em um arquivo de programa como Navclass.prg.
 Definição da classe CommandButton genérica de navegação
| Código | Comentários |
| --- | --- |
| DEFINE CLASS Navbutton AS COMMANDBUTTON Height = 25 Width = 25 TableAlias = "" | Define a classe pai dos botões de navegação. Fornece algumas dimensões à classe. Inclui uma propriedade personalizada, TableAlias, para armazenar o nome do alias pelo qual navegar. |
| PROCEDURE Click IF NOT EMPTY(This.TableAlias) SELECT (This.TableAlias) ENDIF ENDPROC | Se TableAlias tiver sido definido, este procedimento da classe pai selecionará o alias antes da execução do código de navegação propriamente dito nas subclasses. Caso contrário, pressupõe que o usuário deseja navegar pela tabela na área de trabalho selecionada no momento. |
| PROCEDURE RefreshForm _SCREEN.ActiveForm.Refresh ENDPROC | O uso de _SCREEN.ActiveForm.Refresh em vez de THISFORM.Refresh permite adicionar a classe a um formulário ou a uma barra de ferramentas, com funcionamento igualmente adequado. |
| ENDDEFINE | Encerra a definição da classe. |

Todos os botões de navegação específicos se baseiam na classe `Navbutton`. O código a seguir define o botão Superior do conjunto de botões de navegação. Os outros três botões de navegação são definidos na tabela a seguir. As quatro definições de classe são semelhantes; portanto, somente a primeira possui comentários detalhados.
 Definição da classe do botão de navegação Superior
| Código | Comentários |
| --- | --- |
| DEFINE CLASS navTop AS Navbutton Caption = "|<" | Define a classe do botão de navegação Superior e configura a propriedade Caption. |
| PROCEDURE Click | Cria o código do método a ser executado quando ocorre o evento Click do controle. |
| DODEFAULT( ) GO TOP THIS.RefreshForm | Chama o código do evento Click na classe pai, Navbutton, para que o alias apropriado possa ser selecionado caso a propriedade TableAlias tenha sido definida. Inclui o código que define o ponteiro de registro para o primeiro registro da tabela: GO TOP. Chama o método RefreshForm da classe pai. Não é necessário usar o operador de resolução de escopo (::) neste caso, pois não há um método na subclasse com o mesmo nome que o método da classe pai. Por outro lado, tanto a classe pai quanto a subclasse possuem código de método para o evento Click. |
| ENDPROC | Encerra o procedimento Click. |
| ENDDEFINE | Encerra a definição da classe. |

Os outros botões de navegação possuem definições de classe semelhantes.
 Definição das outras classes de botões de navegação
| Código | Comentários |
| --- | --- |
| DEFINE CLASS navNext AS Navbutton Caption = ">" | Define a classe do botão de navegação Seguinte e configura a propriedade Caption. |
| PROCEDURE Click DODEFAULT( ) SKIP 1 IF EOF( ) GO BOTTOM ENDIF THIS.RefreshForm ENDPROC ENDDEFINE | Inclui o código que define o ponteiro de registro para o registro seguinte da tabela. Encerra a definição da classe. |
| DEFINE CLASS navPrior AS Navbutton Caption = "<" | Define a classe do botão de navegação Anterior e configura a propriedade Caption. |
| PROCEDURE Click DODEFAULT( ) SKIP –1 IF BOF( ) GO TOP ENDIF THIS.RefreshForm ENDPROC ENDDEFINE | Inclui o código que define o ponteiro de registro para o registro anterior da tabela. Encerra a definição da classe. |
| DEFINE CLASS navBottom AS Navbutton Caption = ">|" | Define a classe do botão de navegação Inferior e configura a propriedade Caption. |
| PROCEDURE Click DODEFAULT( ) GO BOTTOM THIS.RefreshForm ENDPROC ENDDEFINE | Inclui o código que define o ponteiro de registro para o último registro da tabela. Encerra a definição da classe. |

A definição de classe a seguir contém os quatro botões de navegação para que possam ser adicionados como uma unidade a um formulário. A classe também inclui um método para definir a propriedade TableAlias dos botões.
 Definição de uma classe de controle de navegação em tabelas
| Código | Comentários |
| --- | --- |
| DEFINE CLASS vcr AS CONTAINER Height = 25 Width = 100 Left = 3 Top = 3 | Inicia a definição da classe. A propriedade Height é definida com a mesma altura dos botões de comando que ela conterá. |
| ADD OBJECT cmdTop AS navTop ; WITH Left = 0 ADD OBJECT cmdPrior AS navPrior ; WITH Left = 25 ADD OBJECT cmdNext AS navNext ; WITH Left = 50 ADD OBJECT cmdBot AS navBottom ; WITH Left = 75 | Adiciona os botões de navegação. |
| PROCEDURE SetTable(cTableAlias) IF TYPE("cTableAlias") = 'C' THIS.cmdTop.TableAlias = ; cTableAlias THIS.cmdPrior.TableAlias = ; cTableAlias THIS.cmdNext.TableAlias = ; cTableAlias THIS.cmdBot.TableAlias = ; cTableAlias ENDIF ENDPROC | Este método é usado para definir a propriedade TableAlias dos botões. TableAlias é definida na classe pai Navbutton. Você também pode usar o método SetAll para definir essa propriedade: IF TYPE ("cTableAlias") = 'C' This.SetAll("TableAlias", "cTableAlias")ENDIF. No entanto, isso causaria um erro se um objeto sem a propriedade TableAlias fosse adicionado à classe. |
| ENDDEFINE | Encerra a definição da classe. |

Depois de definir a classe, você pode criar uma subclasse dela ou adicioná-la a um formulário.

# Criação de uma subclasse baseada na nova classe

Você também pode criar subclasses baseadas em `vcr` que tenham botões adicionais, como Pesquisar, Editar, Salvar e Sair. Por exemplo, `vcr2` inclui um botão Sair:
 Definição de uma subclasse de controle de navegação em tabelas
| Código | Comentários |
| --- | --- |
| DEFINE CLASS vcr2 AS vcr ADD OBJECT cmdQuit AS COMMANDBUTTON WITH ; Caption = "Quit",; Height = 25, ; Width = 50 Width = THIS.Width + THIS.cmdQuit.Width cmdQuit.Left = THIS.Width - ; THIS.cmdQuit.Width | Define uma classe baseada em vcr e adiciona um botão de comando a ela. |
| PROCEDURE cmdQuit.CLICK RELEASE THISFORM ENDPROC | Quando o usuário clica em cmdQuit, este código libera o formulário. |
| ENDDEFINE | Encerra a definição da classe. |

`Vcr2` possui tudo o que `vcr` possui, além do novo botão de comando, sem que seja necessário reescrever nenhum código existente.

# Alterações em VCR refletidas na subclasse

Devido à herança, as alterações na classe pai são refletidas em todas as subclasses baseadas nela. Por exemplo, você pode informar ao usuário que o final da tabela foi alcançado alterando a instrução `IF EOF( )` em `navNext.Click` para o seguinte:

```foxpro
IF EOF()
   GO BOTTOM
   SET MESSAGE TO "Bottom of the table"
ELSE
   SET MESSAGE TO
ENDIF
```

Você pode informar ao usuário que o início da tabela foi alcançado alterando a instrução `IF BOF( )` em `navPrior.Click` para o seguinte:

```foxpro
IF BOF()
   GO TOP
   SET MESSAGE TO "Top of the table"
ELSE
   SET MESSAGE TO
ENDIF
```

Se essas alterações forem feitas nas classes `navNext` e `navPrior`, elas também serão aplicadas automaticamente aos botões apropriados em `vcr` e `vcr2.`

# Adição de VCR a uma classe Form

Depois que `vcr` for definido como um controle, o controle poderá ser adicionado à definição de um contêiner. Por exemplo, o código a seguir adicionado a Navclass.prg define um formulário com botões de navegação:

```foxpro
DEFINE CLASS NavForm AS Form
   ADD OBJECT oVCR AS vcr
ENDDEFINE
```

# Execução do formulário que contém VCR

Depois que a subclasse do formulário for definida, você poderá exibi-la carregando a definição da classe, criando um objeto baseado na subclasse e chamando o método Show do formulário:

```foxpro
SET PROCEDURE TO navclass ADDITIVE
frmTest = CREATEOBJECT("navform")
frmTest.Show
```

Se você não chamar o método SetTable de `oVCR (`o objeto VCR em `NavForm)` quando o usuário clicar nos botões de navegação, o ponteiro de registro se moverá na tabela da área de trabalho selecionada no momento. Você pode chamar o método SetTable para especificar a tabela a percorrer.

```foxpro
frmTest.oVCR.SetTable("customer")
```

> **Observação:** Quando o usuário fecha o formulário, frmTest é definido como um valor nulo (.NULL.). Para liberar da memória a variável de objeto, use o comando RELEASE. As variáveis de objeto criadas em arquivos de programa são liberadas da memória quando o programa é concluído.
