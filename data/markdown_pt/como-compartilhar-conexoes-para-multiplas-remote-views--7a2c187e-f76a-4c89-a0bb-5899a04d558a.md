# Como: compartilhar conexões para múltiplas remote views

Você pode usar uma conexão ativa como pipeline de informações para múltiplas remote views compartilhando uma conexão. Quando você compartilha uma conexão ativa, você:
 - Reduz o número de conexões em um servidor remoto.
- Reduz custos de conexões a servidores que cobram por conexão.

Você compartilha conexões definindo a definição da view para usar uma conexão compartilhada na ativação. Quando a view é usada, o Visual FoxPro conecta-se à fonte de dados remota usando a conexão compartilhada existente (se houver). Se uma conexão compartilhada não estiver em uso, o Visual FoxPro cria uma conexão exclusiva quando a view é aberta, que pode então ser compartilhada com outras views.

Somente uma instância ativa de uma definição de conexão nomeada é compartilhada durante uma sessão do Visual FoxPro. Se múltiplas instâncias da mesma definição de conexão estiverem ativas, a primeira instância a ser usada como conexão compartilhada torna-se a conexão compartilhada designada. Todas as views que usam essa definição de conexão e empregam compartilhamento de conexão acessarão o servidor remoto através da conexão compartilhada designada.

Conexões diferentes da conexão compartilhada designada não são compartilhadas. O compartilhamento de conexão não é limitado a sessions.

### Para compartilhar uma conexão
- No menu Tools, escolha Options e selecione a guia Remote Data; depois selecione Share connection na área Remote view defaults e escolha OK . -ou-
- Use os designers Query e View . -ou-
- Use o comando CREATE SQL VIEW Command com a cláusula SHARE.

O código a seguir cria uma view que, quando ativada com o comando USE Command, compartilha uma conexão:

```foxpro
CREATE SQL VIEW product_view_remote ;
   CONNECTION remote_01 SHARE AS ;
   SELECT * FROM products
USE product_view_remote
```
