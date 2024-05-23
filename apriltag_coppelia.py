import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        self.subscription = self.create_subscription(Image, 'nome_do_topico', self.callback, 10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Processamento de imagem com OpenCV
        # Aqui você pode adicionar seu código de processamento de imagem usando o OpenCV

        # Exemplo: exibindo a imagem
        cv2.imshow('Imagem do Vision Sensor', cv_image)
        cv2.waitKey(1)  # Aguarda um pouco para que a janela seja exibida

def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    image_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
