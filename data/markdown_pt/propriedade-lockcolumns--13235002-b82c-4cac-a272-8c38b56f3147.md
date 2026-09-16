# Propriedade LockColumns

Especifica o número de colunas a bloquear no painel direito de uma grade, começando pela borda esquerda. Leitura/gravação em tempo de design e em tempo de execução.

Depois que LockColumns é definido, a capacidade de mover colunas é desabilitada. As colunas bloqueadas permanecem na grade ou na janela Browse ao navegar para a direita.

```foxpro
Grid.LockColumns [ = nValue ]
```

#### Parâmetros
 **nValue**
Tipo de dados numérico. Especifica um número de colunas a bloquear no painel direito de uma grade. O valor padrão é 0. Se nValue for maior que 0, definir nValue como 0 remove o número atual de colunas bloqueadas.

# Observações

Aplica-se a: Grid Control | BROWSE Command

Uma grade sempre contém dois painéis; no entanto, apenas o painel direito é visível no modo padrão. Você pode ativar o painel esquerdo definindo a propriedade SplitBar como True (.T.) e arrastando a barra de divisão na interface do usuário para expor o painel esquerdo, ou definindo um valor para a propriedade Partition.

Uma linha separadora de coluna, que aparece 1 pixel mais larga que a linha que separa as outras colunas, indica a área onde as colunas bloqueadas terminam e as colunas normais começam.

LockColumns se aplica apenas ao painel direito da grade, que é exibido por padrão. Para bloquear colunas no painel esquerdo da grade, quando exposto pelas propriedades Partition ou SplitBar, use a propriedade LockColumnsLeft.

O método Column SetFocus não funciona se uma coluna estiver bloqueada e não visível na janela da grade, por exemplo, rolada para fora do lado esquerdo.

Quando qualquer uma das colunas bloqueadas rola para fora da janela Grid para a esquerda, elas permanecem fora de vista e não ficam visíveis novamente até que o bloqueio seja removido. Por exemplo, suponha que uma grade contenha cinco colunas e a fonte de dados tenha dez colunas. Quando você rola duas colunas para a direita, a primeira e a segunda colunas rolam para fora da grade para a esquerda.

Suponha que você defina LockColumns com o seguinte código:

```foxpro
Grid.LockColumns = 3
```

A primeira, segunda e terceira colunas agora estão bloqueadas. A terceira coluna aparece como a primeira coluna visível na grade bloqueada, embora a primeira e a segunda colunas ainda existam e permaneçam fora de vista. Você não pode rolar para a esquerda para visualizar todas as colunas bloqueadas. Essa funcionalidade é útil se você deseja bloquear as colunas no meio da grade e não quer exibir as colunas anteriores ou posteriores.

# Exemplo

O exemplo a seguir demonstra como usar LockColumns com BROWSE ... NAME:

```foxpro
CLOSE DATABASES
OPEN DATABASE testdata && Open testdata database in \Samples\Data.
USE Customer
BROWSE NAME Customer
Customer.LockColumns = 2 && Locks first two columns in right pane.
```
