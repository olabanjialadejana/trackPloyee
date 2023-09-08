import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(cv2.CAP_ANY)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_image = cv2.imread("reference_image.jpg")


def check_face(frame):
	global face_match
	try:
		result = DeepFace.verify(frame, reference_image.copy(), distance_metric='euclidean_l2', model_name='VGG-Face',
								 enforce_detection=False)

		if result['distance'] < 0.4:
			face_match = True
		else:
			face_match = False
	except Exception as e:
		print(f"Error: {e}")
		face_match = False


while True:
	ret, frame = cap.read()

	if ret:
		if counter % 30 == 0:
			try:
				threading.Thread(target=check_face, args=(frame.copy(),)).start()
			except ValueError:
				pass
		counter += 1

		if face_match:
			cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
		else:
			cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

		cv2.imshow("video", frame)

	key = cv2.waitKey(1)
	if key == ord("q"):
		break

cv2.destroyAllWindows()
