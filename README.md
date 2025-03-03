Face Recognition - Missing Person Detection System

📌 Project Overview

Face Recognition is a missing person detection system developed using the MERN (MongoDB, Express.js, React.js, Node.js) stack. This project aims to help families reunite with their missing loved ones by leveraging deep learning techniques. The system detects faces using a Recurrent Neural Network (RNN) and matches them with registered cases in the database.

🔍 How It Works

Case Registration: The family of the missing person registers a case by providing details and an image.

Database Storage: The details and image are stored in the MongoDB database.

Feature Extraction: The system extracts facial features using the RNN algorithm.

Face Matching: When a new face is detected, the system compares it with the stored images.

Location Tracking: If a match is found, the recent location of the detected person is displayed.

🛠️ Tech Stack

Frontend: React.js, HTML, CSS, JavaScript, Bootstrap

Backend: Node.js, Express.js

Database: MongoDB

Face Recognition Algorithm: RNN (Recurrent Neural Network)

Additional Tools: OpenCV, Cloudinary (for image storage)

🚀 Features

Secure user authentication and case management

Image storage and retrieval using Cloudinary

Real-time face detection and matching

Location tracking of detected persons

Responsive and user-friendly UI

🏗️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/Jyothikrishna21/Final-year-project.git
cd Final-year-project

2️⃣ Install Dependencies

# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install

3️⃣ Configure Environment Variables

4️⃣ Start the Application

# Start backend server
cd backend
npm start

# Start frontend server
cd ../frontend
npm start

🖼️ Demo

[Provide a link to the deployed project or screenshots]

📧 Contact

For any queries, feel free to reach out:

Email: jyothikrishnaavutu@gmail.com

GitHub: Jyothikrishna21

📜 License

This project is licensed under the MIT License.

