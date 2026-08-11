✈️ TravelBot – AI-Powered Travel Planning Assistant

TravelBot is an AI-powered travel planning assistant built with Python, Streamlit, and the Groq API. It allows users to interact with a Large Language Model (LLM) through a conversational interface to explore destinations, plan trips, discover attractions, estimate travel budgets, and receive personalized travel recommendations.

The application uses prompt engineering and conversational context to generate structured and easy-to-understand travel plans based on the user's destination, requirements, duration, and number of travelers.

---

🌟 Features

🗺️ AI Travel Planning

Ask TravelBot natural-language questions such as:

- "Plan a 5-day trip to Goa."
- "What are the best places to visit in Kerala?"
- "Suggest attractions in Paris."
- "Give me a travel plan for Bali."
- "What is the estimated budget for 4 people?"

The AI generates a structured response based on the user's requirements.

📍 Destination Exploration

The application provides information about:

- Destination overview
- Popular attractions
- Best places to visit
- Recommended activities
- Local experiences
- Travel suggestions

🏨 Accommodation Recommendations

TravelBot can provide suggestions and information related to:

- Hotels
- Hostels
- Resorts
- Different accommodation categories
- Approximate accommodation costs

🍜 Food & Local Experiences

Users can ask about:

- Local cuisine
- Popular dishes
- Restaurants and food experiences
- Street food
- Local cultural experiences

🚗 Transportation Guidance

TravelBot can provide guidance regarding:

- Local transportation
- Inter-city travel
- Public transportation
- Taxi/cab options
- Approximate transportation costs

💰 Travel Budget Estimation

The application can generate estimated travel budgets based on:

- Destination
- Trip duration
- Number of travelers
- Accommodation
- Food
- Transportation
- Activities

Users can specify the number of travelers and receive a budget tailored to their group.

🤖 Multiple AI Models

TravelBot supports multiple LLM options available through Groq, allowing users to select a suitable model depending on their requirements.

💬 Conversational Memory

The application maintains the conversation during the current session.

For example:

User: Plan a trip to Goa.

Bot: [Provides Goa travel plan]

User: What about the budget?

Bot: [Provides budget based on the previous context]

This is implemented using Streamlit Session State.

⚡ Streaming Responses

AI responses are streamed progressively instead of waiting for the entire response to be generated.

This provides a more responsive conversational experience.

🔐 API Key Configuration

The application supports Groq API authentication.

For secure deployment, the API key should be stored using Streamlit Secrets rather than being hard-coded in the source code.

Example:

GROQ_API_KEY = "your_groq_api_key"

The secret should never be committed to GitHub.

📥 Save Conversation

Users can save their conversation as a text file for future reference.

📱 Responsive Interface

The application uses customized HTML and CSS along with Streamlit components to provide a responsive interface suitable for desktop and mobile screens.

---

🏗️ System Architecture

                 ┌─────────────────┐
                 │      User       │
                 └────────┬────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Streamlit Web UI  │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ User Travel Query │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Session State &   │
                │ Conversation      │
                │ History           │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │  System Prompt &  │
                │ Prompt Engineering│
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │     Groq API      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Selected LLM      │
                │ Llama / Gemma /   │
                │ Mixtral            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Generated Travel  │
                │ Recommendations   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Streaming Output  │
                │ to User           │
                └───────────────────┘

---

🔄 Application Workflow

1. The user opens the TravelBot application.
2. The application initializes the Streamlit interface.
3. The user provides a Groq API key if required.
4. The user selects an AI model and travel preferences.
5. The user enters a travel-related question.
6. The application stores the conversation in Streamlit Session State.
7. The system prompt provides instructions to the LLM about how the response should be generated.
8. The query, system instructions, and conversation history are sent to the Groq API.
9. The selected LLM processes the request.
10. The generated response is streamed back to the application.
11. Travel information is displayed in a structured format.
12. The conversation can be continued or saved as a text file.

---

🧠 Prompt Engineering

Prompt engineering is an important component of TravelBot.

Instead of simply sending the user's question to the LLM, the application provides system-level instructions that guide the model to generate structured travel information.

The response can be organized into sections such as:

1. Destination Overview
2. Top Attractions
3. Accommodation
4. Food & Local Experience
5. Transportation
6. Estimated Budget
7. Useful Links

