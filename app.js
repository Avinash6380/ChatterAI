const chatbotToggler = document.querySelector(".chatbot-toggler");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const logOutBtn = document.getElementsByClassName("log-out");

// function logOut(){
//     window.location.href = "login_page.html";
// }

let userMessage = null; // Variable to store user's message
 
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    // Create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return chat <li> element
}

const generateResponse = (chatElement) => {
    const API_URL = "http://localhost:5005/webhooks/rest/webhook";
    const messageElement = chatElement.querySelector("p");

    // Define the properties and message for the API request
    const requestOptions = {
        method: 'POST',
            body: JSON.stringify({
                message: userMessage }),
            mode: 'cors',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'charset':'UTF-8'
            },
    }

    // Send POST request to API, get response and set the reponse as paragraph text
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        console.log(data);
        messageElement.textContent = data[0].text;
        console.log(userMessage)
    }).catch(() => {
         messageElement.classList.add("error");
         messageElement.textContent = "Oops! Something went wrong. Please try again.";
     }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
    if(!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 600);
}
sendChatBtn.onclick = function(){
    handleChat();
}

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window 
    // width is greater than 800px, handle the chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

//<-------------------Responsive Menu------------------->

let menu = document.querySelector('.menu');
let leftList = document.querySelector('.left');
let closeBtn = document.querySelector('#close-Btn');

menu.onclick = function() {
    leftList.classList.add('active');

    //leftList.classList.toggle('active');
    console.log(leftList)
}
closeBtn.onclick = function () {
    leftList.classList.remove('active');
    console.log(leftList);
}

function feedback(){
    let feedback_icon = document.querySelector("material-symbols-outlined");
    console.log("Feedback Clicked")
    window.location.href = "feedback_index.html"
}



// Portfoilo 

function avinashPortfolio(){
    // window.location.href = "feedback_index.html";
    window.location.href = "/Avinash_Portfolio/index.html";
    console.log("Working");
}

function faheemPortfolio(){
    window.location.href = "/Faheem_Portfoilo/index.html";
    console.log("Working");
}

function azharPortfolio(){
    window.location.href = "/Azhar_Portfolio/index.html";
    console.log("Working");
}

function kameshPortfolio(){
    window.location.href = "/Kamesh_Portfolio/index.html";
    console.log("Working");
}

function roomanPortfolio(){
    window.location.href = "/Rooman_Portfolio/index.html";
    console.log("Working");
}


