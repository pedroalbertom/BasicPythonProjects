# Abra o arquivo de entrada (arquivo.txt) e o arquivo de saída (arquivo_formatado.txt)
with open('palavras.txt', 'r', encoding='utf-8') as arquivo_entrada, open('arquivo_formatado.txt', 'w', encoding='utf-8') as arquivo_saida:
    # Leia cada linha do arquivo de entrada
    for linha in arquivo_entrada:
        # Remove espaços em branco no início e no fim da palavra e adiciona as aspas
        palavra_formatada = f'"{linha.strip()}",'
        # Escreve a palavra formatada no arquivo de saída
        arquivo_saida.write(palavra_formatada)

print("Concluído! As palavras foram formatadas e escritas no arquivo_formatado.txt")