# Como: adicionar código de limpeza a um sistema de menus

Você pode personalizar seu sistema de menus adicionando código de limpeza a ele. O código de limpeza normalmente contém código que habilita ou desabilita inicialmente menus e itens de menu. Quando você gera e executa o programa de menu, o código de configuração e o código de definição de menu são processados antes do código de limpeza.

### Para adicionar código de limpeza a um sistema de menus
- No menu View, escolha General Options .
- Na área Menu Code, selecione Cleanup e, em seguida, escolha OK .
- Na janela de código, digite o código de limpeza apropriado. Suas alterações são salvas quando você fecha o Menu Designer . Dica Se seu menu é o programa principal em um aplicativo, inclua um comando READ EVENTS no código de limpeza e atribua um comando CLEAR ao comando de menu usado para sair do sistema de menus. Isso impede que seus aplicativos de tempo de execução terminem prematuramente.
