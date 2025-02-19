# Attend-Me: Attendance Management System 🎯  

## 📌 Overview  
Attend-Me is a **Face Recognition-Based Attendance Management System** developed using **Python, OpenCV, and MySQL**. The system automates attendance marking by detecting and recognizing faces in real time, ensuring accuracy and efficiency. It eliminates the need for traditional manual attendance methods and provides a **secure, fast, and scalable** solution for schools, colleges, and workplaces.

## 🏗️ Features  
- ✅ **User Registration**: Register new users by storing their details in a MySQL database.  
- ✅ **Face Data Collection**: Capture **100 images** per user for model training.  
- ✅ **Face Recognition**: Recognize registered users using **Haar Cascade Algorithm** for real-time attendance marking.  
- ✅ **Automated Attendance Logging**: Store attendance records automatically in an **Excel sheet**.  
- ✅ **Editable Attendance**: Modify attendance records within the **Python application itself**.  

## 🛠️ Tech Stack  
- **Programming Language**: Python 🐍  
- **Image Processing**: OpenCV 🎥  
- **Database**: MySQL 🗄️  
- **Data Storage**: Excel (for attendance records) 📄  

## 🚀 Installation Guide  

### 1️⃣ Prerequisites  
Ensure you have the following installed on your system:  
- Python (>= 3.7)  
- MySQL  
- OpenCV  
- NumPy  
- Pandas  

### 2️⃣ Clone the Repository  
```sh
git clone https://github.com/prathamesh901/Attend-Me.git
cd Attend-Me

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt

### 4️⃣ Setup MySQL Database
```sh
CREATE DATABASE attendance_db;
mysql -u root -p attendance_db < database.sql
python main.py

📌 How It Works
📝 Step 1: User Registration
A new user registers by entering their details.
The system captures 100 images of the user for training.
📸 Step 2: Face Training
The collected images are trained using OpenCV's Haar Cascade Algorithm.
The trained model is stored for real-time recognition.
🔍 Step 3: Attendance Marking
When a registered user appears in front of the camera, their face is recognized, and attendance is marked automatically.
Attendance records are stored in an Excel sheet and can be edited within the app.

📊 Future Improvements
🔹 Enhance face recognition accuracy with Deep Learning (CNNs).
🔹 Implement Cloud Integration for remote access to attendance data.
🔹 Add QR Code-Based Attendance as an alternative method.
 
 
