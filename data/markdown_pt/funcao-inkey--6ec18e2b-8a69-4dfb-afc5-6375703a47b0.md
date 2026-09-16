# Função INKEY( )

Retorna um número correspondente ao primeiro clique do mouse ou à primeira tecla pressionada no buffer de antecipação.

```foxpro
INKEY([nSeconds] [, cHideCursor])
```

#### Parâmetros
 **nSeconds**
Especifica o número de segundos a aguardar por uma tecla. Se você não especificar um valor para nSeconds, INKEY( ) retorna um valor para uma tecla imediatamente. Se nSeconds for 0, INKEY( ) aguarda indefinidamente por uma tecla.
**cHideCursor**
Mostra ou oculta o cursor, ou verifica um clique do mouse. A tabela a seguir lista os valores para cHideCursor. cHideCursor Descrição S Mostra o cursor. H Oculta o cursor. M Verifica um clique do mouse. E Expande a macro de teclado se uma macro de teclado estiver atribuída a uma tecla ou combinação de teclas. Para retornar valores sucessivos para cada tecla em uma macro, execute INKEY( ) repetidamente com E incluído. Observação Se S e H estiverem incluídos em cHideCursor, o último caractere especificado tem precedência. Você pode combinar valores para cHideCursor; por exemplo, para verificar um clique do mouse e mostrar o cursor, inclua M e S. Para verificar um clique do mouse e ocultar o cursor, inclua H e M. INKEY( ) ignora caracteres diferentes de S, H, M e E em cHideCursor.

# Valor de retorno

Numérico. INKEY( ) retorna 0 se nenhuma tecla foi pressionada. Se várias teclas estiverem presentes no buffer de antecipação, INKEY( ) retorna o valor da primeira tecla inserida no buffer. INKEY( ) também retorna os seguintes valores conforme certas condições:
 - Se M estiver incluído para cHideCursor, INKEY( ) retorna o valor 151.
- Se E estiver incluído, INKEY( ) retorna um valor correspondente à primeira tecla atribuída à macro de teclado. Se você omitir E, INKEY( ) retorna o valor da tecla ou combinação de teclas que aciona a macro de teclado.
- Para teclas individuais e combinações de teclas usando as teclas SHIFT, CTRL e ALT, a tabela a seguir lista os valores de retorno para INKEY( ). Um traço (–) indica que a combinação de teclas não retorna valor. Tecla Sozinha SHIFT CTRL ALT F1 28 84 94 104 F2 –1 85 95 105 F3 –2 86 96 106 F4 –3 87 97 107 F5 –4 88 98 108 F6 –5 89 99 109 F7 –6 90 100 110 F8 –7 91 101 111 F9 –8 92 102 112 F10 –9 93 103 113 F11 133 135 137 139 F12 134 136 138 140 1 49 33 – 120 2 50 64 – 121 3 51 35 – 122 4 52 36 – 123 5 53 37 – 124 6 54 94 – 125 7 55 38 – 126 8 56 42 – 127 9 57 40 – 128 0 48 41 – 19 a 97 65 1 30 b 98 66 2 48 c 99 67 3 46 d 100 68 4 32 e 101 69 5 18 f 102 70 6 33 g 103 71 7 34 h 104 72 127 35 I 105 73 9 23 j 106 74 10 36 k 107 75 11 37 l 108 76 12 38 m 109 77 13 50 n 110 78 14 49 o 111 79 15 24 p 112 80 16 25 q 113 81 17 16 r 114 82 18 19 s 115 83 19 31 t 116 84 20 20 u 117 85 21 22 v 118 86 22 47 w 119 87 23 17 x 120 88 24 45 y 121 89 25 21 z 122 90 26 44 INS 22 22 146 162 HOME 1 55 29 151 DEL 7 7 147 163 END 6 49 23 159 PAGE UP 18 57 31 153 PAGE DOWN 3 51 30 161 UP ARROW 5 56 141 152 DOWN ARROW 24 50 145 160 RIGHT ARROW 4 54 2 157 LEFT ARROW 19 52 26 155 ESC 27 –/27 –*/27 –*/1 ENTER 13 13 10 –/166 BACKSPACE 127 127 127 14 TAB 9 15 148/* * SPACEBAR 32 32 32/– 57 ` or ~ 96 126 41 - or _ 45 95 = or + 61 43 13 [ or { 91 123 27 26 ] or } 93 125 29 27 \ or | 92 124 28 43 ; or : 59 58 39 ' or " 39 34 40 , or < 44 60 51 . or > 46 62 52 / or ? 47 63 53 * Tecla reservada pelo Windows.
