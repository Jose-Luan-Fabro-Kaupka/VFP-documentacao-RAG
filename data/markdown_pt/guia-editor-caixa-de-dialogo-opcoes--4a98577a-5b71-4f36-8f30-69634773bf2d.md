# Guia Editor, caixa de diálogo Opções

Fornece opções para personalizar a funcionalidade de edição na janela Command e na maioria dos editores do Visual FoxPro. Por exemplo, essas opções não se aplicam a janelas de edição abertas com os comandos MODIFY FILE e MODIFY MEMO, exceto onde indicado.

Quando você escolhe Definir como padrão, que aparece em cada guia da caixa de diálogo, o Visual FoxPro salva as configurações no Registro do Windows.

# Opções do editor

Fornece opções para especificar a funcionalidade das janelas de edição.
 **Margem de seleção**
Especifica se os editores exibem uma margem de seleção para que você possa selecionar uma linha e especificar breakpoints, bookmarks ou atalhos da lista de tarefas. Para obter mais informações, consulte Como: criar bookmarks e atalhos da lista de tarefas .
**Arrastar e soltar entre palavras**
Especifica se as operações de arrastar permitem arrastar para dentro de palavras ou apenas entre palavras.
**Habilitar hyperlinks**
Especifica se os editores reconhecem linhas que começam com "http:/" como hyperlinks.
**Cadeia de comentário**
Especifica o caractere que identifica um comentário no código. A cadeia de comentário padrão é *!*.
**Compilação em segundo plano**
Especifica um estilo de formatação usado para indicar sintaxe inválida quando a coloração de sintaxe está ativada. Quando a linha atual de código que você está digitando contém sintaxe inválida, o Visual FoxPro exibe a linha de código com um dos seguintes estilos de formatação: Inversão vermelha A sintaxe inválida aparece em vermelho enquanto as palavras-chave válidas aparecem em rosa. (Padrão) Linha cinza A linha que contém sintaxe inválida aparece em cinza. Sublinhado A linha que contém sintaxe inválida aparece sublinhada. Nenhum A sintaxe inválida não é indicada. A configuração Compilação em segundo plano é suportada para janelas de edição abertas com o comando MODIFY MEMO. Para obter mais informações, consulte Como: exibir e imprimir código-fonte em cores .
**Duração do destaque**
Especifica o número de milissegundos para destacar instruções em delimitadores parentéticos ou de colchetes. Você pode selecionar uma das configurações da lista ou digitar qualquer duração específica na caixa manualmente.

# Configurações de cor de sintaxe

Fornece opções para coloração de sintaxe.
 **Área**
Especifica o elemento do programa para o qual definir estilos de fonte e cor. Quando você faz sua seleção, as outras opções são atualizadas com valores apropriados para a área selecionada.
**Estilo da fonte**
Especifica um estilo de fonte para a área selecionada. Por exemplo, para exibir todos os comentários em programas em itálico, selecione Comments na caixa Área e selecione Italic na caixa Estilo da fonte.
**Primeiro plano**
Especifica uma cor para o texto da área selecionada. Para usar a cor padrão definida no Painel de controle, selecione Automático.
**Plano de fundo**
Especifica uma cor de plano de fundo para a área selecionada. Por exemplo, para mostrar comentários em texto amarelo sobre fundo azul, escolha Comments na caixa Área, selecione amarelo em Primeiro plano e selecione azul em Plano de fundo . Para usar a cor padrão definida no Painel de controle, selecione Automático .
**Área de exemplo**
Exibe o efeito das suas configurações.
**Redefinir tudo**
Define a coloração de sintaxe para as configurações padrão do Visual FoxPro.
