# Passar dados para parâmetros

Você pode passar dados, como variáveis e elementos de matriz, como "argumentos" para parâmetros por referência ou por valor. Passar dados por referência salva as alterações feitas nos dados e passa essas alterações de volta ao programa chamador. Passar dados por valor passa uma cópia dos dados para processamento, mantendo os dados originais intactos.

Por padrão, os dados passam para procedimentos por referência e para funções definidas pelo usuário (UDFs) por valor. No entanto, você pode alterar os protocolos padrão para passar dados por parâmetros, embora o Visual FoxPro sempre passe objetos por referência.

> **Observação:** Ao passar matrizes inteiras para parâmetros, você deve passá-las por referência. Se você não passar matrizes por referência, apenas o primeiro elemento é passado. Portanto, elementos individuais de matriz são sempre passados por valor.
