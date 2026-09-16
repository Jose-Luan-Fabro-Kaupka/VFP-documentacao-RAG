# Como: filtrar a lista de classes do Class Browser

Você pode exibir um conjunto específico de classes especificando um tipo de classe, nome de classe ou um filtro no Class Browser.

### Para filtrar a lista de classes
- No Class Browser, abra a biblioteca de classes desejada. Para obter informações sobre como abrir o Class Browser, consulte Como: executar o Class Browser.
- Na caixa type, selecione uma classe da lista, digite o nome de uma classe ou digite um único filtro ou filtros separados por vírgulas, que atuam como operadores lógicos OR. Observação Uma classe precisa corresponder a apenas um filtro para inclusão na lista de classes. As classes que correspondem à classe, tipo ou filtro que você especificou aparecem na lista de classes. Os filtros que você especifica são adicionados à lista type.

A lista type mantém um histórico dos tipos e filtros que você selecionou somente para a instância atual do Class Browser. A lista não é salva depois que você fecha o Class Browser.

> **Observação:** O modo Hierarchical é selecionado por padrão no menu de atalho do Class Browser. Quando o modo Hierarchical está selecionado, o Visual FoxPro avalia classes pai. Se uma classe pai corresponder ao filtro, suas classes filho são avaliadas. Se a classe pai não corresponder ao filtro, suas classes filho não são avaliadas e não aparecem na lista, mesmo que a filha corresponda ao filtro.

Você pode expandir sua pesquisa de classes para incluir uma cadeia de caracteres específica no nome ou descrição.

### Para pesquisar por nome de classe e texto de descrição
- No Class Browser, abra a biblioteca de classes desejada.
- No Class Browser, clique no botão Find.
- Na caixa Look for da caixa de diálogo Find Class, digite uma cadeia de caracteres que deseja pesquisar.
- Clique em Find.

Classes que contêm a cadeia de caracteres em seu nome ou descrição aparecem na lista de classes.

> **Observação:** Quando o modo Hierarchical está selecionado, apenas as classes pai correspondentes e suas subclasses associadas correspondentes aparecem na lista.

A tabela a seguir de operadores e expressões de filtro descreve caracteres curinga que você pode combinar com os caracteres em um nome de classe para criar um filtro no Class Browser.

| O filtro contém | Descrição |
| --- | --- |
| + cTargetName | O nome deve começar com cTargetName. |
| % cTargetName % | O nome contém cTargetName. Por exemplo, para visualizar todas as classes que contêm a cadeia de caracteres "mover", digite %MOVER%. |
| - cTarget | O nome NÃO contém cTarget. Tem precedência sobre outros filtros de pesquisa. |
| ~ cTarget | O nome contém algo semelhante a cTarget. |
| cTarget * Um asterisco (*) substitui um número ilimitado de caracteres. | O nome contém qualquer coisa após cTarget. Por exemplo, para visualizar todas as classes que começam com "VCR", digite VCR*. |
| " cTarget " | O nome é cTarget. Se cTarget não for uma classe básica, reporta resultados da pesquisa por nome de classe. |
| cTarget | Se cTarget for uma classe básica, reporta todos os membros da classe básica independentemente do nome. |
| [ ? ...] cTarget [ ? ...] | O nome contém cTarget mais os caracteres desconhecidos especificados nas posições relativas especificadas. O ponto de interrogação (?) substitui um único caractere. Você pode usar pontos de interrogação em qualquer posição e em qualquer quantidade. Por exemplo, para visualizar todas as classes que começam com MsgBox e algum número, como MsgBox1, digite MsgBox?. |

A tabela a seguir descreve exemplos que ilustram combinações de expressões de filtro separadas por espaços, que representam o operador OR.

| Se você quiser isto | Use uma expressão como esta |
| --- | --- |
| O alvo é uma cadeia de caracteres que deve começar com "test" mas NÃO é uma classe "form". | -%form% +test* |
| O alvo é qualquer cadeia de caracteres que NÃO contém "debug" e começa com "c" OU contém "test". | c* %test% -%debug% |
| O alvo é qualquer cadeia de caracteres que NÃO começa com "debug" e é semelhante a "test" OU é a cadeia de caracteres "myform" | ~test -debug* "myForm" |
