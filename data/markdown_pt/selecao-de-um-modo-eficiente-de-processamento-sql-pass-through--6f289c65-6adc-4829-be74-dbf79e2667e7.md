# Seleção de um modo eficiente de processamento SQL Pass-Through

O Visual FoxPro fornece dois modos de processamento para recuperar e atualizar dados remotos usando SQL pass-through: síncrono e assíncrono. Quando você usa funções SQL pass-through, pode escolher o método que preferir. Você não precisa escolher um método para views remotas; o Visual FoxPro emprega automaticamente busca progressiva e gerencia o modo de processamento para você em views remotas.

# Benefícios do modo síncrono

Por padrão, as funções SQL do Visual FoxPro são processadas de forma síncrona: o Visual FoxPro não retorna o controle a uma aplicação até que uma chamada de função seja concluída. O processamento síncrono é útil quando você está trabalhando com o Visual FoxPro de forma interativa.

# Benefícios do modo assíncrono

O processamento assíncrono oferece maior flexibilidade que o processamento síncrono. Por exemplo, quando sua aplicação está processando uma função de forma assíncrona, sua aplicação pode construir um indicador de progresso para exibir o progresso da instrução em execução, exibir o movimento do ponteiro do mouse, criar loops e definir temporizadores para permitir a interrupção de processamento que está demorando muito.
