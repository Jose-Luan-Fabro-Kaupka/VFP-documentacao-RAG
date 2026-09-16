# Função WINDOW( )

Determina a janela de saída ativa.

```foxpro
WINDOW()
```

# Valor de retorno

Character.

# Observações

WINDOW( ) retorna o nome da janela para a qual a saída está sendo direcionada.

WINDOW( ) retorna a cadeia vazia se a saída estiver sendo direcionada à janela principal do Visual FoxPro.
Esta função está incluída para compatibilidade com versões anteriores. Você pode usar a função WOUTPUT( ) em seu lugar.

# Exemplo

```foxpro
PUBLIC oForm
oForm = CREATEOBJECT('Form')
oForm.AllowOutput = INT(SECONDS()) % 2 = 0
oForm.Caption = IIF(oForm.AllowOutput, "This form accepts output", ;
"This form does not accept output")
oForm.Show()
? "Default output window name is " + ;
    IIF( EMPTY( WINDOW()), "None", WINDOW())
WAIT WINDOW "The default output window name should appear " + ;
    IIF( EMPTY( WINDOW()), "nowhere", "in the form " + WINDOW())
```
