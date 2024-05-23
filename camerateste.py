import cv2

def main():
    # Define a resolução desejada (nesse caso, 640x480)
    width = 640
    height = 480

    # Inicializa a captura de vídeo da câmera com a resolução desejada
    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        # Lê um frame da câmera
        ret, frame = cap.read()

        # Exibe o frame capturado
        cv2.imshow('Camera', frame)

        # Aguarda a tecla 'q' ser pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos e fecha todas as janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
