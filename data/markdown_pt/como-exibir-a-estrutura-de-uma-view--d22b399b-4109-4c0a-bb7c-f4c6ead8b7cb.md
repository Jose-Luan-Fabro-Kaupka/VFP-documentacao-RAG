# Como: exibir a estrutura de uma view

Você pode exibir a estrutura de uma view sem abrir o View Designer. Essa opção é útil quando você deseja examinar a estrutura de uma remote view sem esperar o download dos dados.

### Para exibir uma view sem dados
- Abra a view com o comando USE e a palavra-chave NODATA.
- Use o comando DISPLAY STRUCTURE para exibir as informações de estrutura da view na janela principal do Visual FoxPro.

Para obter mais informações, consulte USE Command.

> **Dica:** Usar a palavra-chave NODATA é a maneira mais rápida de recuperar a estrutura de uma view, pois cria o menor cursor possível na fonte de dados remota.

Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase. O comando USE abre uma remote view criada anteriormente chamada Customer_Remote_View com a palavra-chave NODATA na área de trabalho 0. O comando DISPLAY STRUCTURE grava as informações de estrutura em um arquivo chamado ViewStructure sem enviá-las para a janela principal do Visual FoxPro.

```foxpro
OPEN DATABASE MyDatabase
USE Customer_Remote_View NODATA IN 0
DISPLAY STRUCTURE TO FILE ViewStructure.txt NOCONSOLE
```
