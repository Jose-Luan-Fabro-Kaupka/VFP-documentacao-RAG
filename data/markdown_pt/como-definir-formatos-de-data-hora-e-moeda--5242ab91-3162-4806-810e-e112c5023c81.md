# Como: definir formatos de data, hora e moeda

Para formatar datas, horas e moeda, você pode usar uma variedade de técnicas de formatação. Você pode:
 - Permitir que o Visual FoxPro use as configurações estabelecidas no Painel de controle.
- Especificar um idioma ou um formato específico na caixa de diálogo Opções do Visual FoxPro que deseja usar.
- Formatar informações de data, hora e moeda em código.

### Para definir um formato para datas, horas e moeda
- No menu Tools, escolha Options e clique na guia Regional.
- Para usar as configurações feitas com o Painel de controle do Windows, escolha Use system settings. -ou- Escolha um idioma ou formato para datas e horas e depois escolha opções para formatar moeda e números. Observação Se você escolher o formato Short ou Long para o formato de data, não pode especificar mais opções para o formato de data, e as configurações são lidas do Painel de controle do Windows.
- Escolha OK para usar as opções nesta sessão, ou Set As Default para tornar as alterações as configurações padrão desta cópia do Visual FoxPro.

Você também pode usar os comandos SET SYSFORMATS e SET DATE. Como regra, você emitiria este comando durante a inicialização da sua aplicação (por exemplo, no arquivo de configuração). O padrão para SET SYSFORMATS é OFF, então você deve definir explicitamente como ON ao iniciar sua aplicação.

Você pode estabelecer validação de dados em caixas de texto individuais definindo a propriedade Format da caixa de texto. Observe que a formatação da caixa de texto tem precedência sobre a formatação em todo o sistema.
