import streamlit as st
import cv2
import os
from simple_facerec import SimpleFacerec
import requests
from dateandwhatsapp import sendmessage
from getlocationinfo2 import getlocation

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Sidebar and UI Setup
st.sidebar.title('Face Recognition App to Find Missing People')
st.sidebar.subheader('Parameters')

sfr = SimpleFacerec()

# Specify your images path correctly
stored_images = "/Users/jyothikrishnareddy/Desktop/Face_recognition_Finding_missing_people-master/Node-js server MS/uploads" 

if stored_images is None or not isinstance(stored_images, str):
    raise ValueError("The stored_images path must be a valid string.")

if not os.path.exists(stored_images):
    raise FileNotFoundError(f"The specified path does not exist: {stored_images}")

print(f"Loading encoding images from: {stored_images}")
sfr.load_encoding_images(stored_images)

mylocation = getlocation()

processed_faces = set()

# Function to handle adding data to the database and sending a WhatsApp message
def add_in_base(a):
    idx = 0
    actual_name = ""
    adhaar = ""
    for i in range(len(a)-1, -1, -1):
        if a[i] == '_':
            idx = i
            break
    
    actual_name = a[:idx]
    adhaar = a[idx+1:]
    
    print(adhaar)
    print(actual_name)

    dataval = {
        "name": actual_name,
        "adhaar": adhaar,
        "locationval": mylocation
    }
    
    r = requests.post(url="http://localhost:3000/api/foundlocation/addlocation", json=dataval)
    print(r.text)
    
    newr = requests.get(url=f"http://localhost:3000/api/missingpeople/getallpersons/{adhaar}")
    newrdata = newr.json()
    
    if newrdata:
        print(newrdata[0]['phonenumber'])
        sendmessage(newrdata[0]['phonenumber'], actual_name, adhaar, mylocation)
    else:
        print("No matching person found in the database.")

if st.sidebar.button('Use Webcam'):
    st.session_state['webcam_active'] = True

if st.session_state.get('webcam_active'):
    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to capture video")
            break

        # Detect faces in the frame
        face_locations, face_names = sfr.detect_known_faces(frame)
        
        # Iterate through detected faces
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc

            # If no name is recognized, display "Unknown"
            if name is None or name == "":
                name = "Unknown"
            elif name not in processed_faces:
                processed_faces.add(name)
                add_in_base(name)

            # Display bounding box and name
            cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Display webcam frame in Streamlit
        new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(new_frame)

    cap.release()
    cv2.destroyAllWindows()
