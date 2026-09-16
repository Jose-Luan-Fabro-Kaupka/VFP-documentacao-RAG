# Propriedade LockColumnsLeft

Especifica o número de colunas a bloquear no painel esquerdo de uma grade, começando na borda esquerda. Leitura/gravação em tempo de design e em tempo de execução.

As colunas bloqueadas permanecem na grade ou na janela Browse ao pressionar Tab para a direita. LockColumnsLeft se aplica apenas ao painel esquerdo da grade, que não é exibido por padrão. Depois que LockColumns é definido, a capacidade de mover colunas é desabilitada.

```foxpro
Grid.LockColumnsLeft [ = nValue ]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. Especifica um número de colunas a bloquear no painel esquerdo de uma grade. O valor padrão é 0. Se nValue for maior que 0, definir nValue como 0 remove o número atual de colunas bloqueadas.

# Observações

Aplica-se a: Controle Grid | Comando BROWSE

Uma linha separadora de colunas, que aparece 1 pixel mais larga que a linha que separa as outras colunas, indica a área onde as colunas bloqueadas terminam e as colunas normais começam.

Para bloquear colunas no painel direito da grade, use a propriedade LockColumns.

# Exemplo

O exemplo a seguir demonstra como usar LockColumnsLeft com BROWSE ... NAME:

```foxpro
CLOSE DATABASES
&& Open testdata database in \Samples\Data.
OPEN DATABASE testdata
USE Customer
BROWSE NAME Customer
&& Locks first two columns in left pane.
Customer.LockColumnsLeft = 2
```
