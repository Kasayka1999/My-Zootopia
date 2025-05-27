
# 🐾 Animal Info Generator

This project fetches information about animals using the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates a static HTML file to display the data in a user-friendly format.

---

## 📌 Project Description

This tool allows users to input the name of an animal and receive structured data (like diet, habitat, and type) about it. It dynamically replaces a section of an HTML template with the fetched information and outputs a new HTML file (`animals.html`). If no data is found, the page shows a friendly message.

**Key Features:**
- Fetch data using API Ninjas
- Format and serialize animal data
- Generate visually structured HTML cards
- Fallback message if the animal is not found

---

## 🚀 Usage

### 1. Setup

Install dependencies and set up your environment.

```bash
pip install python-dotenv requests
```

Create a `.env` file in the root directory and add your API key:

```env
API_KEY=your_api_key_here
```

### 2. Run the Program

Execute the script:

```bash
python your_script_name.py
```

You'll be prompted to enter an animal name. The script fetches the data and generates an `animals.html` file.

### 3. View the Output

Open `animals.html` in a browser to see the formatted data.

---

## 🧩 Project Structure

```
project/
├── animals_template.html     # Your HTML template file with a placeholder
├── data_fetcher.py           # Handles API requests
├── main.py                   # Main logic: fetch, process, write
├── .env                      # Stores your API key securely
└── README.md                 # Project overview
```

---

## 🤝 Contributing Guidelines

Contributions are welcome! Here's how you can help:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Create a pull request.

Please follow clean code practices and include clear commit messages.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

For any suggestions or questions, feel free to reach out!
