# Função CPCURRENT( )

Retorna a configuração de página de código do arquivo de configuração do Visual FoxPro ou a página de código atual do sistema operacional.

```foxpro
CPCURRENT([1 | 2])
```

# Observações

CPCURRENT( ) retorna:
 - A página de código atual do sistema operacional se CODEPAGE não estiver no arquivo de configuração. Versões anteriores retornavam 0.
- O número especificado em CODEPAGE; por exemplo, retorna 852 para CODEPAGE = 852.
- A página de código atual do sistema operacional para CODEPAGE = AUTO.

CPCURRENT(1) retorna a página de código atual do sistema operacional independentemente da configuração CODEPAGE.

CPCURRENT(2) sempre retorna a página de código subjacente do sistema operacional. No Windows, por exemplo, retorna a página de código do MS-DOS.

Para obter mais informações, consulte Páginas de código compatíveis com o Visual FoxPro e Desenvolvendo aplicativos internacionais.
