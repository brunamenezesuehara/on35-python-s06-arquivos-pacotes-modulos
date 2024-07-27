import os

# Caminho do diretório atual onde o script está localizado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cria um novo arquivo CSV para armazenar os dados mesclados
output_file_path = os.path.join(current_dir, 'exerciciocasa0106.csv')
with open(output_file_path, 'w') as arquivo:
    arquivo.write("id,mean\n")

    # Lista dos arquivos CSV a serem mesclados
    csv_files = [
        'Planilha aula 06 - Página1.csv',
        'Planilha aula 06 - Página1 (1).csv',
        'Planilha aula 06 - Página1 (2).csv',
        'Planilha aula 06 - Página1 (3).csv',
        'Planilha aula 06 - Página1 (4).csv',
        'Planilha aula 06 - Página1 (5).csv',
        'Planilha aula 06 - Página1 (6).csv',
        'Planilha aula 06 - Página1 (7).csv'
    ]

    # Itera sobre cada arquivo CSV na lista
    for filename in csv_files:
        file_path = os.path.join(current_dir, filename)

        # Verifica se o arquivo existe
        if not os.path.exists(file_path):
            print(f"Arquivo não encontrado: {file_path}")
            continue

        try:
            with open(file_path) as open_csv:
                first_row = True
                # Itera sobre cada linha do arquivo CSV
                for line in open_csv:
                    # Ignora a linha de cabeçalho
                    if first_row:
                        first_row = False
                        continue
                    # Escreve a linha no novo arquivo CSV
                    arquivo.write(line.strip() + '\n')

        except Exception as e:
            print(f"Erro ao processar o arquivo {file_path}: {e}")

print("Arquivos mesclados com sucesso!")
