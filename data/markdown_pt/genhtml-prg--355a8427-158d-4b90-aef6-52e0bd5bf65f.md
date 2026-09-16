# Genhtml.prg

Genhtml.prg é o programa padrão chamado pela variável de sistema _GENHTML.

Você pode usar _GenHTML para coletar facilmente dados estáticos ou converter formulários, etiquetas, relatórios e menus para visualização ou transmissão em email ou publicação como páginas Web. Você pode usar _GenHTML para compartilhar dados com sites que não têm o Visual FoxPro instalado ou para criar modelos para uso em páginas Web.

GenHTML.PRG é acessado no menu File quando você escolhe a opção Save As HTML. Esta opção de menu está disponível quando o Form Designer, Label Designer, Menu Designer ou Report Designer está ativo ou quando uma tabela ou cursor está aberta em uma janela Browse. GenHTML usa a fonte de dados especificada como base para gerar um documento HTML usando classes contidas na biblioteca de classes _HTML.VCX.

Você pode executar GenHTML na janela Command com a seguinte sintaxe:

```foxpro
DO (_GENHTML) WITH <cOutFile> <cSourceFile> [, <nShow>][,<vIELink>][,...
```

| parâmetro | descrição |
| --- | --- |
| cOutFile | Padrão = "" Especifica o nome do arquivo de saída. Quando nenhuma extensão é especificada, .HTM é o padrão. |
| cSourceFile | Padrão: = "" Especifica o nome do arquivo de origem, alias ou objeto. |
| nShow | Padrão: = 0 Especifica se GenHTML criará e abrirá o arquivo de saída. tnShow pode assumir os seguintes valores: 0 = Gerar arquivo de saída1 = Gerar e exibir arquivo de saída no editor Visual FoxPro.2 = Gerar e exibir arquivo de saída no Internet Explorer.3 = Gerar e exibir arquivo de saída após usar uma caixa de diálogo Save As4 = Criar objeto PUBLIC _oHTML e gerar um arquivo.5 = Criar um objeto PUBLIC _oHTML sem gerar um arquivo. |
| vIELink | Padrão: Especifica um link para um objeto Internet Explorer ou controle de navegador Web. |
| Object | Padrão: Especifica uma referência a um objeto Internet Explorer. |
| cStyle | Padrão: Especifica um ID de estilo em GenHTML.DBF. |
| tcScope | Padrão: Especifica o escopo de varredura definindo a propriedade cScope. |
| cHTMLClass | Padrão: Especifica a classe e, opcionalmente, a biblioteca de classes que é instanciada para o objeto HTML. |
