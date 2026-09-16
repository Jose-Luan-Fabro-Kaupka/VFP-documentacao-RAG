# Entendendo objetos contêiner e controle

Você pode adicionar os seguintes tipos de objetos a um formulário:
 - Controles
- Contêineres
- Classes definidas pelo usuário
- Compartilhando informações e adicionando OLE

Objetos no Visual FoxPro pertencem a uma de duas categorias, dependendo da natureza da classe em que se baseiam:
 - Contêineres podem conter outros contêineres ou controles. Podem atuar como o objeto pai para outros objetos. Por exemplo, um formulário, como contêiner, é o objeto pai de uma caixa de seleção nesse formulário.
- Controles podem ser colocados em contêineres, mas não podem ser o pai de outros objetos. Por exemplo, uma caixa de seleção não pode conter nenhum outro objeto.

O Form Designer permite projetar tanto contêineres quanto controles.

| Contêiner | Pode conter |
| --- | --- |
| Column | Headers e quaisquer objetos exceto form sets, formulários, barras de ferramentas, timers e outras colunas |
| Command button group | Command buttons |
| Form-set | Formulários, barras de ferramentas |
| Form | Page frames, grids, quaisquer controles |
| Grid | Columns |
| Option button group | Option buttons |
| Page frame | Pages |
| Page | Grids, quaisquer controles |

# Propriedades Collection e Count

Todos os objetos contêiner no Visual FoxPro têm uma propriedade count e uma propriedade collection associadas a eles. A propriedade collection é uma matriz que referencia cada objeto contido. A propriedade count é uma propriedade numérica que indica o número de objetos contidos.

As propriedades collection e count para cada contêiner são nomeadas de acordo com o tipo de objeto que pode ser contido no contêiner. A tabela a seguir lista os contêineres e as propriedades collection e count correspondentes.

| Contêiner | Propriedade Collection | Propriedade Count |
| --- | --- | --- |
| Application | Objects Forms | Count FormCount |
| FormSet | Forms | FormCount |
| Form | Objects Controls | Count ControlCount |
| PageFrame | Pages | PageCount |
| Page | Controls | ControlCount |
| Grid | Columns | ColumnCount |
| CommandGroup | Buttons | ButtonCount |
| OptionGroup | Buttons | ButtonCount |
| Column | Controls | ControlCount |
| ToolBar | Controls | ControlCount |
| Container | Controls | ControlCount |
| Control | Controls | ControlCount |

Essas propriedades permitem usar um loop para manipular programaticamente todos ou objetos contidos específicos. Por exemplo, as linhas de código a seguir definem a propriedade BackColor, ForeColor das colunas em uma grade para verde e vermelho alternados:

```foxpro
o = THISFORM.grd1
FOR i = 1 to o.ColumnCount
   IF i % 2 = 0 && Even-numbered column
      o.Columns(i).BackColor = RGB(0,255,0) && Green
   ELSE
      o.Columns(i).BackColor = RGB(255,0,0) && Red
   ENDIF
ENDFOR
```
