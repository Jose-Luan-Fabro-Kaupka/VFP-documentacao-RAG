# Como: gerenciar várias instâncias de um formulário

Você pode ter várias instâncias de uma definição de classe ativas ao mesmo tempo. Por exemplo, você pode projetar um formulário de pedido, mas ter vários pedidos abertos em seu aplicativo. Cada um usa a mesma definição de formulário, mas é exibido e manipulado individualmente.

Quando você tem várias instâncias de um formulário, os pontos-chave a lembrar são:
 - Crie uma propriedade de matriz no formulário de lançamento para armazenar as variáveis de objeto associadas a cada instância do formulário de múltiplas instâncias. A maneira mais fácil de rastrear variáveis de instância quando você não sabe de antemão quantas haverá é usar uma matriz.
- Para o formulário que terá várias instâncias, defina a propriedade DataSession Property como 2 – Private Data Session. Uma sessão de dados privada fornece um conjunto separado de áreas de trabalho para cada instância do formulário, de modo que tabelas selecionadas e posições do ponteiro de registro são todas independentes.

# Exemplo

O exemplo a seguir fornece código que demonstra a criação de várias instâncias de um formulário. Por brevidade, este código não está otimizado; destina-se apenas a apresentar os conceitos.

O formulário a seguir lança várias instâncias:
 Configuração de propriedade para Launch.scx
| Object | Property | Setting |
| --- | --- | --- |
| frmLaunch | aForms[1] | " " |
 Código de evento para Launch.scx
| Object | Event | Code |
| --- | --- | --- |
| cmdQuit | Click | RELEASE THISFORM |
| cmdLaunch | Click | nInstance = ALEN(THISFORM.aForms) DO FORM Multi ; NAME THISFORM.aForms[nInstance] ; LINKED DIMENSION ; THISFORM.aForms[nInstance + 1] |

Ao refinar o código neste exemplo, você poderia gerenciar a matriz de objetos de formulário para que elementos de matriz vazios reutilizados como formulários sejam fechados e novos formulários sejam abertos, em vez de sempre redimensionar a matriz e aumentar o número de elementos em um.

O formulário que pode ter várias instâncias é Multi.scx. O ambiente de dados para este formulário contém a tabela Employee.
 Várias instâncias de Multi.scx
 Configuração de propriedade para Multi.scx
| Object | Property | Setting |
| --- | --- | --- |
| txtFirstname | ControlSource | Employee.first_name |
| txtLastName | ControlSource | Employee.last_name |
| frmMulti | DataSession | 2 - Private Data Session |

Quando você escolhe Launch Form no formulário Launcher, uma instância do formulário Multi é criada. Quando você fecha o formulário Launcher, a matriz de propriedades aForms é liberada e todas as instâncias de Multi são destruídas.

O Visual FoxPro fornece algumas funções e propriedades para ajudar a gerenciar várias instâncias de objetos. Para obter mais informações, consulte AINSTANCE( ) Function, AUSED( ) Function e DataSessionID Property.
