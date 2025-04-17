# CompanyWise DSA Q&A

This project is a web application built with **Streamlit** that displays Data Structures and Algorithms (DSA) questions for different companies. The questions are dynamically loaded from CSV files and can be filtered by company, difficulty level, and search query. It also includes answers to questions, allowing users to view solutions for specific problems.

## Features

- Display company-specific DSA questions.
- Filter questions by difficulty (Easy, Medium, Hard).
- Search questions by name.
- View answers for questions (if available).
- Built with Streamlit for an interactive user experience.

## Tech Stack

- **Streamlit**: For building the web app interface.
- **Pandas**: For data manipulation and filtering.
- **Python 3.9**: Backend programming language.
- **Docker**: For containerization and easy deployment.

## Prerequisites

- **Docker** installed on your machine.
- **Python 3.9** or later (if not using Docker).

## Installation and Running the App

### 1. Clone the repository

```bash
git clone https://github.com/AyushKatre05/DSA-Questions-CompanyWise.git
cd DSA-Questions-CompanyWise
```

## Building the Docker Image


###  2. Build the Docker Image

Navigate to the root directory of the project and run the following command to build the Docker image:

```bash
docker build -t leetcode-dsa-app .
```

Once you have successfully built the Docker image, you can run the application inside a Docker container. 

### 3. Run the Docker Container

To run the application, use the following command:

```bash
docker run -p 8501:8501 leetcode-dsa-app:latest 
```

### 4. Accessing the Application

Once you have successfully built and run the Docker container for the **CompanyWise DSA Q&A** app, follow the steps below to access the application:

### Open Your Browser

After the Docker container is running, open your web browser of choice.

## Navigate to the App URL

In the browser, enter the following URL to access the app:

```bash
 http://localhost:8501
```

## 5. Interact with the App

Once the app is loaded, you will be able to:

- **Select a Company**: Choose from a list of companies to see the DSA questions asked by that company.
- **Filter by Difficulty**: Use the filter options to narrow down the questions based on difficulty (Easy, Medium, Hard).
- **Search Questions**: Enter a question name or keyword in the search bar to find specific questions.
- **View Question Details**: Click on any question to see its details like acceptance rate, frequency, and a link to the LeetCode problem.
- **Solution Display**: If available, the solution to the question will be shown below its details.


## How to use:
1. Save this content in a file named `ACCESS_APP.md`.
2. Place it in your project repository so users can access detailed instructions on how to open and use the app once it's running in Docker.

This guide helps users access the application after the Docker container is up and running, offering basic troubleshooting steps in case of issues.
