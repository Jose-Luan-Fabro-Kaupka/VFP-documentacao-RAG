# Comando SET MEMOWIDTH

Especifica a largura exibida de campos memo e expressões de caractere.

```foxpro
SET MEMOWIDTH TO nColumns
```

#### Parâmetros
 **nColumns**
Especifica uma largura entre 8 e 8192 colunas. A largura padrão para saída é 50 colunas. Se você emitir SET COMPATIBLE ON ou SET COMPATIBLE DB4, a largura padrão é alterada para 80 colunas. Se você especificar um valor para nColumns maior que 8192, a largura é definida como 8192.

# Observações

SET MEMOWIDTH especifica a largura da saída enviada para a janela principal do Microsoft Visual FoxPro ou para uma janela definida pelo usuário por comandos como ? | ??, DISPLAY ou LIST. Afeta a largura de saída de campos memo e expressões de caractere com mais de 254 caracteres. Também afeta os valores retornados pelas funções ATCLINE( ), ATLINE( ), MEMLINE( ) e MLINE( ).

Observe que para ? e ?? a largura exibida não excederá 256 caracteres.

Se a saída for direcionada para a janela principal do Visual FoxPro, a largura da saída é determinada pela fonte da janela principal do Visual FoxPro. Se a saída for direcionada para uma janela definida pelo usuário, a largura da saída é determinada pela fonte da janela definida pelo usuário.

SET MEMOWIDTH tem escopo na sessão de dados atual.
