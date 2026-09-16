# Como: verificar diferenças em formulários, relatórios e outros arquivos de tabela

No Visual FoxPro, apenas alguns tipos são tratados como arquivos de texto pelo controle de código-fonte, entre eles programas (.prg) e a lista de arquivos do projeto (.pjm). Formulários, relatórios e outros arquivos são tabelas com informações sobre seus componentes. Isso inclui .scx, .frx, .mnx, .lbx e .vcx.

Como são tabelas do Visual FoxPro, os sistemas de controle de código-fonte os tratam como arquivos binários. Assim, as ferramentas de comparação não conseguem identificar diferenças nem mostrar um histórico detalhado.

Para permitir comparações, o Visual FoxPro cria representações textuais desses arquivos e as mantém automaticamente sob controle de código-fonte.
 Representação textual de arquivo do Visual FoxPro

O Visual FoxPro inclui o utilitário Scctext.prg, mas você também pode usar outro programa.

### Para especificar um utilitário de conversão em texto
- Na caixa de diálogo Options, escolha Projects.
- Na caixa Text generation, informe o programa de conversão.
- Escolha Set as Default e OK.

O Visual FoxPro chama automaticamente o conversor ao adicionar um formulário, relatório, menu, rótulo ou classe visual a um projeto controlado. O arquivo textual tem o mesmo nome e usa "A" como última letra da extensão; Myform.scx gera Myform.sca. Ao fazer check-in, o texto também é criado e enviado.

Se o projeto já contiver esses arquivos, remova-os temporariamente e adicione-os novamente com a geração de texto habilitada.

### Para gerar representações textuais de arquivos existentes
- Faça backup dos formulários, relatórios, menus, rótulos e bibliotecas de classes.
- Verifique se não estão em check-out.
- No menu Project, escolha Source Control e Remove Files from Source Control.
- Selecione os arquivos e escolha OK.
- Habilite a geração de texto.
- No menu Project, escolha Source Control e Add Files to Source Control.
- Selecione os arquivos e escolha OK.

Ao colocar cada arquivo sob controle de código-fonte, o Visual FoxPro também cria sua representação textual.
