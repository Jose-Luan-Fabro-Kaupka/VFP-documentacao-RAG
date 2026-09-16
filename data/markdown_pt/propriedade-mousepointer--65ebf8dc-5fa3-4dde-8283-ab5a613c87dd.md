# Propriedade MousePointer

Especifica a forma do ponteiro do mouse quando você move o mouse sobre uma parte específica de um objeto em tempo de execução. Leitura/gravação em tempo de design e em tempo de execução.

Você pode usar a propriedade MousePointer para indicar alterações na funcionalidade conforme o ponteiro do mouse passa sobre controles em um formulário ou caixa de diálogo.

```foxpro
Object.MousePointer [= nType]
```

# Valor de retorno
 **nType**
Especifica um valor que representa a forma do ponteiro do mouse. Observação Quando você define a propriedade MousePointer usando a janela Properties, a lista suspensa exibe os nomes de configuração usados no Visual FoxPro para Windows. A tabela a seguir lista os valores para nType . nType Descrição 0 Forma determinada pelo objeto. (Padrão) 1 Seta. 2 Cruz (ponteiro em forma de mira). 3 I-beam. 4 Ícone (pequeno quadrado branco dentro de um quadrado preto). 5 Tamanho (seta de quatro pontas apontando para cima, baixo, esquerda e direita). 6 Tamanho NE SW (seta dupla apontando diagonalmente do canto inferior esquerdo para o superior direito). 7 Tamanho NS (seta dupla apontando verticalmente para cima e para baixo). 8 Tamanho NW SE (seta dupla apontando diagonalmente do canto inferior direito para o superior esquerdo). 9 Tamanho WE (seta dupla apontando horizontalmente para esquerda e direita). 10 Seta para cima. 11 Ampulheta ou relógio de pulso. Dica Para indicar que o usuário deve aguardar a conclusão de um processo, defina a propriedade MousePointer como 11. 12 No drop. 13 Ocultar ponteiro. 14 Seta. Observação Não é um valor de propriedade válido para grades. Se definido para grades, retorna o erro "Expression evaluated to an illegal value." 15 Mão. Observação Ao executar aplicativos Visual FoxPro em sistemas operacionais Windows 2000, uma seta aparece em vez de uma mão. 16 Seta para baixo. Dica Esta configuração é particularmente útil se a coluna pai de um cabeçalho substituir a configuração padrão da propriedade MousePointer do cabeçalho. 99 Personalizado. Usa o ponteiro especificado na propriedade MouseIcon do objeto.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object
