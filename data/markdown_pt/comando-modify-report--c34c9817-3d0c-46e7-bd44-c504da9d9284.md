# Comando MODIFY REPORT

Abre o Report Designer para criar ou modificar um relatório.

```foxpro
MODIFY REPORT [FileName | ?]
   [[WINDOW WindowName1] [IN [WINDOW] WindowName2 | IN SCREEN]]
   [NOENVIRONMENT] [NOWAIT] [PROTECTED] [SAVE]
```

#### Parâmetros
 **[ FileName | ? ]**
Especifica o nome do arquivo do relatório ou exibe a caixa de diálogo Open para que você possa selecionar um arquivo de relatório existente ou digitar o nome do arquivo de relatório a criar. A extensão de arquivo padrão para relatórios é .frx. Observação Se o arquivo de relatório que você especificar não existir ou não puder ser encontrado, MODIFY REPORT cria um novo arquivo de relatório. Chamar MODIFY REPORT sem argumentos exibe a caixa de diálogo Open. Escolher New abre o Report Designer e cria um novo arquivo de relatório com o nome padrão ReportNumber . Quando você fecha o Report Designer, o Visual FoxPro solicita que você salve as alterações no relatório e forneça um nome diferente.
**[[WINDOW WindowName1 ]**
Especifica uma janela cujas características o Report Designer herda. Por exemplo, se a janela especificada foi criada com a opção FLOAT de DEFINE WINDOW , você pode mover o Report Designer. A janela especificada deve estar definida, mas não precisa estar ativa ou visível. Observação O Report Designer tem um tamanho padrão que pode ser maior que a janela especificada. Nesse caso, o Report Designer ainda herda as características da janela com o canto superior esquerdo do Report Designer posicionado nas mesmas coordenadas do canto superior esquerdo da janela especificada, mas se estende além das bordas da janela especificada.
**[IN [WINDOW] WindowName2 | IN SCREEN]]**
Especifica abrir o Report Designer em uma janela pai ou na janela principal do Visual FoxPro depois de colocar o Report Designer em uma janela pai. O Report Designer não assume as características da janela pai e não pode se mover fora da janela pai. Se a janela pai for movida, o Report Designer se move com ela. Observação Você deve primeiro definir a janela pai usando DEFINE WINDOW e torná-la visível para acesso pelo Report Designer.
**[NOENVIRONMENT]**
Impede salvar o ambiente de dados do Visual FoxPro com o relatório e é incluído para compatibilidade com relatórios 2.x. Para obter mais informações, consulte Controlling Data in Reports . Dica Você pode restaurar o ambiente de dados associado a um relatório Visual FoxPro definindo a propriedade AutoOpenTables do ambiente de dados como True (.T.). Para garantir que o ambiente do relatório seja fechado quando a impressão do relatório terminar, defina a propriedade AutoCloseTables como True (.T.). Para obter mais informações, consulte AutoOpenTables Property e AutoCloseTables Property .
**[NOWAIT]**
Continua a execução do programa depois que o Report Designer abre. O programa não aguarda o fechamento do Report Designer, mas continua a execução na linha imediatamente seguinte. Se você omitir NOWAIT , o Report Designer abre e a execução do programa pausa até que o Report Designer seja fechado. Ao chamar MODIFY REPORT com NOWAIT na janela Command, NOWAIT não tem efeito.
**[PROTECTED]**
Especifica que o Report Designer deve abrir no modo "protected", que desabilita ou suprime certos recursos do Report Designer. Destinado a ser usado em aplicativos para expor a edição de formulários de relatório pelo usuário final de forma mais segura e controlada, onde algumas ações de edição potencialmente prejudiciais não podem ocorrer.
**[SAVE]**
Especifica que o Report Designer permaneça aberto depois de ativar outra janela. Se você omitir SAVE , o Report Designer fecha quando você ativa outra janela. Ao chamar MODIFY REPORT com SAVE na janela Command, SAVE não tem efeito.

# Observações

Você também pode editar relatórios usando a interface do usuário do Visual FoxPro. Para obter mais informações, consulte How to: Open Reports and Labels. Você também pode criar relatórios usando um assistente. Para obter mais informações, consulte How to: Create Reports (Visual FoxPro).
