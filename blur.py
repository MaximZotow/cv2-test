import cv2
import os.path
import subprocess
def bluring (image,x1,x2,y1,y2,power):
    image[y1:y2, x1:x2] = cv2.blur(image[y1:y2, x1:x2], (power, power), 0)
def quick_cmd(cmd_str):
    cmd2 = cmd_str
    subprocess.call(cmd2, shell=True)
def blurimage(image,power):
    #преобразование изображения в чб и отсев "лишнего" методом ОЦУ
    img2gray = cv2.cvtColor(image[0:50, 0:200], cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(img2gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contour, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        x, y, w, h = cv2.boundingRect(cnt)
        bluring(image, x, x + w, y, y + h,power)
#исходное видео
video_name="cam.mp4"
#аудио-дорожка, извлечённая из видео
audio_name=os.path.splitext(video_name)[0]+".wav"
#полученное после opencv видео без звука
output_video=os.path.splitext(video_name)[0]+"-edit"+os.path.splitext(video_name)[1]

quick_cmd(f"ffmpeg -y -loglevel quiet -i {video_name} {audio_name}")
cap = cv2.VideoCapture(video_name)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video,fourcc ,(cap.get(cv2.CAP_PROP_FPS)),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
#показ числа кадров для отлова возможных ошибок
i = 0;
while (cap.isOpened()):
    i+=1
    ret, frame = cap.read()
    if (ret==True):
        blurimage(frame,1000)
        out.write(frame)
        print(i)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

quick_cmd(f"ffmpeg -y -loglevel quiet -i {output_video} -i {audio_name} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4")

