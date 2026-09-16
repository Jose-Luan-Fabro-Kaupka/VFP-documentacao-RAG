# Comando SET READBORDER

Determina se bordas são colocadas ao redor de caixas de texto criadas com @ ... GET.

```foxpro
SET READBORDER ON | OFF
```

#### Parâmetros
 **ON**
Coloca uma borda de linha única ao redor de todas as caixas de texto criadas com @ ... GET. Se SET READBORDER estiver definido como ON quando a primeira caixa de texto é criada, todas as caixas de texto subsequentes criadas no mesmo nível READ também terão bordas.
**OFF**
(Padrão) Especifica que uma borda não é colocada ao redor de caixas de texto criadas com @ ... GET. Se SET READBORDER estiver definido como OFF quando a primeira caixa de texto é criada, todas as caixas de texto subsequentes criadas no mesmo nível READ não terão bordas.

# Observações

SET READBORDER especifica se bordas de linha única são colocadas ao redor de caixas de texto criadas com @ ... GET.

# Exemplo

No exemplo a seguir, as três primeiras caixas de texto criadas com @ ... GET têm bordas. A terceira caixa de texto tem borda, mesmo que SET READBORDER tenha sido definido como OFF antes de ser criada. A quarta caixa de texto não tem borda, pois READBORDER foi definido como OFF e ela está abrangida em um READ diferente das três primeiras caixas de texto.

```foxpro
SET READBORDER ON
@ 2,2 GET gnW DEFAULT 1   && 1st READ
@ 4,2 GET gnX DEFAULT 1   && 1st READ
SET READBORDER OFF
@ 6,2 GET gnY DEFAULT 1   && 1st READ
READ
@ 8,2 GET gnZ DEFAULT 2   && 2nd READ
READ
```
