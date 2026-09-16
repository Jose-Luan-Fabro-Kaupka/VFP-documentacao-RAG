# Comando MODIFY LABEL

Abre o Label Designer para criar ou modificar uma etiqueta.

```foxpro
MODIFY LABEL [FileName | ?]
   [[WINDOW WindowName1] [IN [WINDOW] WindowName2 | IN SCREEN]]
   [NOENVIRONMENT] [NOWAIT] [PROTECTED] [SAVE]
```

#### Parâmetros
 **[ FileName | ? ]**
Especifica o nome do arquivo da etiqueta ou exibe a caixa de diálogo Open para que você possa selecionar um arquivo de etiqueta existente ou digitar o nome do arquivo de etiqueta a ser criado. A extensão padrão dos arquivos de etiqueta é .lbx. Observação: se o arquivo de etiqueta especificado não existir ou não puder ser encontrado, MODIFY LABEL criará um novo arquivo de etiqueta. Chamar MODIFY LABEL sem argumentos exibe a caixa de diálogo Open. Escolher New abre o Label Designer e cria um novo arquivo de etiqueta com o nome padrão LabelNumber. Ao fechar o Label Designer, o Visual FoxPro solicita que você salve as alterações da etiqueta e forneça outro nome.
**[[WINDOW WindowName1 ]**
Especifica uma janela cujas características serão herdadas pelo Label Designer. Por exemplo, se a janela especificada tiver sido criada com a opção FLOAT de DEFINE WINDOW, você poderá mover o Label Designer. A janela especificada deve estar definida, mas não precisa estar ativa nem visível. Observação: o Label Designer tem um tamanho padrão que pode ser maior que a janela especificada. Nesse caso, ele ainda herda as características da janela, com seu canto superior esquerdo posicionado nas mesmas coordenadas do canto superior esquerdo da janela especificada, mas estende-se além das bordas dessa janela.
**[IN [WINDOW] WindowName2 | IN SCREEN]]**
Especifica a abertura do Label Designer em uma janela pai ou na janela principal do Visual FoxPro após posicioná-lo em uma janela pai. O Label Designer não assume as características da janela pai e não pode se mover para fora dela. Se a janela pai for movida, o Label Designer se moverá com ela. Observação: primeiro você deve definir a janela pai usando DEFINE WINDOW e torná-la visível para que o Label Designer possa acessá-la.
**[NOENVIRONMENT]**
Impede que o ambiente de dados do Visual FoxPro seja salvo com a etiqueta e é incluído para compatibilidade com etiquetas da versão 2.x. Para obter mais informações, consulte Controlando dados em relatórios. Dica: você pode restaurar o ambiente de dados associado a uma etiqueta do Visual FoxPro definindo a propriedade AutoOpenTables do ambiente de dados como True (.T.). Para garantir que o ambiente da etiqueta seja fechado quando a impressão terminar, defina a propriedade AutoCloseTables como True (.T.). Para obter mais informações, consulte Propriedade AutoOpenTables e Propriedade AutoCloseTables.
**[NOWAIT]**
Continua a execução do programa após a abertura do Label Designer. O programa não espera o fechamento do Label Designer, mas continua a execução na linha imediatamente seguinte. Se você omitir NOWAIT, o Label Designer será aberto e a execução do programa ficará pausada até que ele seja fechado. Ao chamar MODIFY LABEL com NOWAIT na janela Command, NOWAIT não terá efeito.
**[PROTECTED]**
Especifica que o Label Designer deve ser aberto no modo “protegido”, que desabilita ou suprime determinados recursos do Designer. Destina-se ao uso em aplicativos para permitir que usuários finais editem formulários de etiqueta de maneira mais segura e controlada, sem que determinadas ações de edição potencialmente prejudiciais possam ocorrer.
**[SAVE]**
Especifica que o Label Designer permaneça aberto após a ativação de outra janela. Se você omitir SAVE, o Label Designer será fechado quando outra janela for ativada. Ao chamar MODIFY LABEL com SAVE na janela Command, SAVE não terá efeito.

# Observações

Você pode editar etiquetas usando a interface do usuário do Visual FoxPro. Para obter mais informações, consulte Como: abrir relatórios e etiquetas. Também é possível criar etiquetas usando um assistente. Para obter mais informações, consulte Como: criar etiquetas.
