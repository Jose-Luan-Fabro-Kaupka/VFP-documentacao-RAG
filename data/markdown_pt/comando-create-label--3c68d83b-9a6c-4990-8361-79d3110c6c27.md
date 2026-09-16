# Comando CREATE LABEL

Abre o Label Designer para criar uma etiqueta em formato de etiqueta padrão ou para projetar uma etiqueta personalizada.

```foxpro
CREATE LABEL [FileName | ?] [NOWAIT] [SAVE] [WINDOW WindowName1]
   [IN [WINDOW] WindowName2 | IN SCREEN] [PROTECTED]
```

#### Parâmetros
 **[ FileName | ?]**
Especifica um nome de arquivo para a etiqueta ou exibe a caixa de diálogo Create para que você possa digitar o nome do arquivo de etiqueta a ser criado. A extensão de nome de arquivo padrão para etiquetas é .lbx. Observação Chamar CREATE LABEL sem argumentos abre o Label Designer e atribui ao arquivo de etiqueta o nome padrão Label VersionNumber . Quando você fecha o Label Designer, o Visual FoxPro solicita que você salve as alterações na etiqueta e forneça um nome diferente.
**[NOWAIT]**
Continua a execução do programa depois que o Label Designer é aberto. O programa não aguarda o fechamento do Label Designer, mas continua a execução na linha imediatamente seguinte. Se você omitir NOWAIT , o Label Designer é aberto e a execução do programa pausa até que o Label Designer seja fechado. Ao chamar CREATE LABEL com NOWAIT na janela Command, NOWAIT não tem efeito.
**[SAVE]**
Especifica que o Label Designer permaneça aberto após ativar outra janela. Se você omitir SAVE , o Label Designer fecha quando você ativa outra janela. Ao chamar CREATE LABEL com SAVE na janela Command, SAVE não tem efeito.
**[WINDOW WindowName1 ]**
Especifica uma janela cujas características o Label Designer herda. Por exemplo, se a janela especificada foi criada com a opção FLOAT de DEFINE WINDOW , você pode mover o Label Designer. A janela especificada deve estar definida, mas não precisa estar ativa ou visível. Observação O Label Designer tem um tamanho padrão que pode ser maior que a janela especificada. Neste caso, o Label Designer ainda herda as características da janela, com o canto superior esquerdo do Label Designer posicionado nas mesmas coordenadas do canto superior esquerdo da janela especificada, mas se estende além das bordas da janela especificada.
**[IN [WINDOW] WindowName2 | IN SCREEN]**
Especifica abrir o Label Designer em uma janela pai ou na janela principal do Visual FoxPro depois de posicionar o Label Designer em uma janela pai. O Label Designer não assume as características da janela pai e não pode se mover para fora da janela pai. Se a janela pai for movida, o Label Designer se move com ela. Observação Você deve primeiro definir a janela pai usando DEFINE WINDOW e torná-la visível para acesso pelo Label Designer.
**[PROTECTED]**
Esta cláusula é ignorada pelo Label Designer por padrão, porque um layout de etiqueta recém-criado não terá nenhum sinalizador de proteção definido. No entanto, um report builder pode ser escrito para executar uma ação específica se esta cláusula estiver presente na coleção de parâmetros de linha de comando. Por exemplo, o Report Builder padrão respeita esta cláusula ocultando a guia Protection da caixa de diálogo Report Properties. Consulte Understanding Report Builder Events para obter mais informações.

# Observações

Você também pode criar etiquetas usando um assistente. Para obter mais informações, consulte Como: criar etiquetas.
