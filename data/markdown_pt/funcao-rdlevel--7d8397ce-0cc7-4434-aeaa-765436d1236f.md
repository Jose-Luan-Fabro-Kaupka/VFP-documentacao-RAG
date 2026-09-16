# Função RDLEVEL( )

Incluída para compatibilidade com versões anteriores. Use o Form Designer em vez de READ.

Retorna o nível READ atual.

```foxpro
RDLEVEL()
```

# Valor de retorno

Valor de retorno - Numérico

# Observações

READs aninhados são criados emitindo @ ... GETS e um READ em uma rotina executada durante um READ ativo. READs podem ser aninhados até cinco níveis.

Use RDLEVEL() para retornar o nível do comando READ atual. RDLEVEL() retorna um valor de 0, 1, 2, 3, 4 ou 5, dependendo de quão profundo o READ atual está aninhado. RDLEVEL() retorna 0 se nenhum READ estiver em execução.

# Exemplo

No exemplo a seguir, pressionar CTRL+Z a qualquer momento exibe o nível READ atual usando RDLEVEL(). Você pode avançar para o próximo nível READ pressionando Enter ou pode voltar um nível READ pressionando Esc. Observe o uso da cláusula VALID com @ ... GET e uma UDF para criar READs aninhados.

```foxpro
ON KEY LABEL CTRL+Z DO saylevel
CLEAR
DO saylevel
@ 4,2 GET level1 VALID(proc1()) DEFAULT 1
READ				&& READ Level 1
ON KEY LABEL CTRL+Z
RETURN
PROCEDURE proc1
@ 6,2 GET level2 VALID(proc2()) DEFAULT 2
READ				&& READ Level 2
RETURN ''
PROCEDURE proc2
@ 8,2 GET level3 VALID(proc3()) DEFAULT 3
READ				&& READ Level 3
RETURN ''
PROCEDURE proc3
@ 10,2 GET level4 DEFAULT 4
READ				&& READ Level 4
RETURN ''
PROCEDURE saylevel
@ 2,2 SAY 'Read level: ' + STR(RDLEVEL())
RETURN ''
```
