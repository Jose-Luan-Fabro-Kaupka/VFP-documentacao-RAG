# Usar o Navegador de objetos

O Navegador de objetos permite navegar, filtrar e pesquisar componentes que você pode querer consumir em seus projetos.

Para abrir o Navegador de objetos no menu Ferramentas, clique em Navegador de objetos.

Você também pode abrir o Navegador de objetos clicando no botão Navegador de objetos na barra de ferramentas principal do Visual FoxPro ou digitando a seguinte linha de código na janela Comando:

```foxpro
DO (_OBJECTBROWSER)
```

> **Observação:** Depois que o Navegador de objetos é aberto, você pode abri-lo programaticamente usando a variável de sistema _OBJECTBROWSER.

Você pode visualizar qualquer biblioteca de tipos de classe COM registrada no seu sistema. O painel esquerdo mostra uma lista de todas as bibliotecas de tipos de classe carregadas. Você pode expandir cada categoria para exibir as classes na biblioteca. Os membros associados a essas classes aparecem no painel direito.

# Trabalhar com classes

As classes fornecem informações completas de membros para um componente COM ou controle ActiveX específico que você pode querer consumir em sua aplicação. Instâncias desses objetos normalmente são criadas usando uma das seguintes funções do Visual FoxPro:

Função CREATEOBJECT( ), Função CREATEOBJECTEX( ), Função NEWOBJECT( ), Função GETOBJECT( ), Método AddObject

> **Observação:** Controles ActiveX geralmente são colocados diretamente em uma classe de formulário e são instanciados com o formulário.

Você pode explorar uma classe para visualizar detalhes dos membros selecionando a classe no nó Classes no painel Classes e membros. Quando selecionada, as propriedades, métodos e eventos dessa classe são exibidos no painel Membros à direita. Membros protegidos são mostrados com um ícone de cadeado.

Quando você clica em membros de classe no painel Membros, informações detalhadas são mostradas no painel Descrição. O conteúdo do painel Descrição fornece detalhes dos tipos de dados para parâmetros de membros e valores de retorno. Itens sublinhados no painel Descrição são links nos quais você pode clicar para ir diretamente a esse item para obter mais informações. Se disponível, uma descrição funcional do membro também será exibida no painel Descrição.

# Trabalhar com propriedades, métodos e eventos

A melhor maneira de visualizar propriedades, métodos e eventos é usar uma classe específica no painel Membros. Normalmente você trabalha com uma única classe por vez. Às vezes você pode querer visualizar todas as propriedades, métodos e eventos em uma biblioteca de uma vez, sem filtrar por classe. Para fazer isso, clique no nó apropriado no painel Classes e membros. Dependendo do tamanho da biblioteca de tipos, pode levar vários segundos ou minutos para listar todos os membros.

Quando você clica em uma propriedade, método ou evento no painel Classes e membros, você pode visualizar todas as classes e interfaces que a utilizam no painel Membros.

# Trabalhar com classes em cache

Quando você expande um dos nós Propriedades, Métodos ou Eventos no painel Classes e métodos, pode levar algum tempo para exibir todo o conteúdo. Por isso, o Navegador de objetos armazena essas informações em cache no Objectbrowser.dbf. Isso economiza tempo quando você quer recarregar uma biblioteca posteriormente. Você pode clicar no botão Atualizar para que propriedades, métodos ou eventos sejam recarregados na próxima vez que um desses nós for expandido.

# Trabalhar com constantes e enums

Muitas bibliotecas de tipos contêm constantes. Uma constante é o equivalente a um #DEFINE numérico com o qual os desenvolvedores Visual FoxPro estão familiarizados. Enums são coleções de duas ou mais constantes.

Enums são especiais porque um membro pode denotar um enum específico como o tipo de dados de um parâmetro ou valor de retorno. Para um parâmetro, isso significa que o valor passado para um parâmetro deve ser uma das Constantes associadas ao Enum especificado.

Você pode visualizar o valor de uma constante clicando nela e visualizando o valor numérico no painel Descrição.

Ao especificar uma constante para um parâmetro de método, você deve passar o valor numérico real. O Visual FoxPro não reconhece o nome real da constante como referência, como em outras linguagens, como o Visual Basic.

Você pode criar um conjunto de diretivas #DEFINE que representam todas as constantes usando arrastar e soltar do nó Constantes de uma biblioteca de tipos para uma janela do editor.

# Trabalhar com interfaces

Desenvolvedores avançados podem querer trabalhar com interfaces específicas na biblioteca COM. Interfaces são particularmente úteis quando você cria servidores COM no Visual FoxPro que usam a cláusula IMPLEMENTS do comando DEFINE CLASS. A cláusula IMPLEMENTS aceita um nome de interface como parâmetro e pode ser usada em associação com uma variedade de serviços COM+, bem como a Função EVENTHANDLER( ).

Você pode criar um modelo de classe usando arrastar e soltar de um nó Interface para uma janela do editor. Este modelo conterá qualquer instrução IMPLEMENTS e detalhes dos membros da interface.

# Pesquisar em bibliotecas

Você pode realizar pesquisas de texto em uma biblioteca clicando no botão Localizar. O botão Localizar exibe uma visualização Localizar exclusiva acima dos dois painéis principais. A visualização Localizar simples pesquisa uma cadeia especificada em todas as bibliotecas abertas. A pesquisa é feita em todos os elementos de uma biblioteca e para cadeias "contidas em". A visualização Localizar avançada oferece maior refinamento da pesquisa.

# Persistência dos dados do Navegador de objetos

A sessão do Navegador de objetos é persistida entre usos. As informações do Navegador de objetos são salvas em uma tabela objectbrowser.dbf armazenada no mesmo local do Navegador de objetos. Essas informações incluem o seguinte:
 - Uma lista de Histórico recente de todas as bibliotecas abertas anteriormente para que você possa recuperar uma dessas bibliotecas rapidamente no futuro.
- Propriedades, métodos e eventos em cache de uma biblioteca para que ela possa ser carregada rapidamente na próxima vez que for acessada.
- Todos os add-ins carregados anteriormente.
- Preferências do usuário especificadas na caixa de diálogo Opções.
- Componentes COM e controles ActiveX exibidos na caixa de diálogo Abrir (armazenados em Foxrefs.dbf).

# Trabalhar com add-ins
 - Add-ins do Navegador de objetos podem executar uma variedade de funções úteis que não são nativas do navegador. Isso inclui adicionar elementos de interface do usuário adicionais, novos itens de menu e capacidades de arrastar e soltar. Add-ins normalmente são criados como classes VCX.

# Assistente de instalação de add-ins existentes

A primeira etapa do assistente Add-ins existentes especifica as seguintes opções:
 - Insira um nome amigável para o add-in conforme deseja que apareça na lista Add-ins da caixa de diálogo Opções.
- Insira uma descrição para o add-in conforme deseja que apareça na lista Add-ins da caixa de diálogo Opções.
- Selecione um ícone para exibir na lista Add-ins da caixa de diálogo Opções (opcional).

A segunda etapa especifica a entrada para informações de classe do add-in.
 - Selecione a classe específica e a biblioteca de classes para a classe do add-in.

A terceira etapa é uma etapa opcional para fornecer informações de suporte:
 - Você pode especificar uma URL para uma página Web que fornece informações adicionais para usar o add-in. Você também pode fornecer HTML específico que aparece na descrição do add-in.

A última etapa permite concluir a instalação do add-in.
 - Você pode especificar algumas opções avançadas. Isso inclui Propriedades e Configurações definidas pelo usuário.
