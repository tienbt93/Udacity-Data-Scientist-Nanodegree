
# Recommendations with IBM

## Table of Contents
1. [Installations](#installations)
2. [Project Motivation](#project-motivation)
3. [File Structure](#file-descriptions)
4. [Contributing](#contributing)
5. [License](#licensing-authors-acknowledgements-etc)

## Installations

To set up the environment for this project, follow these steps:

### Step 1: Create a Virtual Environment
First, create a virtual environment to manage project dependencies. Open your terminal and run the following command:

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment
Activate the virtual environment. Depending on your operating system, use one of the following commands:

- **For Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **For macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Once the virtual environment is activated, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

## Project Motivation

For this project I was interested in analysing the interactions that users have with articles on the IBM Watson Studio platform, and making recommendations to them about new articles they would like. The project was divided into the following tasks:

- Exploratory Data Analysis
- Rank Based Recommendations
- User-User Based Collaborative Filtering
- Matrix factorisation

## File Structure
```
Project 3/
│
├── data/
│   ├── articles_community.csv  # articles
│   ├── user-item-interactions.csv  # user item interactions data
│
├── Recommendations_with_IBM.ipynb # Jupyter notebook
│
├── requirements.txt
├── README.md
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
