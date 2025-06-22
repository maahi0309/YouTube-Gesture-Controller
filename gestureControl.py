import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import time

# Open YouTube
webbrowser.open("https://www.youtube.com")
time.sleep(5)

# Initialize MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
gesture_active = ""

def count_fingers(lmList):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if lmList[tips[0]][1] > lmList[tips[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # 4 Fingers
    for id in range(1, 5):
        if lmList[tips[id]][2] < lmList[tips[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                fingerCount = count_fingers(lmList)

                if fingerCount == 2 and gesture_active != "playpause":
                    pyautogui.press("space")  # play/pause
                    gesture_active = "playpause"
                    print("Play/Pause")

                elif fingerCount == 1 and gesture_active != "volup":
                    pyautogui.press("up")
                    gesture_active = "volup"
                    print("Volume Up")

                elif fingerCount == 0 and gesture_active != "voldown":
                    pyautogui.press("down")
                    gesture_active = "voldown"
                    print("Volume Down")

                elif fingerCount == 5 and gesture_active != "mute":
                    pyautogui.press("m")
                    gesture_active = "mute"
                    print("Mute/Unmute")

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    else:
        gesture_active = ""  # reset when no hand is visible

    cv2.imshow("YouTube Gesture Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
