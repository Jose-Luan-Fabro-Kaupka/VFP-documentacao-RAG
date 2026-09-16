# Caixa de diálogo Find (Visual FoxPro)

Esta caixa de diálogo contém opções que possibilitam pesquisar texto. O Visual FoxPro adiciona várias maneiras de acessar a caixa de diálogo Find pelo teclado.

| Teclas | Descrição |
| --- | --- |
| CTRL+F | Find. |
| CTRL+L | Replace. |
| F3 | Find Again ou abrir a caixa de diálogo Find. |
| CTRL+F3 | Atualizar Find com a palavra ou os caracteres selecionados na posição do cursor. |
| CTRL+SHIFT+F3 | Atualizar Find com a palavra ou os caracteres selecionados na posição do cursor para uma ocorrência anterior. |
 **Look For**
Especifica a cadeia de caracteres a pesquisar. Para pesquisar caracteres especiais, digite as seguintes representações da linguagem C nas caixas de texto da caixa de diálogo Find. Para pesquisar Digite Enter \r Tab \t Barra invertida \\ Nova linha (line feed) \n

No Visual FoxPro, as pesquisas suportam curingas.
 **Options**
Essas opções definem os limites e a direção da pesquisa. Se você especificar texto a pesquisar e não obtiver os resultados esperados, certifique-se de que as opções corretas estão selecionadas. Match Case Localiza texto que corresponde exatamente à combinação de letras maiúsculas e minúsculas que você digita na caixa Look For. Wrap Around Pesquisa o arquivo atual desde o ponto de inserção até o fim do arquivo e depois desde o início do arquivo até o ponto de inserção original. Match Whole Word Localiza ocorrências distintas de palavras, não grupos de caracteres dentro de palavras. Search Backward Pesquisa para trás a partir da posição atual do ponto de inserção até o início do arquivo. Use wildcards Possibilita usar caracteres curinga no texto de pesquisa. Com Use wildcards desmarcado, uma pesquisa literal é conduzida para quaisquer caracteres. Quando Use wildcards estiver selecionado, as seguintes regras se aplicam: Caractere Descrição Uso ? Qualquer caractere único Especificado no lugar do caractere ausente. * Zero ou mais caracteres Especificado no lugar do(s) caractere(s) ausente(s). # Qualquer dígito único Especificado no lugar do dígito ausente. < Início de uma palavra Encontra a expressão no início de uma palavra. > Fim de uma palavra Encontra a expressão no fim de uma palavra. Deve ser colocado após os caracteres a pesquisar. [charlist] Conjunto de caracteres Corresponde a qualquer um dos caracteres especificados entre colchetes. O conjunto pode ser um intervalo, separado por um traço (–) (por exemplo, [a-d]). [!charlist] Excluir caracteres Corresponde a qualquer caractere, exceto os que seguem o ponto de exclamação entre colchetes. \ Escape Corresponde ao caractere que segue a barra invertida (\). Isso possibilita encontrar caracteres usados na notação de expressão regular, como * e >.
**Scope**
Define quão extensa é a pesquisa. As opções Scope são habilitadas quando você está editando um procedimento em uma janela Code. Current Procedure Pesquisa somente o procedimento atual, que é exibido na janela Code. Current Object Pesquisa todos os procedimentos (código de evento) no objeto atual (selecionado). All Objects Pesquisa todos os procedimentos (código de evento) em todos os objetos no formulário ou conjunto de formulários atual. Se Wrap Around estiver selecionado, somente o método ou evento atual será pesquisado.
**Find Next**
Encontra a próxima ocorrência da cadeia de caracteres que você digitou na caixa Look For.
**Replace**
Expande a caixa de diálogo adicionando um botão Replace All e a caixa de entrada de texto Replace With, na qual você pode especificar o texto de substituição.
