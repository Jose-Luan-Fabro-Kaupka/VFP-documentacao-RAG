# Função ANETRESOURCES( )

Coloca os nomes de compartilhamentos de rede ou impressoras em um array e retorna o número de recursos.

```foxpro
ANETRESOURCES(ArrayName, cNetworkName, nResourceType)
```

#### Parâmetros
 **ArrayName**
Especifica o nome do array que contém as informações de compartilhamento de rede ou impressora. Se o array que você especificar não existir, o Visual FoxPro o cria automaticamente. Se o array existir e não for grande o suficiente para conter todas as informações, o Visual FoxPro aumenta automaticamente o tamanho do array para acomodar as informações. Se o array for maior do que o necessário, o Visual FoxPro o trunca. Se o array existir e ANETRESOURCES( ) retornar 0 porque nenhum compartilhamento de rede ou impressora foi encontrado, o array permanece inalterado. Se o array não existir e ANETRESOURCES( ) retornar 0, o array não é criado.
**cNetworkName**
Especifica o nome da rede ou domínio para o qual as informações de compartilhamento ou impressora são retornadas. O nome da rede deve estar no formato "\\NetworkName." Você não precisa estar conectado à rede que especificar, e especificar uma rede não conecta você a ela. Se você especificar um nome de domínio, ANETRESOURCES( ) retorna um array de membros ou recursos desse domínio.
**nResourceType**
Especifica o tipo de recurso de rede para o qual as informações são retornadas. Os nomes de compartilhamentos na rede são retornados se nResourceType for avaliado como 1. Os nomes de impressoras na rede são retornados se nResourceType for avaliado como 2. Um valor 0 retorna o nome de qualquer recurso.

# Valor de retorno

Numeric

# Observações

ANETRESOURCES( ) retorna o número de compartilhamentos de rede ou impressoras encontrados (idêntico ao número de linhas no array). ANETRESOURCES( ) retorna zero se não houver compartilhamentos ou impressoras para a rede do tipo que você especificar, ou se a rede que você especificar não existir.

> **Observação:** Antes do Windows 2000, os nomes de compartilhamento eram limitados a doze caracteres. Se você executar ANETRESOURCES() em um computador que usa um sistema operacional anterior ao Windows 2000, ANETRESOURCES() não retornará compartilhamentos em computadores executando Windows 2000 ou posterior que tenham nomes de compartilhamento com mais de doze caracteres.

Consulte as funções Win32 API WNetOpenEnum e WNetEnumResource para obter mais detalhes.
