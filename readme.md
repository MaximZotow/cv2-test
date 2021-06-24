# Ветки
В проекте 4 ветки, каждая отвечает за способ обработки:

1. [base-image](https://github.com/MaximZotow/cv2-test/tree/base-image) --- размывает картинку в строго заданном месте
1. [base-video](https://github.com/MaximZotow/cv2-test/tree/base-video) --- аналогично с видео
1. [adv-image](https://github.com/MaximZotow/cv2-test/tree/adv-image) --- берётся кусок изображения и при помощи алгоритма Оцу ищется текст, который затем оказывается в области, которую передаём функции "размытия
1. [adv-video](https://github.com/MaximZotow/cv2-test/tree/adv-video) --- аналогично изображению, однако в некоторых местах у камеры цвет текста меняется с черного на белый, что сказывается на размере и расположении области
