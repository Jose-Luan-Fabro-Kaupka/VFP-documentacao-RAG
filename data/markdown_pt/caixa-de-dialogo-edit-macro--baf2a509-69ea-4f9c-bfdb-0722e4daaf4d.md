# Caixa de diálogo Edit Macro

Permite editar manualmente uma macro existente.
 **Defined Key**
Exibe a combinação de teclas que você pressiona para iniciar a macro.
**Macro Name**
Exibe o nome padrão da macro, que é baseado na tecla definida. Por exemplo, se a tecla definida é CTRL+D, o nome da macro será CTRL_D. Se desejar renomear a macro, digite o novo nome (até 20 caracteres) na caixa.
**Macro Contents**
Fornece espaço para digitar as teclas que a macro executa. Use as atribuições de etiqueta de tecla listadas no tópico Comando ON KEY LABEL e coloque-as entre chaves para representar as teclas desejadas. Coloque também todas as combinações de teclas (como CTRL+F2) entre chaves. Por exemplo: MODIFY{SPACEBAR}COMMAND{ENTER} {HOME}{SHIFT+END} Observação As combinações de teclas SHIFT+CTRL+\, CTRL+–, CTRL+^ e SHIFT+CTRL+ENTER não são suportadas no Visual FoxPro.
