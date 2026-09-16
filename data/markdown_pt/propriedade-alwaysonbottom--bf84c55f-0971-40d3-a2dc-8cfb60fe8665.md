# Propriedade AlwaysOnBottom

Impede que outras janelas cubram a janela de um formulário. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.AlwaysOnBottom[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade AlwaysOnBottom são: Configuração Descrição True (.T.) O formulário está sempre na parte inferior (somente outra janela com a propriedade AlwaysOnBottom definida como True (.T.) pode ficar abaixo do formulário). False (.F.) (Padrão) O formulário pode cobrir outra janela.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

A propriedade AlwaysOnBottom é ignorada se qualquer uma das seguintes propriedades estiver definida com os valores especificados:
 - AlwaysOnTop = .T.
- Desktop = .T.
- ShowWindow = 2

A configuração da propriedade AlwaysOnBottom é ignorada para _SCREEN.
