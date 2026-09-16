# Incorporação de hiperlinks

Os editores do Visual FoxPro suportam a incorporação e ativação de hiperlinks. Quando você inclui um hiperlink válido, o Visual FoxPro aplica atributos de hiperlink ao texto do hiperlink.

Se os hiperlinks forem ativados na caixa de diálogo Options ou definindo a propriedade EditorOptions, um hiperlink será exibido no seu editor com a indicação visual sublinhada típica de um hiperlink em HTML. O caractere de término do hiperlink é um espaço, portanto, se houver espaços no seu caminho, você deve substituí-los por %20. Por exemplo, http://servername/program files/my folder deve ser escrito http://servername/program%20files/my%20folder.

Por padrão, você precisa pressionar CTRL + clique para seguir um link. A propriedade EditorOptions permite alterar o padrão para que um clique simples siga o link. A tabela a seguir descreve os protocolos válidos.

| Protocolo | Acionador(es) | Sintaxe |
| --- | --- | --- |
| File | File:/ | file:/// cDrive/cPathcFile file://// cUNCPath |
| FTP | FTP:/ | ftp://[ cUserName [: cPassword @]] cDomain |
| Gopher | Gopher:/ | gopher ://cDomain |
| HTTP | HTTP:/, www.<char> | http ://cDomain |
| HTTPS | HTTP:/ | https ://cDomain |
| MailTo | MailTo: | mailto: cAddress [; cMoreAddresses ][& cSubject ] [& cBody ] [& cCC ][& cBCC ] |
| News | News: | news : cNewsGroup |
| Telnet | Telnet:/ | telnet:// cDomain [: iPort ] |
