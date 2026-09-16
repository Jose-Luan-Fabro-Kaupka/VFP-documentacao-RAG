# SYS(2800) - Suporte à acessibilidade

Desabilita ou habilita o suporte ao Microsoft Active Accessibility e define certas opções para rastrear o foco do teclado do controle atualmente selecionado em um formulário do Visual FoxPro.

```foxpro
SYS(2800 [,nFlag] )
```

#### Parâmetros
 **nFlag**
Desabilita o suporte à acessibilidade ou habilita várias funcionalidades de acessibilidade conforme a tabela a seguir. Observação Os sinalizadores são aditivos. nFlags Descrição 0 Desabilita o Active Accessibility (AA). 1 Habilita WM_GETOBJECT. 2 Habilita NotifyWinEvent. 4 Faz com que o Visual FoxPro não retorne aos clientes de Acessibilidade até que uma ação especificada seja concluída. Substitui as mensagens de certos métodos de IAccessible, como accDoDefaultAction ou accSelect, para processar a solicitação do cliente e retornar ao cliente imediatamente. 16 Habilita ACCNAME. Retorna Name do objeto em vez de Caption. Use para testes. 32 Somente para compatibilidade com versões anteriores. O padrão para nFlag é 3, que é a soma de "Habilita WM_GETOBJECT" (2) + "Habilita NotifyWinEvent" (3). Para detalhes sobre WM_GETOBJECT, NotifyWinEvent e accDoDefaultAction, consulte o tópico Accessibility na seção User Interface Services do Platform SDK na MSDN Online Library.

# Valor de retorno

Character

# Observações

SYS(2800) retorna um valor numérico como uma cadeia de caracteres para a configuração atual do Active Accessibility.

Esta função permite verificar a funcionalidade de auxílios de acessibilidade, como o Microsoft Magnifier, quando você está desenvolvendo um aplicativo para atender aos requisitos do Windows Logo.

Esta função é eficaz somente para controles nativos do Visual FoxPro. Controles ActiveX de terceiros podem ou não rastrear corretamente o foco do teclado com os auxílios de acessibilidade habilitados. Entre em contato com o fornecedor do controle para obter informações sobre o comportamento de acessibilidade de um controle específico.
