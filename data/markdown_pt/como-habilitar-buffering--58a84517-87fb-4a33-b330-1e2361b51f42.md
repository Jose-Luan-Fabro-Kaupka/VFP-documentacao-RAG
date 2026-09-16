# Como: habilitar buffering

Você pode habilitar buffering de registro e de tabela para proteger dados durante atualizações.

# Habilitando buffering de registro

Habilite o buffering de registro com a função CURSORSETPROP( ).

### Para habilitar bloqueio pessimista de registro na área de trabalho atual
- Use esta função e valor: CURSORSETPROP("Buffering", 2)

O Visual FoxPro tenta bloquear o registro na localização do ponteiro. Se o bloqueio for bem-sucedido, o Visual FoxPro coloca o registro em um buffer e permite a edição. Quando você move o ponteiro de registro ou usa a função TABLEUPDATE( ), o Visual FoxPro grava o registro em buffer na tabela original.

### Para habilitar bloqueio otimista de registro na área de trabalho atual
- Use esta função e valor: CURSORSETPROP("Buffering", 3)

O Visual FoxPro grava o registro na localização do ponteiro em um buffer e permite edições. Quando você move o ponteiro de registro ou usa a função TABLEUPDATE( ), o Visual FoxPro tenta um bloqueio no registro. Se o bloqueio for bem-sucedido, o Visual FoxPro compara o valor atual do registro no disco com o valor original do buffer. Se esses valores são iguais, as edições são gravadas na tabela original; se esses valores são diferentes, o Visual FoxPro gera um erro.

# Habilitando buffering de tabela

Habilite o buffering de tabela com a função CURSORSETPROP( ).

### Para habilitar bloqueio pessimista de vários registros na área de trabalho atual
- Use esta função e valor: CURSORSETPROP("Buffering", 4)

O Visual FoxPro tenta bloquear o registro na localização do ponteiro. Se o bloqueio for bem-sucedido, o Visual FoxPro coloca o registro em um buffer e permite a edição. Use a função TABLEUPDATE( ) para gravar os registros em buffer na tabela original.

### Para habilitar bloqueio otimista de vários registros na área de trabalho atual
- Use esta função e valor: CURSORSETPROP("Buffering", 5)

O Visual FoxPro grava os registros em um buffer e permite edições até que você use a função TABLEUPDATE( ). O Visual FoxPro então executa a seguinte sequência em cada registro no buffer:
 - Tenta um bloqueio em cada registro editado.
- Após um bloqueio bem-sucedido, compara o valor atual de cada registro no disco com o valor original do buffer.
- Grava as edições na tabela original se a comparação mostrar que os valores são iguais.
- Gera um erro se os valores diferirem.

Quando o buffering de tabela está habilitado, o Visual FoxPro tenta atualizações somente depois de usar a função TABLEUPDATE( ).
