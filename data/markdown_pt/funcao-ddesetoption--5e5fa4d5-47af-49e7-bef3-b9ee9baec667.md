# Função DDESetOption( )

Altera ou retorna configurações de troca dinâmica de dados (DDE).

```foxpro
DDESetOption(cOption [, nTimeoutValue | lExpression])
```

#### Parâmetros
 **cOption**
Especifica as opções de configuração. cOption Setting Default Description TIMEOUT nTimeoutValue (número de milissegundos) 2000 O número de milissegundos que as funções DDE aguardam o aplicativo servidor responder; o valor TIMEOUT atual é retornado se você omitir nTimeoutValue . SAFETY lExpression (true (.T.) ou false (.F.)) .T. Especifica se uma caixa de diálogo é exibida quando você usa DDEInitiate( ) para estabelecer um canal para um aplicativo servidor e o aplicativo não responde; a configuração SAFETY atual é retornada se você omitir lExpression .
**nTimeoutValue**
Especifica o valor de timeout.
**lExpression**
Habilita ou desabilita a exibição da caixa de diálogo.

# Valor de retorno

Lógico ou Numérico

# Observações

Use DDESetOption( ) para alterar ou retornar configurações DDE. Duas opções, TIMEOUT e SAFETY, estão disponíveis.
