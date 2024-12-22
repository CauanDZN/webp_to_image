import os
from PIL import Image

def convert_webp_to_png(folder_path):
    """
    Converte todas as imagens WEBP de uma pasta para PNG, substituindo na mesma pasta.
    
    Args:
        folder_path (str): Caminho da pasta contendo as imagens WEBP.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(".webp"):
            try:
                with Image.open(file_path) as img:
                    new_file_path = os.path.splitext(file_path)[0] + ".png"

                    img.convert("RGBA").save(new_file_path, "PNG")
                    print(f"Convertido: {filename} -> {os.path.basename(new_file_path)}")

                os.remove(file_path)
                print(f"Removido: {filename}")
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

folder_path = input("Digite o caminho da pasta contendo as imagens WEBP: ").strip()

if os.path.isdir(folder_path):
    convert_webp_to_png(folder_path)
else:
    print("O caminho fornecido não é válido. Por favor, tente novamente.")
