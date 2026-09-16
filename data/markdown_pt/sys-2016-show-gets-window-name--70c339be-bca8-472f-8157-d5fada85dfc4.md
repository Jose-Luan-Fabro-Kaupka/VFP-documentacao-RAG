# SYS(2016) - SHOW GETS WINDOW Name

Incluído para compatibilidade com versões anteriores. Use o método Refresh (Visual FoxPro) em vez de SHOW GETS.

Retorna o nome da janela incluído no último comando SHOW GETS WINDOW; retorna um valor apenas em uma rotina READ SHOW.

```foxpro
SYS(2016)
```

# Valor de retorno

Valor de retorno - Character

# Observações

SHOW GETS suporta uma cláusula WINDOW opcional que permite atualizar controles (caixas de seleção, campos, invisíveis, botões push ou de opção, listas, popups, spinners ou regiões de edição de texto) em uma janela específica.

SYS(2016) retorna um asterisco (*) se você emitir SHOW GETS sem uma cláusula WINDOW (atualizando @ ... GETS em todas as janelas). Use SHOW GETS WINDOW "" para atualizar apenas controles na janela principal do FoxPro. SYS(2016) retorna a cadeia de caracteres nula quando você atualiza controles na janela principal do FoxPro.
