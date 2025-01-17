import cv2
import numpy as np


def converter_imagem(imagem_path, tipo='cinza', threshold=127):
    # Carregar a imagem
    imagem = cv2.imread(imagem_path)

    if tipo == 'cinza':
        # Converter para níveis de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        return imagem_cinza
    elif tipo == 'binarizada':
        # Converter para binarizada (preto e branco)
        _, imagem_binaria = cv2.threshold(imagem, threshold, 255, cv2.THRESH_BINARY)
        return imagem_binaria
    else:
        raise ValueError("Tipo de conversão inválido. Escolha 'cinza' ou 'binarizada'.")


# Exemplo de uso
imagem_path = 'imagem.jpg' # Coloque aqui a imagem que deseja transformar
imagem_cinza = converter_imagem(imagem_path, tipo='cinza')
imagem_binaria = converter_imagem(imagem_path, tipo='binarizada')

# Salvar as imagens convertidas
cv2.imwrite('imagem_cinza.jpg', imagem_cinza)
cv2.imwrite('imagem_binaria.jpg', imagem_binaria)
