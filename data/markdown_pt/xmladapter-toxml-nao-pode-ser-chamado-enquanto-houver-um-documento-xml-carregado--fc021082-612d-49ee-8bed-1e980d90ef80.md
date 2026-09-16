# XMLAdapter.ToXML não pode ser chamado enquanto houver um documento XML carregado. (Erro 2107)

O Visual FoxPro não permite que o método ToXML seja executado quando um documento XML já está carregado.
 - Verifique a propriedade IsLoaded para garantir que um documento XML não esteja já carregado.
- Use o método ReleaseXML para liberar o documento XML atualmente carregado.
