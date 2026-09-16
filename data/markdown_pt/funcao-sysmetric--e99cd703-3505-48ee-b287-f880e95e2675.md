# Função SYSMETRIC( )

Retorna o tamanho dos elementos de tela do sistema operacional.

```foxpro
SYSMETRIC(nScreenElement)
```

#### Parâmetros
 **nScreenElement**
Especifica um elemento de tela. A tabela a seguir mostra os valores para nScreenElement e o elemento de tela correspondente: nScreenElement Screen Element 1 Screen width 2 Screen height. 3 Width of sizable window frame 4 Height of sizable window frame 5 Width of scroll arrows on vertical scroll bar 6 Height of scroll arrows on vertical scroll bar 7 Width of scroll arrows on horizontal scroll bar 8 Height of scroll arrows on horizontal scroll bar 9 Height of window title 10 Width of non-sizable window frame 11 Height of non-sizable window frame 12 Width of DOUBLE or PANEL window frame 13 Height of DOUBLE or PANEL window frame 14 Scroll box width on horizontal scroll bar in text editing windows 15 Scroll box height on vertical scroll bar in text editing windows 16 Minimized window icon width 17 Minimized window icon height 18 Maximum insertion point width 19 Maximum insertion point height 20 Single-line menu bar height 21 Maximized window width 22 Maximized window height 23 Kanji window height 24 Minimum sizable window width 25 Minimum sizable window height 26 Minimum window width 27 Minimum window height 28 Window controls width 29 Window controls height 30 1 if mouse hardware present; otherwise 0 31 1 for Microsoft Windows debugging version; otherwise 0 32 1 if mouse buttons swapped; otherwise 0 33 Width of a button in a half-caption window's caption or title bar 34 Height of half-caption window caption area

# Valor de retorno

Caractere

# Observações

SYSMETRIC( ) retorna o tamanho dos elementos de tela. Elementos de tela incluem menus, janelas, controles de janela e o ponto de inserção. Os valores são retornados em pixels, salvo indicação contrária, e podem variar para diferentes monitores, drivers de exibição e hardware de vídeo. Para obter mais informações sobre elementos de tela, consulte a função GetSystemMetrics na MSDN Library em http://msdn.microsoft.com/library.

SYSMETRIC( ) permite determinar o tamanho de menus, janelas e controles de janela que você cria no Visual FoxPro. Janelas e menus criados com DEFINE WINDOW e DEFINE MENU usam os mesmos tamanhos de elementos de tela que as janelas e menus do sistema operacional.
