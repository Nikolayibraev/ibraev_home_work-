#--------------- H O M E  W O R K  (M O D U L E _ 11 _ 1) ---------------

from PIL import Image

image = Image.open('mountain.jpg')                  #откр изображение
image.show('mountain_2.jpg')                        #показать изображение

resized_image = image.resize((200, 200))            #меняем размер
resized_image.save('mountain_2.jpg')

image.save('mountain_png.png', 'PNG')     #меняем формат

# ФУНКЦИЯ
def resize_image(in_image, out_image, size):
    image = Image.open(in_image)
    resized_image = image.resize(size)
    resized_image.save(out_image, format='PNG')
    print('Изображение сохранено как', out_image)

resize_image('mountain.jpg', 'mountain.png', (200, 200))

