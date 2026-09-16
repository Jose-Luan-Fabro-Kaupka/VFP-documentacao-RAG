# Função DDETerminate( )

Fecha um canal de troca dinâmica de dados (DDE) estabelecido com DDEInitiate( ).

```foxpro
DDETerminate(nChannelNumber | cServiceName)
```

#### Parâmetros
 **nChannelNumber**
Especifica o número do canal a fechar.
**cServiceName**
Especifica o nome do serviço a fechar.

# Valor de retorno

Logical

# Observações

Se o canal for fechado com sucesso, DDETerminate( ) retorna true (.T.). Se o canal não puder ser fechado, DDETerminate( ) retorna false (.F.).

Certifique-se de fechar os canais assim que não forem mais necessários para conservar recursos do sistema.

Todos os canais são fechados automaticamente se você sair do Visual FoxPro escolhendo Sair no menu Arquivo ou emitindo QUIT na Janela de Comando ou de dentro de um programa.
