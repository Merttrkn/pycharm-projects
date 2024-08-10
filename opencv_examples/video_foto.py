import cv2
import sys
def fotograf_oynat():
    path = 'elma.jpg'

    image = cv2.imread(path)

    window_name = 'image'

    cv2.imshow(window_name, image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

def video_oynat():
    cap = cv2.VideoCapture('manzara.mp4')

    if (cap.isOpened() == False):
        print("Error opening video file")

    while (cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:

            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        print("1 - Fotoğraf Oynat")
        print("2 - Video Oynat")
        print("0 - Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            fotograf_oynat()
        elif secim == '2':
            video_oynat()
        elif secim == '0':
            sys.exit()
        else:
            print("Hatalı Sayı")
