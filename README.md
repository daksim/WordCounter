# Word Counter Web App

A simple web application to count the number of words in a given English text. Words connected with hyphens (e.g., "mother-in-law") are counted as a single word, and punctuation marks are ignored.

## Installation

### Prerequisites

- Python 3.8 or higher

### Steps

1. Clone this repository:

   ```shell
   git clone https://github.com/daksim/WordCounter.git
   cd WordCounter
   ```

2. Install dependencies:

   ```bash
   pip install flask
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`.

------

## Usage

1. Enter or paste your text into the text area.
2. The word count will be displayed in real-time below the text area.
3. Words connected by hyphens (e.g., `mother-in-law`) are counted as one word.
4. Punctuation marks are ignored in the word count.

## **Examples of Word Counting**

| Input Text                           | Word Count |
| ------------------------------------ | ---------- |
| `Hello, world!`                      | 2          |
| `Let's count words correctly!`       | 4          |
| `mother-in-law's advice is helpful.` | 4          |
| `I'm testing this regex now.`        | 5          |

