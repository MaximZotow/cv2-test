import cv2
import os.path
import subprocess
def bluring (image,x1,x2,y1,y2,power):
    image[y1:y2, x1:x2] = cv2.blur(image[y1:y2, x1:x2], (power, power), 0)
def quick_cmd(cmd_str):
    cmd2 = cmd_str
    subprocess.call(cmd2, shell=True)


video_name="cam.mp4"
audio_name=os.path.splitext(video_name)[0]+".wav"
output_video=os.path.splitext(video_name)[0]+"-edit"+os.path.splitext(video_name)[1]
quick_cmd(f"ffmpeg -y -i {video_name} {audio_name}")
cap = cv2.VideoCapture(video_name)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video,fourcc ,(cap.get(cv2.CAP_PROP_FPS)),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
i = 0;
while (cap.isOpened()):
    i+=1
    ret, frame = cap.read()
    if (ret==True):
        bluring(frame,10,180,20,30,1000)
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

quick_cmd(f"ffmpeg -y -i {output_video} -i {audio_name} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4")

