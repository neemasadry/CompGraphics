from pathlib import Path
import cv2

# monolith = Path("/Users/neema/Dropbox/Semesters/Winter 2023/CSC 5870 - Computer Graphics I/Assignments/colimg/input/Monolith.mp4")
# witcher = Path("/Users/neema/Dropbox/Semesters/Winter 2023/CSC 5870 - Computer Graphics I/Assignments/colimg/input/Witcher.mp4")
outputs = Path("/Users/neema/Dropbox/Semesters/Winter 2023/CSC 5870 - Computer Graphics I/Assignments/colimg/python/outputs")
# outputs.mkdir(exist_ok=True)

cap_monolith = cv2.VideoCapture("Monolith.mp4")
cap_witcher = cv2.VideoCapture("Witcher.mp4")
cap_objs = [cap_monolith, cap_witcher]

list_position = 1
cap_frame_number = 0

for cap_obj in cap_objs:

	if list_position == 1:
		subfolder_name = "monolith"
	elif list_position == 2:
		subfolder_name = "witcher"
	else:
		print("Error: Subfolder name not found!")

	print(f'\t{str(list_position)} - {subfolder_name}')

	while cap_obj.isOpened():
		ret, frame = cap_obj.read()

		if cap_frame_number % 10 == 0:
			target = str(f'{outputs}/{subfolder_name}/{cap_frame_number}.jpg')
			cv2.imwrite(target, frame)

		cap_frame_number += 1

		if (cap_frame_number > (60 * 30)):
			break

	cap_obj.release()
	print(f"Released VideoCapture object: {subfolder_name.capitalize()}")
	list_position += 1
	cap_frame_number = 0


print("Finished processing videos!")