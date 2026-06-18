const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS for frontend-backend communication
app.use(cors());

// Parse JSON and URL-encoded bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Endpoint to dynamically serve Supabase config keys to the frontend client.
// This prevents hardcoding API keys in static files and allows using .env configurations.
app.get('/config.js', (req, res) => {
  res.type('application/javascript');
  
  const supabaseUrl = process.env.SUPABASE_URL || '';
  const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || '';
  
  if (!supabaseUrl || !supabaseAnonKey || supabaseUrl === 'YOUR_SUPABASE_PROJECT_URL' || supabaseAnonKey === 'YOUR_SUPABASE_ANON_KEY') {
    console.warn('WARNING: Supabase credentials are not configured in your .env file!');
  }
  
  res.send(`
    // Supabase Configuration injected by Express server
    window.SUPABASE_URL = "${supabaseUrl}";
    window.SUPABASE_ANON_KEY = "${supabaseAnonKey}";
    console.log("Supabase config loaded successfully.");
  `);
});

// Serve all static files in the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Root route redirects to login page
app.get('/', (req, res) => {
  res.redirect('/login-page.html');
});

// Start the server
app.listen(PORT, () => {
  console.log(`===========================================================`);
  console.log(` ChatterAI Server is running at http://localhost:${PORT}`);
  console.log(` Open http://localhost:${PORT}/login-page.html to log in`);
  console.log(`===========================================================`);
});
