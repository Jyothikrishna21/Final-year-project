import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for faster processing
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from the specified path.
        :param images_path: Path to images for encoding.
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            if img is None:
                print(f"Warning: Image at {img_path} could not be loaded.")
                continue

            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Get face encodings, handle potential errors
            face_encodings = face_recognition.face_encodings(rgb_img)
            if len(face_encodings) == 0:
                print(f"Warning: No faces found in image {img_path}.")
                continue

            # Store file name and file encoding
            self.known_face_encodings.append(face_encodings[0])
            self.known_face_names.append(filename)

        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        """
        Detect known faces in a given frame.
        :param frame: The frame in which to detect faces.
        :return: Locations and names of detected faces.
        """
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all faces and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"  # Default name for unmatched faces

            # Check for matches
            if True in matches:
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:  # If it's a match, assign the name
                    name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Adjust coordinates with frame resizing
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names

    def clean_up_temp_images(self, directory):
        """
        Clean up temporary images directory.
        :param directory: Path to the directory to clean.
        """
        try:
            if os.path.exists(directory):
                os.rmdir(directory)
                print(f"Temporary directory {directory} has been removed.")
            else:
                print(f"Temporary directory {directory} does not exist.")
        except Exception as e:
            print(f"Error while removing temporary directory: {e}")

# Usage example (make sure to implement it in your application):
if __name__ == "__main__":
    sfr = SimpleFacerec()
    
    # Assuming you have a method to fetch images and store them in a directory
    # Example: save_images_from_mongodb(getimages()) 
    sfr.load_encoding_images("path_to_your_image_folder")  # Specify your images path

    # To test detection, open your webcam or a video file
    cap = cv2.VideoCapture(0)  # Use 0 for the webcam, or replace with a video file path
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video")
            break

        face_locations, face_names = sfr.detect_known_faces(frame)

        # Display results (optional, you can customize how you show results)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Cleanup (if needed)
    sfr.clean_up_temp_images("temp_images")  # Adjust to your temp images folder if necessary
