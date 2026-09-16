# SYS(2700) — Ativa temas do Windows XP

Ativa ou desativa totalmente o suporte a temas do Windows XP no Visual FoxPro.

```foxpro
SYS(2700 [, nValue ])
```

#### Parâmetros
**nValue**
Especifica um valor numérico que determina se o suporte a temas será desativado ou ativado. A tabela a seguir lista os valores de nValue. nValue Configuração 0 Desativa o suporte a temas. 1 Ativa o suporte a temas. (Padrão)

# Valor de retorno

Tipo de dados caractere. Se os temas não estiverem ativados ou se você estiver executando um sistema operacional antigo que não oferece suporte a temas, SYS(2700) retornará 0 quando os argumentos forem omitidos. Se os temas estiverem ativados, SYS(2700) retornará 1.

# Observações

O comportamento de chamar SYS(2700) sem argumentos para retornar a configuração atual difere da variável de sistema _SCREEN, pois sempre retorna o estado dos temas no computador. Portanto, se você usar `SYS(2700,1)` para ativar os temas no Visual FoxPro e desativá-los pelo painel de controle Display do Windows, SYS(2700) retornará 0, enquanto _SCREEN.Themes ainda retornará True (.T.).

Quando você altera o suporte a temas usando a função SYS(2700), o Visual FoxPro pode não atualizar automaticamente a interface do usuário. Contudo, quando os temas estão ativados, determinados efeitos, como os exibidos ao mover o mouse sobre controles, funcionarão. Portanto, recomenda-se definir o suporte a temas no início de um aplicativo, antes que a interface do usuário seja renderizada.

> **Observação:** Se você alterar o suporte a temas enquanto um formulário estiver em execução, poderá chamar o método Refresh do formulário para redesenhar os controles com tema.
