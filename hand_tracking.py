import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

def get_direction(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    direction = None
    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            index_tip = handLms.landmark[8]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            # Screen zone logic
            if y < h/3:
                direction = "UP"
            elif y > 2*h/3:
                direction = "DOWN"
            elif x < w/3:
                direction = "LEFT"
            elif x > 2*w/3:
                direction = "RIGHT"

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    return frame, direction

