# Função COMCLASSINFO( )

Retorna informações do registro sobre um objeto COM, como um servidor de automação do Visual FoxPro.

```foxpro
COMCLASSINFO(oObject [, nInfoType])
```

#### Parâmetros
 **oObject**
Uma referência de objeto a um objeto COM ou OLE.
**nInfoType**
Especifica o tipo de informação a retornar. A tabela a seguir lista os valores de nInfoType e as informações retornadas. nInfoType Informação retornada 1 (Padrão) O identificador programático (ProgID) do objeto. Um ProgID é uma entrada de registro que pode ser associada a um CLSID. 2 O VersionIndependentProgID do objeto. O VersionIndependentProgID associa um ProgID a um CLSID. Ele é usado para determinar a versão mais recente de um aplicativo de objeto, refere-se à classe do aplicativo e não muda de versão para versão. 3 O nome amigável do objeto. 4 O identificador de classe (CLSID) do objeto. Um CLSID é um identificador globalmente exclusivo que identifica um objeto de classe COM. 5 Tipo de objeto passado: Valor de retorno Descrição 1 Objeto Visual FoxPro 2 Controle ActiveX 3 Componente COM 4 Objeto OLEBound (campo General)

# Valor de retorno

Character

# Observações

COMCLASSINFO( ) retorna a cadeia de caracteres vazia se as informações do registro não estiverem disponíveis para o objeto especificado. Servidores de automação do Visual FoxPro são objetos COM, tanto arquivos executáveis .exe quanto bibliotecas de vínculo dinâmico .dll que você pode criar no Project Manager.

Se você criar uma instância de um controle ActiveX usando CREATEOBJECT( ), como no código a seguir, nInfoType retorna 3 (Componente COM) em vez de 2.

```foxpro
X=CREATEOBJECT("MSComctlLib.treectrl.2")
```

Para retornar 2 (controle ActiveX), você deve usar o objeto como tal, como no código a seguir:

```foxpro
ox.addobject("oc","olecontrol","MSComctlLib.treectrl.2")
```
