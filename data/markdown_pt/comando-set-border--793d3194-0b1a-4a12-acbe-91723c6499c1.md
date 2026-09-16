# Comando SET BORDER

Incluído para compatibilidade com versões anteriores. Use a propriedade BorderStyle em vez disso.

Define uma borda para popups criados com DEFINE POPUP e para janelas criadas com DEFINE WINDOW.

```foxpro
SET BORDER TO [SINGLE | DOUBLE
	| PANEL | NONE
	| border string1
	[, border string2]]
```

#### Parâmetros
 border string1 [, border string2]

 Use as cadeias de definição de borda border string1 e border string2 para criar suas próprias bordas. border string1 é usada para menus, popups e caixas e para a janela de saída atual. border string2 especifica a borda que aparece quando a saída não está sendo direcionada para a janela. border string2 não afeta caixas ou popups.

 Uma cadeia de definição de borda é um conjunto de valores de caracteres ASCII definidos [1] [, [2] [, [3] [, [4] [, [5] [, [6] [, [7] [, [8]]]]]]]]. As entradas 1 a 8 da cadeia de borda designam o topo, a base, o lado esquerdo, o lado direito, o canto superior esquerdo, o canto superior direito, o canto inferior esquerdo e o canto inferior direito da borda, respectivamente. Se você incluir apenas um valor ASCII na definição da cadeia de borda, toda a borda é desenhada usando esse único caractere.

 Se uma definição de cadeia de borda for alterada após um popup ou janela ter sido definido, a cadeia de borda original é mantida. Para usar a nova cadeia de borda, você deve recriar o popup ou a janela.

# Observações

Use SET BORDER para especificar as bordas de caixas, popups e janelas. Caixas são criadas com @ ... TO, popups são criados com DEFINE POPUP e janelas são criadas com DEFINE WINDOW. SET BORDER não afeta caixas criadas com @ ... BOX.

SET BORDER fornece compatibilidade com popups no estilo FoxBASE+. Quando você inicia o FoxPro, a borda padrão para popups no estilo FoxBASE+ é uma linha dupla. Todos os outros objetos (janelas, popups criados com DEFINE POPUP e assim por diante) usam por padrão uma borda de linha simples. Se você emitir SET BORDER TO SINGLE ou SET BORDER TO DOUBLE, todos os objetos, incluindo popups no estilo FoxBASE+, são desenhados com borda de linha simples ou dupla, respectivamente.

No FoxPro for Windows e FoxPro for Macintosh, a opção DOUBLE cria uma borda PANEL para popups e janelas, e a opção border string é ignorada.

Se você emitir SET BORDER TO sem argumentos adicionais, as bordas padrão são restauradas.

SINGLE

 Incluir SINGLE cria uma borda de linha simples. Esta é a configuração padrão.

DOUBLE

 Incluir DOUBLE cria uma borda de linha dupla.

PANEL

 Incluir PANEL cria uma borda larga.

NONE

 Incluir NONE suprime a borda inteiramente.
