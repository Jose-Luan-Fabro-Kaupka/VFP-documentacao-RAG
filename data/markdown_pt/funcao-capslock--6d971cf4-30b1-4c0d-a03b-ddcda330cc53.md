# Função CAPSLOCK( )

Retorna o modo atual da tecla CAPS LOCK ou define o modo da tecla CAPS LOCK como ligado ou desligado.

```foxpro
CAPSLOCK([lExpression])
```

#### Parâmetros
 **lExpression**
Inclua para ligar ou desligar a tecla CAPS LOCK. CAPSLOCK(.T.) liga o CAPS LOCK e CAPSLOCK(.F.) desliga o CAPS LOCK. Um valor lógico correspondente à configuração do CAPS LOCK antes de CAPSLOCK(.T.) ou CAPSLOCK(.F.) ser emitido é retornado.

# Valor de retorno

Lógico

# Observações

Emitir CAPSLOCK( ) sem argumento retorna verdadeiro (.T.) se o CAPS LOCK estiver ligado, ou falso (.F.) se o CAPS LOCK estiver desligado.

# Exemplo

O código a seguir armazena o estado de CAPSLOCK( ) em uma variável de sistema. O comando = executa a função CAPSLOCK( ) para ligar o CAPS LOCK. Depois o comando = executa a função CAPSLOCK( ) para definir o CAPS LOCK para seu estado anterior.

```foxpro
glOldLock = CAPSLOCK()     && Save original setting
CAPSLOCK(.T.)     && Turn CAPS LOCK on
*** Perform any number of statements ***
CAPSLOCK(glOldLock)  && Return to original setting
*** or, toggle CapsLock to the opposite value and back ***
CAPSLOCK(!CAPSLOCK())
WAIT WINDOW
CAPSLOCK(!CAPSLOCK())
WAIT WINDOW
CAPSLOCK(glOldLock)  && Return to original setting
```
