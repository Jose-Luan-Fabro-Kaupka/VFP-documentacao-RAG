# Função UPDATED( )

Incluída para compatibilidade com versões anteriores. Use o evento InteractiveChange ou ProgrammaticChange em seu lugar.

Retorna true (.T.) se você alterou algum dado durante o READ mais recente.

```foxpro
UPDATED()
```

# Valor de retorno

Valor de retorno - Logical

# Observações

UPDATED() retorna true se os dados de um campo, controle spinner ou região de edição de texto tiverem sido alterados, ou se tiver sido feita uma escolha em uma caixa de seleção; em um botão invisível, de ação ou de opção; em uma lista; ou em um menu popup.

UPDATED() retorna false (.F.) se os dados não tiverem sido alterados nem tiver sido feita uma escolha nesses controles durante o READ mais recente. UPDATED() retorna false se um controle tiver sido atualizado dentro de um programa (por exemplo, com REPLACE ou SHOW GETS).
