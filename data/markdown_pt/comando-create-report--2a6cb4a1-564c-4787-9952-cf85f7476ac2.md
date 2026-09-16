# Comando CREATE REPORT

Abre o Designer de relatórios para criar um relatório em formato padrão ou para criar um relatório personalizado.

```foxpro
CREATE REPORT [FileName | ?] [NOWAIT] [SAVE] [WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN] [PROTECTED]
```

#### Parâmetros
 **[ FileName | ?]**
Especifica o nome do arquivo do relatório ou exibe a caixa de diálogo Criar para que você possa digitar o nome do arquivo de relatório a criar. A extensão de arquivo padrão para relatórios é .frx. Observação Se o arquivo de relatório especificado já existir, o Visual FoxPro solicita que você substitua o arquivo existente se o comando SET SAFETY estiver definido como ON . Chamar CREATE REPORT sem argumentos abre o Designer de relatórios e atribui ao arquivo de relatório o nome padrão Report VersionNumber . Quando você fecha o Designer de relatórios, o Visual FoxPro solicita que você salve as alterações no relatório e forneça um nome diferente.
**[NOWAIT]**
Continua a execução do programa após o Designer de relatórios ser aberto. O programa não aguarda o fechamento do Designer de relatórios, mas continua a execução na linha imediatamente seguinte. Se você omitir NOWAIT , o Designer de relatórios é aberto e a execução do programa é pausada até que o Designer de relatórios seja fechado. Ao chamar CREATE REPORT com NOWAIT na janela Command, NOWAIT não tem efeito.
**[SAVE]**
Especifica que o Designer de relatórios permaneça aberto após a ativação de outra janela. Se você omitir SAVE , o Designer de relatórios é fechado quando você ativa outra janela. Ao chamar CREATE REPORT com SAVE na janela Command, SAVE não tem efeito.
**[WINDOW WindowName1 ]**
Especifica uma janela cujas características o Designer de relatórios herda. Por exemplo, se a janela especificada foi criada com a opção FLOAT de DEFINE WINDOW , você pode mover o Designer de relatórios. A janela especificada deve ser definida, mas não precisa estar ativa ou visível. Observação O Designer de relatórios possui um tamanho padrão que pode ser maior que a janela especificada. Nesse caso, o Designer de relatórios ainda herda as características da janela, com o canto superior esquerdo do Designer de relatórios posicionado nas mesmas coordenadas do canto superior esquerdo da janela especificada, mas se estende além das bordas da janela especificada.
**[IN [WINDOW] WindowName2 | IN SCREEN]**
Especifica abrir o Designer de relatórios em uma janela pai ou na janela principal do Visual FoxPro após colocar o Designer de etiquetas em uma janela pai. O Designer de relatórios não assume as características da janela pai e não pode ser movido para fora da janela pai. Se a janela pai é movida, o Designer de relatórios se move com ela. Observação Você deve primeiro definir a janela pai usando DEFINE WINDOW e torná-la visível para acesso pelo Designer de relatórios.
**[PROTECTED]**
Esta cláusula é ignorada pelo Designer de relatórios por padrão, porque um layout de relatório recém-criado não terá nenhum sinalizador de proteção definido. No entanto, um construtor de relatórios pode ser escrito para executar uma ação específica se esta cláusula estiver presente na coleção de parâmetros de linha de comando. Por exemplo, o construtor de relatórios padrão respeitará esta cláusula ocultando a guia Proteção da caixa de diálogo Propriedades do relatório. Consulte Compreendendo eventos do construtor de relatórios para obter mais informações.

# Observações

Você também pode criar relatórios usando um assistente. Para obter mais informações, consulte Como: criar relatórios (Visual FoxPro). Você também pode criar relatórios rápidos sem abrir o Designer de relatórios usando outra versão de CREATE REPORT. Para obter mais informações, consulte Comando CREATE REPORT - Relatório rápido.
