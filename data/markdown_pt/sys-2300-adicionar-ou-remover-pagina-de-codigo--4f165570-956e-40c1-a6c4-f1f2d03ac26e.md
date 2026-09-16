# SYS(2300) - Adicionar ou remover página de código

Adiciona ou remove uma página de código da lista NLS (National Language Support).

```foxpro
SYS(2300, nCodePage [, nAction])
```

#### Parâmetros
 **nCodePage**
Especifica o valor inteiro da página de código.
**nAction**
Especifica a ação a executar na página de código especificada. 0 remove a página de código; 1 adiciona a página de código.

# Valor de retorno

Character. SYS(2300) retorna 1 se nCodePage aparece na lista NLS; caso contrário, retorna 0.

# Observações

Quando uma página de código é incluída na lista das suportadas pelo Visual FoxPro, rotinas NLS são empregadas para indexação adequada, comparações de cadeias de caracteres, chaveamento de ordenação e assim por diante. Com certas sequências de ordenação (por exemplo, russo, tcheco ou húngaro), comparações de cadeias de caracteres podem resultar em valores inesperados, dependendo de qual página de código está definida. Para garantir que essas operações procedam corretamente, você pode usar SYS(2300) em seus aplicativos para determinar se a página de código correta está definida.

Se você criar índices após usar SYS(2300) para habilitar suporte NLS para uma página de código específica, obterá comportamento estranho em versões anteriores do Visual FoxPro que não têm suporte NLS para essa página de código. Certifique-se de que todo acesso a dados do Visual FoxPro seja feito de clientes com SYS(2300) configurado de forma semelhante.

A lista NLS inclui 874, 932, 936, 949, 950, 1255 e 1256. Para obter mais informações, consulte Páginas de código suportadas pelo Visual FoxPro.

# Exemplo

A página de código 1250 não está incluída na lista NLS por padrão. Portanto, certas comparações de cadeias de caracteres podem retornar valores inesperados. Para demonstrar isso, siga estas etapas:
 - Habilite o suporte de página de código para a página de código não-NLS 1250 adicionando a linha a seguir ao seu arquivo config.fpw: CODEPAGE = 1250
- Reinicie o Visual FoxPro.
- Execute o código a seguir de um arquivo de programa: SET COLLATE TO 'HUNGARY' && Requires CODEPAGE = 1250 in config file CLEAR ? UPPER("B")=LOWER("B"), LOWER("B")=UPPER("B") ? UPPER("F")=LOWER("F"), LOWER("F")=UPPER("F") ? UPPER("H")=LOWER("H"), LOWER("H")=UPPER("H") =SYS(2300,1250,1) && Add code page 1250 to NLS list ? UPPER("B")=LOWER("B"), LOWER("B")=UPPER("B") ? UPPER("F")=LOWER("F"), LOWER("F")=UPPER("F") ? UPPER("H")=LOWER("H"), LOWER("H")=UPPER("H") =SYS(2300,1250,0) && Restore default setting for code page 1250 RETURN

Com as configurações padrão, LOWER("B")=UPPER("B"), LOWER("F")=UPPER("F") e LOWER("H")=UPPER("H") retornam .T..

Depois de habilitar o suporte NLS para a página de código 1250, LOWER("B")=UPPER("B"), LOWER("F")=UPPER("F") e LOWER("H")=UPPER("H") retornam .F..
