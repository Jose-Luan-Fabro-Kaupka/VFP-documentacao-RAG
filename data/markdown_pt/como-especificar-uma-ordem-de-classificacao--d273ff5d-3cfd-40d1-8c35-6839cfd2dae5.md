# Como: especificar uma ordem de classificação

Você pode especificar uma ordem de classificação para campos de caractere usados em operações subsequentes de indexação e classificação.

### Para especificar uma ordem de classificação
- No menu Tools, escolha Options.
- Selecione a guia Data.
- Na caixa Collating sequence, selecione a ordem de classificação apropriada. Para salvar essa configuração para sessões futuras do Visual FoxPro, escolha Set as Default. Dica Você também pode especificar uma ordem de classificação com o comando SET COLLATE TO ou a instrução COLLATE em seu arquivo Config.fpw. Para obter detalhes sobre Config.fpw, consulte Customizing the Visual FoxPro Environment.

A ordem de classificação atual não afeta índices criados anteriormente; no entanto, ela afeta os resultados de comparações e comandos como SEEK e SELECT - SQL.

Você pode alterar a ordem de classificação a qualquer momento. Por exemplo, após abrir uma tabela de clientes, você pode criar tags de índice representando diferentes ordens de classificação, conforme mostrado no código a seguir. Então você pode alterar a ordem de classificação simplesmente usando uma tag diferente:

```foxpro
USE customer
SET COLLATE TO "GENERAL"
INDEX ON fname TAG mygeneral ADDITIVE
SET COLLATE TO "MACHINE"
INDEX ON custid TAG mymachine ADDITIVE
SET COLLATE TO "DUTCH"
INDEX ON lname TAG mydutch ADDITIVE
```

> **Observação:** A ordem de classificação de um índice substitui a ordem de classificação atual.

A página de código atual determina quais ordens de classificação estão disponíveis. Se você usar o comando SET COLLATE para especificar uma ordem de classificação não suportada pela página de código atual, o Visual FoxPro gera um erro. Além disso, se você especificar uma ordem de classificação em Config.fpw que não seja suportada pela página de código atual, a ordem de classificação será padronizada para Machine.
