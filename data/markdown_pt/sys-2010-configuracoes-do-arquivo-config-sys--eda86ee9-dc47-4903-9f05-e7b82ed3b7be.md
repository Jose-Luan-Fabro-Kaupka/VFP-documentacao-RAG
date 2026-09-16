# SYS(2010) - Configurações do arquivo CONFIG.SYS

Retorna a configuração files no CONFIG.SYS.

```foxpro
SYS(2010)
```

# Valor de retorno

Caractere

# Observações

No FoxPro para MS-DOS, SYS(2010) retorna como cadeia de caracteres a configuração files do seu arquivo de configuração CONFIG.SYS.

No Visual FoxPro, SYS(2010) sempre retorna 255.

A maioria dos arquivos Config.sys contém uma linha que especifica o número máximo de arquivos que podem ser abertos ao mesmo tempo no MS-DOS. Essa linha geralmente é FILES=NNN, em que NNN é um número. SYS(2010) retorna esse número.

Um arquivo de configuração Config.sys não precisa ter uma configuração files; além disso, você não precisa ter um arquivo Config.sys. SYS(2010) retorna a configuração files padrão do MS-DOS em qualquer um dos casos.

O número retornado por SYS(2010) não é o número de arquivos que você pode abrir no Visual FoxPro, FoxPro para Windows e FoxPro para MS-DOS. O MS-DOS abre arquivos para seu próprio uso. O Visual FoxPro e o FoxPro para Windows também abrem arquivos para seu uso interno, e o número desses arquivos abertos pode variar durante uma sessão do FoxPro. A configuração files no seu arquivo Config.sys deve ser um pouco maior que o número de arquivos que você deseja abrir no Visual FoxPro.

Para obter mais informações sobre o arquivo de configuração Config.sys, consulte o manual do MS-DOS.
