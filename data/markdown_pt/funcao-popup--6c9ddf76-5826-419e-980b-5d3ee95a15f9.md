# Função POPUP( )

Retorna como cadeia de caracteres o nome do menu ativo, ou um valor lógico indicando se um menu foi definido.

```foxpro
POPUP([cMenuName])
```

#### Parâmetros
 **cMenuName**
Retorna um valor lógico indicando se cMenuName foi definido. POPUP( ) retorna verdadeiro (.T.) se o menu que você especificar foi definido; caso contrário, POPUP( ) retorna falso (.F.).

# Valor de retorno

Caractere ou Lógico

# Observações

POPUP( ) retorna o nome do menu ativo como uma cadeia de caracteres se você omitir o argumento opcional cMenuName. Um menu deve estar definido e ativo para POPUP( ) retornar seu nome. Menus são criados e ativados com DEFINE POPUP e ACTIVATE POPUP. O menu também pode ser um menu do sistema Visual FoxPro. POPUP( ) retorna uma cadeia de caracteres vazia se um menu não estiver definido e ativo ou se você emitir POPUP( ) na janela Command.
