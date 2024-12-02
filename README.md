
# Baymax-AI Personal Healthcare Companion
##https://baymax-v13.streamlit.app/

## Overview
Baymax-AI is a personal healthcare companion inspired by the character Baymax from Disney's *Big Hero 6*. This AI-driven application is designed to provide users with healthcare advice, emotional support, and health monitoring. Utilizing advanced natural language processing and machine learning techniques, Baymax-AI aims to assist users in managing their health and well-being in a compassionate and informative manner.

## Features
- **Conversational Interface**: Engage in natural conversations with Baymax, who responds in a calm and supportive tone.
- **Health Assessments**: Receive comprehensive health assessments and advice based on user input.
- **Emotional Support**: Get caring guidance and encouragement for emotional well-being.
- **Medical Recommendations**: Access healthcare recommendations and protocols tailored to user needs.
- **User-Friendly UI**: A visually appealing interface designed for ease of use.
- **Persistent Chat History**: Keep track of previous interactions for continuity in care.

## Installation
To set up the Baymax-AI Personal Healthcare Companion, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sandesh13fr/baymax-ai.git
   cd baymax-ai
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Download NLTK Data**:
   The application requires NLTK data for natural language processing. You can download it by running:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## Usage
To run the Baymax-AI application, execute the following command in your terminal:
```bash
streamlit run Pages/Baymax.py
```
This will start a local server, and you can access the application in your web browser at `http://localhost:8501`.

### Interacting with Baymax
- Type your health concerns or questions in the input box.
- Baymax will respond with healthcare advice, emotional support, or medical recommendations.
- Use the available commands to navigate through different healthcare protocols.

## Contribution
Contributions are welcome! If you would like to contribute to the Baymax-AI project, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the repository page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Implement your feature or fix the bug.
4. **Commit Your Changes**: 
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Branch**: 
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Create a Pull Request**: Go to the original repository and create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the character Baymax from Disney's *Big Hero 6*.
- Utilizes Groq API for advanced natural language processing capabilities.
- Thanks to the open-source community for their contributions and support.

---
