# 💡 Honeywell Generative AI Project 💡
Monitoring industrial plant or organization processes are complicated, and finding a single reference document amongst gigabytes of data with traditional indexing methods can be tricky. Having engineers be able to interface with a Large Language Model to parse and collect this data would provide a huge productivity boost, and this project aims to develop such an application.

## 🔖 Readme Contents
- [Installation Guide](https://github.gatech.edu/JIB-3315/JIB-3315_GenAIProject/edit/main/README.md#-installation-guide)
- [Release Notes](https://github.gatech.edu/JIB-3315/JIB-3315_GenAIProject/edit/main/README.md#-release-notes)

## 💾 Installation Guide
---
**💿 Pre-requisites**
---
### 📁 File Download
 * Please clone this repository to your local machine. You may do so following these instructions: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### 🎮 Frontend Software requirements
  * Windows: Download the installer from this website per your machine requirements: https://nodejs.org/en/download
  * MacOS: In your terminal, run the following command: `brew install node`
  * Linux (Ubuntu): Run `sudo apt update` and then `sudo apt install nodejs npm`

### ⌨️ Backend Software requirements
- There are two options to install all dependencies required. You can either use our conda virtual environment, or simply install all the dependencies from the requirements.txt file. Try both methods before reaching out for help! Installation via the requirements.txt file will generally lead to fewer issues. 
- Please see the [troubeshooting](https://github.gatech.edu/JIB-3315/JIB-3315_GenAIProject/edit/main/README.md#-troubleshooting) section below if you require any assistance!

### 🐍 Python Software
**1.  Python Installation:** If you already have Python installed on your machine, you can skip to Step #2. If not, please follow these instructions to install Python: 
- Windows: Run the downloaded installer. Ensure to check the box that says "Add Python to PATH" before clicking "Install Now". This step is crucial as it makes Python and pip accessible from the command line. https://www.python.org/downloads/
-  MacOS: Run the downloaded installer and follow the instructions. The installer typically handles all configuration settings including PATH adjustments.
-  Linux (Ubuntu): You probably already have Python installed!

**2. Option 1:** Requirements.txt-- Please recall that you can do EITHER step 2 or 3, please pick whichever one you prefer. 
   - Enter the directory of the Repository that you cloned. Once there, navigate to the `./project/backend` folder.
   - Then, run the following command in your terminal or command line: `pip install -r requirements.txt`

**3. Option 2:** Conda environment 
   - Install Anaconda or minconda from the Anaconda's official site if you don't already have it: https://docs.anaconda.com/free/miniconda/miniconda-install/
   - Open either CMD or Terminal, and navigate to the `./project/backend` folder. Run the following command `conda env create -f environment.yml`. 
   - Once that has finished running, run the following command to activate the environment `conda activate honeywellenv`.

### 👨‍💻 Local Database Setup _**Note-- Required for Responses to Function_
**1. Install PostgreSQL:** You can download and install PostgreSQL from the official PostgreSQL website linked here: https://www.postgresql.org/download/. During the installation process, remember your PostgreSQL username and password. Do NOT install using Homebrew.

**2. pgAdmin:** After installing PostgreSQL, install pgAdmin, which is a popular open-source administration and development platform for PostgreSQL. Download it from the pgAdmin website linked here: https://www.pgadmin.org/download/ and follow the configuration instructions.

**3. Set up DB:** Open your terminal or cmd. Navigate to the `/.project/backend` folder. Run the following command `psql -U jib -d chatbot -f chatbot.sql`. Then, enter the password `3315`. _Note: This only needs to be done on first installation_

**📱 Running the Application**
---
* Run Fast-API server:** Open your terminal or cmd. Navigate to the `/.project/backend` folder. Run the following command `uvicorn main:app --reload`. You can go to http://localhost:8000/docs#/default/home__get to see the Fast-API UI.
* In the main directory, there is a file titled `start_project.py`
* If all installations were able to execute, you should be able to run the command `python start_project.py` in your CMD or Terminal, and the React application will open in your default web browser at 127.0.0.1!
* Please see the troubleshooting guide below if there are any issues.

**🔌 Troubleshooting**
---
## 🚀 Application Won't Start

### Python Script Errors
- Make sure Python 3 is installed and properly added to your system’s PATH.
- Ensure you are using the command `python` for Windows or `python3` for MacOS/Linux to start the script.
- Verify that there are no syntax errors in the `start_project.py` file.

### Missing Modules
- If you get an ImportError, it means a Python module is missing. Make sure to run `pip install -r requirements.txt` within your virtual environment or install the necessary packages as per your `environment.yml`.

## 📦 Dependency Installation Issues

### requirements.txt
- Ensure that you're running `pip install -r requirements.txt` inside the virtual environment. If you’re not in a virtual environment, consider creating one to avoid conflicts.
- If an error occurs during package installation, it may be a compatibility issue. Check if the packages are compatible with your Python version.

### Conda Environment
- If you have trouble creating the Conda environment from the `environment.yml` file, ensure that Anaconda/Miniconda is installed and updated to the latest version.
- Check the environment.yml file for syntax errors or unsupported packages.

## 🗃 Local Database Setup Problems

### PostgreSQL Connection
- Confirm that PostgreSQL is running on your machine.
- If `psql` command is not recognized, ensure that PostgreSQL bin directory is added to your system’s PATH.
- If you see a connection error, double-check that the username and password are correct and match those set during PostgreSQL installation.
- Use these links: https://stackoverflow.com/questions/36155219/psql-command-not-found-mac, https://stackoverflow.com/questions/6790088/postgresql-bash-psql-command-not-found

### Database Script Execution
- Make sure you are in the correct directory (`./project/backend/db`) when you run the `psql -U username -d chatbot -f chatbot.sql` command.
- If you receive an error about missing files, verify that `chatbot.sql` exists in the directory.

### Setting Up User and Database in pgAdmin for Authentication Issues
If you are facing repetitive authentication issues, setting up a dedicated user and database might help. Here’s how to create a user named jib with a password 3315 and set up a database for it in pgAdmin:

#### Create a New Role:
1. Open pgAdmin and connect to your PostgreSQL server.
2. Right-click on "Login/Group Roles" and select "Create" -> "Login/Group Role".
3. Name the role `jib`.
4. In the "Definition" tab, set the password to `3315`.
5. In the "Privileges" tab, set "Can login?" to "Yes".

#### Create a Database:
1. Right-click on "Databases" and select "Create" -> "Database".
2. Name the database `chatbot`.
3. Set the owner to the previously created `jib` role.'

#### Configure Authentication:
* Ensure that the pg_hba.conf file (located in the PostgreSQL installation directory) is configured to allow the jib user to connect with the correct authentication method (e.g., MD5).

## 🖼 Frontend Issues

### npm Dependencies
- If npm dependencies fail to install, make sure you have Node.js installed and that npm is up to date.
- Check for errors in the console output — they often provide clues about what went wrong.

### React Server
- If the React server won’t start, ensure that you are in the correct directory and that all npm dependencies are installed.
- Sometimes, the problem can be with a specific npm package. Try deleting the `node_modules` folder and the `package-lock.json` file and run `npm install` again.

## 🌐 Web Browser Issues

### Application Not Loading
- Ensure that no other services are running on the same port and that your firewall settings are not blocking the ports.
- Check the terminal for any errors indicating that the servers did not start correctly.
- If the application opens but does not function as expected, clear your browser cache and cookies, or try using a different browser.

## 🐞 General Debugging Steps

- Always read error messages carefully; they usually contain useful information about what went wrong.
- Check the console or terminal for stack traces or error logs that can point to the source of the issue.
- Ensure all environment variables and paths are set correctly.
- Restart your computer to resolve issues with ports or background processes that may affect the application.

---

If you continue to experience issues after following these steps, please feel free to contact our team via our shared Teams channel or by our gatech emails.

## 👾 Release Notes
___
### Version 1.0.0

#### Primary Features
* Left-side Chat History and new chat button
* Reset Chat Button
* Input text box for users to input queries
* Fully functional backend Fast-API server connected to Llama API
* Llama API consistently returns responses
* Query response placement mirrors conventional LLM applications
* Increased padding in key areas and rounded corners for boxes
* PostgreSQL database is setup correctly and can potentially be used to store PDFs or queries
* 4 inital prompts which users can choose from
* Chatbot knows it is a Honeywell bot and not a general chatbot
* PDF integration is fully implemented
* Chatbot can analyze and respond to queries about an uploaded PDF
* Chatbot is able to generate incident reports about specific pumps
* Chatbot can generate maintenace checklists for pumps

### New Features
* PDFs can now be uploaded to chatbot
* Chatbot is able to analyze PDFs and answer questions about information in the PDF
* Status of PDF upload is fully viewable from frontend UI

#### Bug Fixes from last developmental release 0.4.0
* Revamped frontend so inital prompts don't disappear without a user input
* Fixed Llama backend bug where chat responses were not coming through due to Streaming implementation attempt
* Resolved the " character over ' character issue

#### Known Issues
* Chat history is not persistent across reloads
* Latency on responses is still quite high
___
### Version 0.4.0

#### New Features
* FastAPI backend is now fully implemented

#### Bug Fixes
* Modified issue where responses are sometimes heavily geared towards recall over fresh answers
* Message bubble is fixed, and flow is visually intuitive

#### Known Issues
* Still wasn't able to resolve " character over ' character issue
* Latency on responses is still quite high
___
### Version 0.3.0

#### New Features
* Front and Back end technologies are fully integrated, allowing full communication with LLM through web interface
* Final major UI changes have been implemented, in line with Honeywell design requirements
* LLM 'Honeywell Chatbot' prompt has been implemented
* LLM now has memory, remembering past data across queries

#### Bug Fixes
* LLM responses are now visible from the website, rather than just in terminal
* Responses are correctly placed on screen

#### Known Issues
* Responses are sometimes heavily geared towards recall over fresh answers
* Incorrect usage of " character over ' character
___
### Version 0.2.0

#### New Features
* Soft launched more advanced LLM (Llama), connected through API. 
  * Basic Prompting and context provided
  * Responses are cogent
* Revamped UI/UX Features
  * Chat history stays persistent when refreshing the page
  * Added a delete chat buttom to each chat in the chat history
  * Chat history shows first 6 words of a new chat's first query
* Backend Features
  * Connected a FastAPI server and PostgreSQL database to the react frontend
  * Setup the UI for FastAPI to see outgoing and incoming requests from react

#### Bug Fixes
* Previous LLM caused major response hallucination, new one lacks such responses

#### Known Issues
* LLM integration still in production, can be tested in terminal but not connected to front end
* LLM lacks memory at the moment, in future may maintain memory through LangChain feature
___
### Version 0.1.0

#### New Features
* Revamped UI/UX Features
  * New left-side Chat History and new chat button
  * New Reset Chat Button
  * Modified input text box
  * More intuitive text box relative location
  * Response placement mirrors conventional LLM applications
  * Fonts align closer with Official Honeywell Fonts
  * Increased padding in key areas and rounded corners for boxes
* New lightweight LLM used (DialoGPT)
* More intuitive way to start all project elements. No more needing to navigate into different directories and running various commands!

#### Bug Fixes
N/A

#### Known Issues
* With new UI elements, user entered queries are displayed out of view, and LLM responses are temporarily suppressed.
* Input bar doesn't scale appropriately based on changing window size
* Saved previous chat history not developed at the moment, only placeholder feature developed.
___

