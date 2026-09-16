# Comando ASSERT

Exibe uma caixa de mensagem quando uma expressão lógica é avaliada como False (.F.).

Quando a condição estipulada no comando ASSERT é avaliada como False (.F.), uma caixa de mensagem de assert é exibida e ecoada na janela Debug Output no Debugger.

> **Observação:** ASSERT é ignorado em aplicativos que você distribui.

```foxpro
ASSERT lExpression [MESSAGE cMessageText]
```

#### Parâmetros
 **lExpression**
Especifica a expressão lógica a ser avaliada. Se lExpression for avaliada como False (.F.) lógico, uma caixa de diálogo de depuração é exibida. Se lExpression for avaliada como True (.T.) lógico, a caixa de diálogo não é exibida.
**cMessageText**
Especifica o texto a ser exibido na caixa de diálogo de depuração. Se você omitir cMessageText, o texto padrão é exibido e indica o número da linha em que a asserção falhou e o procedimento que contém a asserção.

# Observações

Você pode especificar se as mensagens de assert são exibidas configurando o comando SET ASSERTS. Para obter mais informações, consulte Comando SET ASSERTS.

A caixa de mensagem exibida contém os botões Debug, Cancel, Ignore e Ignore All. A tabela a seguir descreve a ação executada ao escolher cada botão.

| Botão | Descrição |
| --- | --- |
| Debug | Suspende a execução do programa e exibe a janela Debugger com a janela Trace ativa. |
| Cancel | Encerra a execução do programa. |
| Ignore | Continua a execução do programa com a linha seguinte ao comando ASSERT. |
| Ignore All | Continua a execução do programa com a linha seguinte ao comando ASSERT e define SET ASSERTS como OFF. Ignora comandos ASSERT subsequentes até que SET ASSERTS seja definido como ON. |

# Exemplo

Suponha que você crie uma função que espera um valor de parâmetro diferente de zero. A linha de código a seguir na função alerta você se o valor do parâmetro é 0:

```foxpro
ASSERT nParm != 0 MESSAGE "Received a parameter of 0"
```
