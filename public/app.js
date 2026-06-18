const chatbotToggler = document.querySelector(".chatbot-toggler");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const logOutBtn = document.getElementsByClassName("log-out");

// Active logout function connected to Supabase AuthService
async function logOut() {
    try {
        await AuthService.signOut();
    } catch (err) {
        console.error("Error signing out:", err.message);
    }
    window.location.href = "login-page.html";
}

// Fetch user profile on load to update the welcome card with the username.
// Implements a self-healing check: if the profile record is missing from the database
// (e.g. first login after email confirmation), it automatically inserts it.
window.addEventListener('DOMContentLoaded', async () => {
    try {
        const session = await AuthService.getCurrentSession();
        if (session && session.user) {
            const user = session.user;
            senderId = user.id;
            let profile = null;
            
            try {
                profile = await AuthService.getUserProfile(user.id);
            } catch (err) {
                console.log("No database profile found for active session on load. Initializing profile sync...");
                const email = user.email;
                const provider = user.app_metadata?.provider || user.identities?.[0]?.provider || 'email';
                
                const profileData = {
                    id: user.id,
                    email: email,
                    provider: provider,
                    created_at: new Date().toISOString()
                };
                
                const sanitizeUsername = (name) => {
                    if (!name) return 'User';
                    let clean = name.replace(/[^A-Za-z0-9]/g, '');
                    if (!/^[A-Za-z]/.test(clean)) {
                        clean = 'U' + clean;
                    }
                    return clean || 'User';
                };

                if (provider === 'google') {
                    const fullName = user.user_metadata?.full_name || user.user_metadata?.name || null;
                    profileData.username = sanitizeUsername(fullName ? fullName : email.split('@')[0]);
                } else {
                    profileData.username = sanitizeUsername(user.user_metadata?.username || email.split('@')[0]);
                }
                
                const supabaseClient = window.supabase.createClient(window.SUPABASE_URL, window.SUPABASE_ANON_KEY);
                const { error: insertError } = await supabaseClient.from('profiles').insert([profileData]);
                
                if (insertError) {
                    console.error("Database self-healing insertion failed:", insertError.message);
                } else {
                    console.log("Database self-healing insertion successful.");
                    profile = profileData;
                }
            }
            
            // Format and set the username in the sidebar welcome section
            let usernameToDisplay = 'User';
            if (profile && profile.username) {
                usernameToDisplay = profile.username
                    .split(' ')
                    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(' ');
            }

            const sidebarUsername = document.getElementById('sidebar-username');
            if (sidebarUsername) {
                sidebarUsername.textContent = usernameToDisplay;
            }
            
            if (profile && profile.username) {
                const welcomeText = document.querySelector('.welcome_text');
                if (welcomeText) {
                    welcomeText.textContent = `Hey, Welcome Here ${usernameToDisplay} ❤️`;
                }
            }
        } else {
            const sidebarUsername = document.getElementById('sidebar-username');
            if (sidebarUsername) {
                sidebarUsername.textContent = 'User';
            }
        }
    } catch (err) {
        console.error("Could not sync or fetch user profile on load:", err.message);
        const sidebarUsername = document.getElementById('sidebar-username');
        if (sidebarUsername) {
            sidebarUsername.textContent = 'User';
        }
    }
});

let userMessage = null; // Variable to store user's message
let senderId = "user"; // Default sender ID for Rasa conversation tracking
 
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
            sender: senderId,
            message: userMessage 
        }),
        mode: 'cors',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'charset':'UTF-8'
        },
    }

    // Send POST request to API, get response and set the response as paragraph text
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        console.log(data);
        if (data && data.length > 0) {
            // First message replaces the "Thinking..." placeholder
            messageElement.textContent = data[0].text || "";
            
            // Append any subsequent messages
            for (let i = 1  ; i < data.length; i++) {
                if (data[i].text) {
                    chatbox.appendChild(createChatLi(data[i].text, "incoming"));
                }
            }
//             console.log("Response:", data);
// console.log("Length:", data.length);
        } else {
            messageElement.textContent = "I received an empty response from the assistant.";
        }
        console.log(userMessage)
    }).catch((error) => {
         console.error("Error connecting to Rasa:", error);
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


