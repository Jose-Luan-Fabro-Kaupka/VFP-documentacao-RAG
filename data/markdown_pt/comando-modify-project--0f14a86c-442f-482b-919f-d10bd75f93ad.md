# Comando MODIFY PROJECT

Abre o Gerenciador de Projetos para que você possa modificar ou criar um arquivo de projeto.

```foxpro
MODIFY PROJECT [FileName | ?] [NOWAIT] [SAVE] [NOSHOW] [NOPROJECTHOOK]
```

#### Parâmetros
 **Sem parâmetros**
Exibe a caixa de diálogo Abrir.
**[ FileName | ?]**
Especifica o nome do arquivo do projeto ou exibe a caixa de diálogo Abrir para que você possa abrir um arquivo de projeto (.pjx) existente ou digitar o nome de um novo projeto a ser criado. Se não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribuirá automaticamente a extensão .pjx.
**[NOWAIT]**
Continua a execução do programa depois que o Gerenciador de Projetos é aberto. O programa não espera que o Gerenciador de Projetos seja fechado; ele continua a execução na linha imediatamente posterior à que contém MODIFY PROJECT NOWAIT. Omitir NOWAIT quando MODIFY PROJECT é emitido em um programa abre o Gerenciador de Projetos e pausa a execução do programa até que ele seja fechado. NOWAIT funciona somente em um programa. Não tem efeito sobre MODIFY PROJECT quando emitido na janela Comando.
**[SAVE]**
Mantém o Gerenciador de Projetos aberto depois que outra janela é ativada. Se SAVE for omitido, o Gerenciador de Projetos será fechado quando outra janela for ativada. Incluir SAVE não tem efeito quando emitido na janela Comando.
**[NOSHOW]**
Especifica que o Gerenciador de Projetos seja ocultado, com sua propriedade Visible definida como False (.F.), quando for aberto. Para exibi-lo, defina sua propriedade Visible como true (.T.). NOSHOW permite manipular um projeto antes de exibi-lo no Gerenciador de Projetos. Observação: para evitar confusão com NOSHADOW, você não pode abreviar NOSHOW para menos de cinco caracteres.
**[NOPROJECTHOOK]**
Especifica que um objeto ProjectHook não deve ser criado quando o Gerenciador de Projetos for aberto. Inclua NOPROJECTHOOK para projetos que não serão manipulados por programação por meio dos ganchos do Gerenciador de Projetos. Observação: um objeto Project ainda é criado sempre que um arquivo de projeto (.pjx) é aberto.

# Observações

Em um projeto, você especifica todos os arquivos-fonte necessários para um aplicativo final, e então o Visual FoxPro garante que o aplicativo gerado se baseie nos arquivos-fonte mais recentes.

Um arquivo de projeto é uma tabela que controla todos os arquivos-fonte, como programas, formulários, menus, bibliotecas, relatórios, etiquetas, tabelas, índices e arquivos de formato. Um projeto também controla todas as dependências, referências e conexões entre os arquivos.

> **Observação:** Bibliotecas compartilhadas (arquivos .fll, .dll e CFM) não podem ser incluídas em projetos.

Um arquivo de projeto tem a extensão .pjx e um arquivo memo associado com a extensão .pjt.

Para obter informações sobre o Gerenciador de Projetos, consulte Compilação de um aplicativo.
