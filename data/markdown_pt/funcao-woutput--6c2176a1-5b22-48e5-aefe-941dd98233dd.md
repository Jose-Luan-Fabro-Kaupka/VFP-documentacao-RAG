# Função WOUTPUT( )

Determina se a saída está sendo direcionada para a janela ativa ou especificada.

```foxpro
WOUTPUT([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica a janela que WOUTPUT( ) avalia para saída. A saída não pode ser direcionada para uma janela do sistema ou barra de ferramentas. Se você omitir WindowName , WOUTPUT( ) retorna o nome da janela para a qual a saída está sendo direcionada no momento. Você também pode incluir a cadeia de caracteres vazia em WindowName para especificar a janela principal do Visual FoxPro. WOUTPUT( ) retorna a cadeia de caracteres vazia se a saída estiver sendo direcionada para a janela principal do Visual FoxPro.

# Valor de retorno

Lógico e Caractere

# Observações

WOUTPUT( ) retorna verdadeiro (.T.) se a janela definida pelo usuário especificada é a janela de saída ativa. WOUTPUT( ) retorna falso (.F.) se a janela que você especificar não existir ou for uma janela do sistema. A última janela definida pelo usuário ativada com ACTIVATE WINDOW é a janela de saída ativa.

# Exemplo

No exemplo a seguir, uma janela é criada e ativada. WOUTPUT( ) é usado para exibir o nome dessa janela de saída ativa. A janela é fechada e removida da memória. Se outra janela estiver ativa, seu nome é exibido. Se outra janela não estiver ativa, uma mensagem é exibida indicando que a saída está sendo direcionada para a janela principal do Visual FoxPro.

```foxpro
DEFINE WINDOW wOutput1 FROM 2,2 TO 12,32 TITLE 'Output Window'
ACTIVATE WINDOW wOutput1
WAIT WINDOW 'wOutput1 window: ' + WOUTPUT()
RELEASE WINDOW wOutput1
IF EMPTY(WOUTPUT())
   WAIT WINDOW 'Output being directed to the main Visual FoxPro window'
ELSE
   WAIT WINDOW 'Output window: ' + WOUTPUT()
ENDIF
```
