# Variável de sistema _SAMPLES

Contém o caminho do diretório no qual os exemplos do Microsoft Visual FoxPro estão instalados.

```foxpro
_SAMPLES = cPath
```

#### Parâmetros
 **cPath**
Especifica o caminho completo para o diretório que contém os exemplos do Visual FoxPro.

# Observações

_SAMPLES especifica o caminho do diretório que contém os exemplos do Visual FoxPro. Esse caminho geralmente é o subdiretório \Samples no diretório raiz do Visual FoxPro, que você pode determinar usando a função HOME(). Se você não instalar os exemplos do Visual FoxPro, _SAMPLES ainda aponta para o subdiretório \Samples porque é o local padrão para instalação dos exemplos.

O caminho contido em _SAMPLES é lido de uma chave de registro do MSDN no Registro do Windows. Se essa chave de registro não existir (por exemplo, se você não instalou os exemplos), _SAMPLES contém a cadeia de caracteres vazia.

Você também pode especificar um caminho para o diretório de exemplos com o item Samples Directory na guia File Locations Tab, Options Dialog Box da caixa de diálogo Options. Se você usar a caixa de diálogo Options para especificar um caminho para o diretório de exemplos, _SAMPLES contém o caminho que você especificar. Se você escolher Set As Default, o caminho é salvo para sessões subsequentes do Visual FoxPro.

HOME(2) retorna o caminho contido em _SAMPLES.
