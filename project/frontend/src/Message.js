import React from 'react';
import './Message.css'; 

const Message = ({ text, isUser }) => {
  return (
    <div className={`message ${isUser ? 'user-message' : 'chatgpt-message'}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;