import React, { useState , useRef, useEffect} from 'react';
import axios from 'axios';
import Message from './Message';
import './App.css';

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [chatSessions, setChatSessions] = useState({});
  const [selectedSession, setSelectedSession] = useState(null);
  const [isPendingSession, setIsPendingSession] = useState(false);
  const [showInitialMessage, setShowInitialMessage] = useState(true);
  const [selectedPrompt, setSelectedPrompt] = useState('');
  const [file, setFile] = useState(null);
  const initialPrompts = ['Generate an incident report', 'Run a system check', 'Explain why popcorn pops at Honeywell', 'Discuss Honeywell stocks'];
  const [showPrompts, setShowPrompts] = useState(true);
  const [fileName, setFileName] = useState('');
  const [uploadStatus, setUploadStatus] = useState('');

  //Changes file to be given to LLM
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setFileName(event.target.files[0].name);
  };

  //Handles file upload
  const uploadFile = async () => {
    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      setUploadStatus('Uploading...');
  
      try {
        const response = await axios.post('http://localhost:8000/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          onUploadProgress: progressEvent => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            setUploadStatus(`Uploading... ${percentCompleted}%`);
          }
        });
        setUploadStatus('File successfully uploaded');
      } catch (error) {
        setUploadStatus('Failed to upload file');
      }
    }
  };
  

  //Handles new chat session on load
  useEffect(() => {
    setInput('')
    startNewChatSession();
    const savedChatSessions = localStorage.getItem('chatSessions');
    if (savedChatSessions) {
        setChatSessions(JSON.parse(savedChatSessions));
    }

    const currentSessionName = localStorage.getItem('currentSessionName');
    if (currentSessionName && JSON.parse(savedChatSessions)?.hasOwnProperty(currentSessionName)) {
        setSelectedSession(currentSessionName);
    }
  }, []);

  //Handles new chat session
  const startNewChatSession = () => {
    setMessages([]);
    setIsPendingSession(true);
  };

  //Handles selection of chat sessions
  useEffect(() => {
      if (selectedSession) {
          const sessionMessages = chatSessions[selectedSession] || [];
          setMessages(sessionMessages);
      }
  }, [selectedSession, chatSessions]);

  //Handles saving of messages to the session
  const saveMessageToSession = (newMessage, sessionName) => {
    const targetSessionName = sessionName || selectedSession;
  
    const updatedSessions = {
      ...chatSessions,
      [targetSessionName]: [...(chatSessions[targetSessionName] || []), newMessage]
    };
    
    setChatSessions(updatedSessions);
    localStorage.setItem('chatSessions', JSON.stringify(updatedSessions));
  };

  //Handles sending of query to llm and the response
  const sendChatMessage = async (inputText) => {
    let currentSessionName = selectedSession;
    
    if (isPendingSession) {
      const newSessionName = inputText.substring(0, 30);
      currentSessionName = newSessionName; 

      setChatSessions(prevSessions => ({
        ...prevSessions,
        [newSessionName]: [{ text: inputText, isUser: true }]
      }));

      setSelectedSession(newSessionName);
      setIsPendingSession(false);
      localStorage.setItem('currentSessionName', newSessionName); 

      const userMessage = { text: inputText, isUser: true };
      //sets messages if there are previous sessions
      setMessages(prevMessages => {
        const updatedMessages = [...prevMessages, userMessage];
        return updatedMessages;
      }, () => saveMessageToSession(userMessage, currentSessionName));
    } else {
      const userMessage = { text: inputText, isUser: true };
      //sets messages if there are not previous sessions
      //Need to fix chat history bug here
      setMessages(prevMessages => {
        const updatedMessages = [...prevMessages, userMessage];
        return updatedMessages;
      }, () => saveMessageToSession(userMessage, currentSessionName));
    }

    try {
      const response = await axios.post('http://localhost:8000/query/', { query: inputText });
      const botMessage = { text: response.data.response, isUser: false };
      setMessages(prevMessages => {
        const updatedMessages = [...prevMessages, botMessage];
        return updatedMessages;
      }, () => saveMessageToSession(botMessage, currentSessionName)); 
    } catch (error) {
        console.error("Error sending chat message: ", error);
    } 

  };

  //sending of message
  const sendMessage = async (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
        setInput('');
        setShowInitialMessage(false);
        await sendChatMessage(input);
        setShowPrompts(false);  // Ensure prompts are hidden after sending message
    }
  };

  const selectChatSession = (sessionName) => {
    setSelectedSession(sessionName);
  };

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  //Handles automatic scrolling to bottom of chat window
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  //Handles deletion of chat session
  const deleteChatSession = (e, sessionName) => {
    e.stopPropagation();
    const updatedSessions = {...chatSessions};
    delete updatedSessions[sessionName];
    setChatSessions(updatedSessions);
    localStorage.setItem('chatSessions', JSON.stringify(updatedSessions));
    if (selectedSession === sessionName) {
        setSelectedSession(null);
        setMessages([]);
    }
  };

  // useEffect(() => {
  //   const timer = setTimeout(() => {
  //     setShowInitialMessage(false);
  //   }, 8000);
  
  //   return () => clearTimeout(timer);
  // }, []);

  //Prompt selection
  const handlePromptSelection = async (prompt) => {
    setInput(prompt);
    setShowInitialMessage(false);
    setShowPrompts(false);  // Ensure prompts are hidden after selecting a prompt
    setInput('');
    await sendChatMessage(prompt);
  };

  return (
    <div className="app-container">
      {showInitialMessage && (
      <div className="centeredMessage">How can I help you today?</div>)}
      <header className="App-header">
        <h1>Honeywell Chatbot</h1>
      </header>
      <div className="chatbot-functions">
        <div className="sidebar">
          <h2>Chat History</h2>
          <button onClick={startNewChatSession} className="new-message-btn">New Message</button>
          {Object.keys(chatSessions).reverse().map((sessionName) => (
              <div key={sessionName} className="panel-text session-item">
                  <p onClick={() => selectChatSession(sessionName)}>{sessionName}</p>
                  <button 
                      className="delete-session-btn" 
                      onClick={(e) => deleteChatSession(e, sessionName)}
                  >
                      Delete
                  </button> 
              </div>
          ))}
        </div>
        <div className="chat-container">
        <div className="prompts-container"
             style={{ marginTop: showPrompts ? '480px' : '0px' }}
        >
        {showPrompts && initialPrompts.map((prompt, index) => (
          <div key={index} className="promptOption" onClick={() => handlePromptSelection(prompt)}>
            {prompt}
          </div>
        ))}
      </div>
          <div className="messages-list">
            {messages.map((message) => (
              <Message isUser={message.isUser} text={message.text} />
            ))}
            <div ref={messagesEndRef} />
          </div>
          {fileName && (
            <div className="uploaded-file-name">
              {fileName}
            </div>
          )}
        <div className="upload-status">
          <div className={uploadStatus.includes('successfully') ? 'success' : uploadStatus.includes('Failed') ? 'error' : ''}>
            {uploadStatus.includes('successfully') && '✅'}
            {uploadStatus.includes('Failed') && '❌'}
            {uploadStatus}
          </div>
        </div>

          <form onSubmit={sendMessage} className="message-form">
          <input
            className="message-input"
            value={input}
            onChange={(e) => {
              setInput(e.target.value);
              if (showPrompts) {
                setShowPrompts(false);  // This will hide the prompts as soon as user starts typing
              }
            }}
            type="text"
            placeholder="Type your message here..."
          />
            <button className="send-button" type="submit">Send</button>
            <label htmlFor="file-input" className="file-input-label">Choose File</label>
            <input type="file" accept="application/pdf" onChange={handleFileChange} id="file-input" className="file-input" />
            <button className="upload-pdf-button" onClick={uploadFile}>Upload PDF</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default App;