The system prompt can also provide information such as the number of travelers, allowing the generated response to be tailored to group travel.

---

🛠️ Technologies Used

Technology| Purpose
Python| Core application development
Streamlit| Web interface and application framework
Groq API| LLM API integration
Llama / Gemma / Mixtral| AI-powered response generation
Streamlit Session State| Conversation and session management
HTML| UI customization
CSS| Styling and responsive design
Markdown| Structured response formatting
datetime| Timestamp generation and saved conversation filenames

---

📁 Project Structure

Travelbot/
│
├── travel_chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml    # Local only - DO NOT upload

---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/PavanKumar1124/Travelbot.git

cd Travelbot

2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

---

🔑 API Key Configuration

Create the following directory:

.streamlit/

Inside it create:

secrets.toml

Add:

GROQ_API_KEY = "your_groq_api_key"

Your ".gitignore" should contain:

.streamlit/secrets.toml
.env
__pycache__/
*.pyc
venv/
.venv/

Never commit your actual API key to GitHub.

For deployment, configure "GROQ_API_KEY" using the hosting platform's secret-management system.

---

▶️ Running the Application

Start the Streamlit application:

streamlit run travel_chatbot.py

The application will open in your browser.

---

💡 Example Queries

Try questions such as:

Plan a 5-day trip to Goa.

What are the best places to visit in Kerala?

Suggest attractions in Paris.

Plan a trip to Bali for 4 people.

Give me an estimated budget for a 7-day trip to Dubai.

What food should I try in Rajasthan?

How can I travel around Kyoto?

---

🔐 Security Considerations

API keys are sensitive credentials and should not be stored directly in source code.

❌ Do NOT do this:

api_key = "gsk_xxxxxxxxxxxxxxxxx"

✅ Use secret management:

api_key = st.secrets["GROQ_API_KEY"]

And add the secret file to ".gitignore".

If an API key is accidentally committed to a public repository, it should be revoked immediately and replaced with a new key.

---

⚠️ Limitations

The current version primarily uses an LLM to generate travel recommendations. Therefore:

- Flight prices are not guaranteed to be real-time.
- Hotel prices and availability are not guaranteed to be live.
- Generated budget figures are estimates.
- The application is not a direct booking platform.
- AI-generated information should be verified before making actual travel or financial decisions.
- An API key is required to communicate with the Groq service.

---

🚀 Future Enhancements

Possible future improvements include:

- 🌐 Real-time Google Maps integration
- ✈️ Real-time flight APIs
- 🏨 Hotel booking APIs
- 🌦️ Weather API integration
- 📍 GPS-based nearby-place recommendations
- 🗄️ Database integration for storing user trips
- 👤 User authentication
- 📊 Personalized recommendation systems
- 🗺️ Interactive maps
- 📱 Mobile application
- 🌍 Multi-language support
- 💳 Actual travel booking integration
- 🔒 Production-grade server-side secret management

---

🎯 Project Objectives

The major objectives of TravelBot are:

1. Simplify travel planning using conversational AI.
2. Generate personalized travel recommendations.
3. Provide structured destination information.
4. Estimate travel expenses based on group size.
5. Maintain conversational context.
6. Provide a simple and interactive user interface.
7. Demonstrate practical integration of an LLM API into a Python application.

---

👨‍💻 Skills Demonstrated

This project demonstrates practical experience in:

- Python Programming
- Generative AI
- Large Language Models
- API Integration
- Prompt Engineering
- Conversational AI
- Streamlit Application Development
- Session State Management
- Error Handling
- HTML/CSS
- Responsive UI Design
- Git & GitHub
- Secret/API-Key Management

---

📌 Conclusion

TravelBot demonstrates how Generative AI and LLM APIs can be integrated into a practical real-world application.

The project combines a Python-based Streamlit interface with the Groq API to create a conversational travel assistant capable of generating destination information, travel plans, recommendations and estimated budgets.

The project can be further expanded by integrating real-time travel services, maps, weather information, booking APIs and persistent user accounts, transforming it from an AI travel assistant into a more complete travel-planning platform.

---

👤 Author

Pavan Kumar

GitHub:
https://github.com/PavanKumar1124

---

⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub!
