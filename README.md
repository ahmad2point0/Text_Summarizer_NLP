<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Summarizer Project</title>
</head>
<body>
    <h1>Text Summarizer Project</h1>
    <p>This project is a simple web application that summarizes raw text using natural language processing techniques. The application is built using Flask and Spacy.</p>

    <h2>How to Run the Project</h2>
    <ol>
        <li>Install Dependencies: Make sure you have Python installed. Then, install the required dependencies using pip:
            <pre><code>pip install flask spacy
python -m spacy download en_core_web_lg</code></pre>
        </li>
        <li>Run the Application: Navigate to the project directory and run the Flask application:
            <pre><code>python app.py</code></pre>
        </li>
        <li>Access the Application: Open your web browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to access the Text Summarizer application.</li>
    </ol>

    <h2>How to Use the Application</h2>
    <p>Enter Raw Text: In the "Enter Text" field, input the text you want to summarize. For example:</p>
    <blockquote>
        <p>Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the fifth-most populous country, with a population of over 241.5 million, having the second-largest Muslim population as of 2023. Islamabad is the nation's capital, while Karachi is its largest city and financial centre. Pakistan is the 33rd-largest country by area. Bounded by the Arabian Sea on the south, the Gulf of Oman on the southwest, and the Sir Creek on the southeast, it shares land borders with India to the east; Afghanistan to the west; Iran to the southwest; and China to the northeast. It shares a maritime border with Oman in the Gulf of Oman, and is separated from Tajikistan in the northwest by Afghanistan's narrow Wakhan Corridor. Pakistan is the site of several ancient cultures, including the 8,500-year-old Neolithic site of Mehrgarh in Balochistan, the Indus Valley Civilisation of the Bronze Age, and the ancient Gandhara civilisation. The regions that compose the modern state of Pakistan were the realm of multiple empires and dynasties, including the Achaemenid, the Maurya, the Kushan, the Gupta; the Umayyad Caliphate in its southern regions, the Hindu Shahis, the Ghaznavids, the Delhi Sultanate, the Samma, the Shah Miris, the Mughals, and most recently, the British Raj from 1858 to 1947. Spurred by the Pakistan Movement, which sought a homeland for the Muslims of British India, and election victories in 1946 by the All-India Muslim League, Pakistan gained independence in 1947 after the Partition of the British Indian Empire, which awarded separate statehood to its Muslim-majority regions and was accompanied by an unparalleled mass migration and loss of life. Initially a Dominion of the British Commonwealth, Pakistan officially drafted its constitution in 1956, and emerged as a declared Islamic republic. In 1971, the exclave of East Pakistan seceded as the new country of Bangladesh after a nine-month-long civil war. In the following four decades, Pakistan has been ruled by governments whose descriptions, although complex, commonly alternated between civilian and military, democratic and authoritarian, relatively secular and Islamist. Pakistan is considered a middle power nation, with the world's sixth-largest standing armed forces. It is a declared nuclear-weapons state, and is ranked amongst the emerging and growth-leading economies, with a large and rapidly growing middle class. Pakistan's political history since independence has been characterized by periods of significant economic and military growth as well as those of political and economic instability. It is an ethnically and linguistically diverse country, with similarly diverse geography and wildlife. The country continues to face challenges, including poverty, illiteracy, corruption, and terrorism. Pakistan is a member of the United Nations, the Shanghai Cooperation Organisation, the Organisation of Islamic Cooperation, the Commonwealth of Nations, the South Asian Association for Regional Cooperation, and the Islamic Military Counter-Terrorism Coalition, and is designated as a major non-NATO ally by the United States.</p>
    </blockquote>

    <h2>Testing the Model</h2>
    <p>To test the summarization model, you can use the provided sample text or any other text of your choice. The application will display the original text, its length, the summary, and the length of the summary.</p>
</body>
</html>