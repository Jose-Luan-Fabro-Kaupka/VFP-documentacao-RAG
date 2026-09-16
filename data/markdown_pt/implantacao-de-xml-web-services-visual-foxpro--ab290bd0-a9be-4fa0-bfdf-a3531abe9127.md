# Implantação de XML Web Services (Visual FoxPro)

Ao implantar aplicações Visual FoxPro que usam XML Web services, você deve incluir os componentes redistribuíveis do SOAP Toolkit. Se sua aplicação acessa apenas XML Web services existentes, você deve incluir apenas o merge module SOAP Client.

Para aplicações que publicam XML Web services, você deve incluir os merge modules do lado do cliente e do servidor do SOAP Toolkit. Além disso, você deve incluir os arquivos de suporte do servidor específicos, por exemplo, arquivos ASP listener e WSDL. Você também deve considerar usar os arquivos de foundation class de XML Web services, _WS3Utils.vcx e _WS3Client.vcx, para automatizar este processo ao executar a aplicação implantada pela primeira vez.

Se você automatizar o processo de publicação de XML Web service, pode criar um diretório virtual e gerar arquivos de suporte sob demanda. No entanto, é recomendado que você realize testes extensivos de Setup se escolher esta abordagem para implantação.
