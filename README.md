# 💬 E-commerce Chatbot (GenAI RAG Project using GROQ)

This is a POC (Proof of Concept) of an intelligent e-commerce chatbot built by **Santhosh Kumar**, designed to deliver real-time, context-aware responses to user queries using **Retrieval Augmented Generation (RAG)** powered by **GROQ's LLM**.

It uses **semantic intent routing** via the `semantic-router` library to categorize queries into predefined routes like product search (SQL) or general support (FAQs), providing an efficient and accurate interaction experience.

---

## 🗂️ Folder Structure

```
e-commerce_chatbot/
├── app/              # Main chatbot code
│   ├── main.py
│   ├── faq.py
│   ├── sql.py
│   ├── router.py
│   └── resources/
│       ├── faq_data.csv
│       ├── ecommerce_data_final.csv
├── web-scraping/     # Jupyter notebook to scrape e-commerce data
│   └── flipkart_data_extraction.ipynb
├── requirements.txt  # Dependencies
└── .gitignore
```

---

## 🧠 Intent Routes Supported

The chatbot supports two major **intents**:

### 📘 1. FAQ Route
Use this to ask general questions about policy, delivery, payment, etc.

💬 Example questions:
- What is the return policy of the products?
- Do I get a discount with the HDFC credit card?
- How can I track my order?
- What payment methods are accepted?
- How long does it take to process a refund?

---

### 🛍️ 2. SQL/Product Query Route
Use this to explore the product catalog based on filters like brand, price, category, etc.

💬 Example questions:
- I want to buy Nike shoes with a 50% discount.
- Are there any shoes under ₹3000?
- Do you have formal shoes in size 9?
- Are there any Puma shoes on sale?
- Pink Puma shoes in price range 5000 to 1000

---

## 🛠️ Setup & Installation (Local)

### 1. 📦 Install dependencies
Make sure you're in the project folder and run:

```bash
pip install -r requirements.txt
```

### 2. 🔐 Create a `.env` file inside the `app/` directory:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile  # or whichever model you want
```

You can get your GROQ API key from: https://console.groq.com/keys

### 3. 🚀 Run the Streamlit app

```bash
streamlit run app/main.py
```

> The chatbot UI will open at http://localhost:8501 in your browser.

---



## 👨‍💻 Author

**Santhosh Kumar**    
Connect with me: [LinkedIn](www.linkedin.com/in/santhosh-kumar-9118932b2) 

---

## ⚖️ License

```
MIT License

Copyright (c) 2025 Santhosh Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software...

Commercial use is **not permitted without permission** from the author. Attribution required.
```




