# Exemplo de rastrear atividades em um projeto

Arquivo: ...\Samples\Solution\Tahoe\Acttrack.scx

Este exemplo torna possível abrir um projeto e manipular o projeto de qualquer maneira. Quaisquer alterações que você faça no projeto são armazenadas em uma tabela. Quando você fecha o projeto, pode visualizar as alterações que fez no projeto em uma janela browse.

Para obter mais informações sobre como o exemplo funciona, abra o formulário para examinar o código do exemplo.

Este exemplo contém as seguintes classes.

| Classe | Biblioteca | Descrição |
| --- | --- | --- |
| activity_tracker | project_hook.vcx | Cria um projeto e um log para documentar a atividade do projeto. |

Os procedimentos de evento na biblioteca de classes ProjectHook, Project_hook.vcx, contêm a maior parte do código que é executado quando eventos de projeto ocorrem. A biblioteca de classes ProjectHook é atribuída ao projeto no exemplo. Project_hook.vcx está localizado no diretório ...\Samples\Solution\Tahoe.
