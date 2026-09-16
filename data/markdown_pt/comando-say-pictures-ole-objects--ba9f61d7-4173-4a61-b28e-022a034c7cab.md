# Comando @ ... SAY - Pictures & OLE Objects

Incluído para compatibilidade com versões anteriores. Use o Image Control (Visual FoxPro), OLE Bound Control e OLE Container Control em vez disso.

Exibe imagens e objetos OLE ou chama o servidor OLE para executar um verbo de objeto OLE.

```foxpro
@ row, column
SAY picture file BITMAP
| general field
	[STYLE expC1]
	[CENTER]
	[ISOMETRIC | STRETCH]
	[SIZE expN1, expN2]
	[NOWAIT]
@ row, column SAY general field
	VERB expN3 | expC2
```

# Observações

Os comandos @ ... SAY Pictures & OLE Objects são suportados no FoxPro for Windows e FoxPro for Macintosh.

Use a primeira forma de sintaxe para exibir arquivos de imagem e objetos OLE (Object Linking and Embedding) na janela principal do FoxPro ou em uma janela definida pelo usuário. Arquivos de imagem e objetos OLE também podem ser direcionados para a impressora com @ ... SAY.

No FoxPro for Windows, você pode usar este comando para exibir .BMPs (arquivos de imagem bitmap).

No FoxPro for Macintosh, você pode exibir arquivos de imagem do tipo PICT e arquivos bitmap .BMP.

Se você emitir SET DEVICE TO SCREEN, a saída aparece na janela principal do FoxPro ou em uma janela definida pelo usuário ativa. SET DEVICE TO SCREEN é o padrão na inicialização. Se você emitir SET DEVICE TO PRINTER, a saída é direcionada para a impressora.

A segunda forma de sintaxe deste comando é usada para chamar o servidor OLE para atender a um verbo de um objeto OLE. Um verbo OLE é uma ferramenta poderosa para manipular objetos OLE. Use a cláusula VERB para executar comandos associados ao objeto OLE. Por exemplo, você pode iniciar a aplicação que criou o objeto OLE, ou editar ou imprimir um objeto OLE.
