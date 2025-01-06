# **Hiring Assistant Chatbot**

This is a **Hiring Assistant Chatbot** built using **Streamlit**, **Google Gemini AI**, and **MongoDB**. The chatbot collects user details, asks technical questions based on the user's tech stack, evaluates their responses, and stores the results in a MongoDB database.

---

## **Prerequisites**

### **1. Python Libraries**
Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### **2. Environment Variables**
Set up a `.env` file in the root of the project directory with the following keys:

```plaintext
GEMINI_API_KEY=<your_google_gemini_api_key>
MONGODB_URI=<your_mongodb_connection_uri>
```

### **3. MongoDB Atlas**
Ensure you have a **MongoDB Atlas** account or a local MongoDB setup. Create a database named `hiringassistant` with a collection named `users`.

---

## **How to Run the Application**

### **Step 1: Clone the Repository**
Clone the project repository to your local machine:

```bash
git clone https://github.com/Rohit131313/HiringAssistant.git
cd HiringAssistant
```

### **Step 2: Install Required Libraries**
If you haven’t already installed the required libraries, you can install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **Step 3: Start the Streamlit Application**
Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

### **Step 4: Interact with the Chatbot**
Once the app is running, open the URL provided by Streamlit (typically `http://localhost:8501`) in your web browser. Interact with the chatbot through the user-friendly web interface.

---

## **Features**

1. **User Information Collection**: Collects user details such as name, email, phone number, tech stack, and more.
2. **Technical Question Round**: Generates tricky technical questions based on the user’s provided tech stack.
3. **Response Evaluation**: Evaluates user answers and provides feedback on correctness.
4. **Score Tracking**: Tracks the number of correct answers and returns the score at the end.
5. **MongoDB Integration**: Stores user responses and scores securely in a MongoDB database.

---

## **Project Structure**

```plaintext
📂 Project Directory
├── app.py           # Main Python script for the chatbot
├── .env                    # Environment variables file
├── requirements.txt        # Required Python libraries
└── README.md               # Documentation
```

---

## **Technologies Used**
- **Python**: Backend logic and integration.
- **Streamlit**: Web-based user interface.
- **Google Gemini AI**: AI model for generating questions and responses.
- **MongoDB**: Database for storing user data and scores.
- **dotenv**: For secure management of environment variables.

---

## **Future Enhancements**
- Add support for additional AI models.
- Include more advanced reporting and analytics.
- Implement multi-user login functionality for better user management.
