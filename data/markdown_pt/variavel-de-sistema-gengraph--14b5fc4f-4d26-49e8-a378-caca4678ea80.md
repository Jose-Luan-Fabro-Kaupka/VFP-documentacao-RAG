# Variável de sistema _GENGRAPH

Incluída para compatibilidade com versões anteriores. Use o Graph Wizard em seu lugar.

Especifica o aplicativo usado para enviar resultados de consultas RQBE ao Microsoft Graph (FoxPro para Windows e Macintosh) ou FoxGraph (FoxPro para MS-DOS).

```foxpro
_GENGRAPH = program name
```

# Observações

Com _GENGRAPH, você pode especificar o aplicativo que o FoxPro usa para enviar resultados de consultas RQBE ao Microsoft Graph ou FoxGraph. Por padrão, _GENGRAPH usa o aplicativo GENGRAPH.APP fornecido com o FoxPro. É possível incluir um caminho com o nome do aplicativo.

As consultas são criadas na janela RQBE. Nela, escolha Graph no menu pop-up Output para especificar o destino dos resultados. Eles podem ser enviados a um gráfico criado com Microsoft Graph ou FoxGraph.

Para obter mais informações sobre a criação de consultas na janela RQBE, consulte CREATE QUERY ou o capítulo "Querying Your Data with RQBE" no Guia do Usuário do FoxPro.
