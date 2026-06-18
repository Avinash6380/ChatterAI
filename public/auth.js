// =========================================================================
// Supabase Frontend Authentication Service Helper
// =========================================================================

let _supabaseInstance = null;

// Initialize Supabase client
function initSupabase() {
  if (_supabaseInstance) return _supabaseInstance;
  
  if (typeof window.supabase === 'undefined') {
    console.error("Supabase SDK is not loaded. Make sure the CDN script tag is present and you have an internet connection.");
    return null;
  }

  const url = window.SUPABASE_URL;
  const key = window.SUPABASE_ANON_KEY;
  
  if (!url || !key || url === 'YOUR_SUPABASE_PROJECT_URL' || key === 'YOUR_SUPABASE_ANON_KEY' || url === '' || key === '') {
    console.error("Supabase credentials are missing or configured with default placeholders in the .env file.");
    return null;
  }
  
  try {
    _supabaseInstance = window.supabase.createClient(url, key);
  } catch (err) {
    console.error("Failed to initialize Supabase client:", err.message);
    return null;
  }
  return _supabaseInstance;
}

// Expose globally so other scripts can access the client instance
window.initSupabase = initSupabase;

// Ensure supabase is initialized
const getClient = () => {
  const client = initSupabase();
  if (!client) {
    throw new Error("Supabase client could not be initialized. Check your credentials.");
  }
  return client;
};

// Authentication Methods exposed globally
window.AuthService = {
  /**
   * Signs up a new user with email, password, and username.
   * Stores the username in user metadata so the database trigger can sync it to profiles.
   */
  async signUp(email, password, username) {
    const client = getClient();
    
    // 1. Sign up the user in Supabase Auth
    const { data, error } = await client.auth.signUp({
      email,
      password,
      options: {
        data: {
          username: username
        }
      }
    });

    if (error) throw error;
    return data;
  },

  /**
   * Logs in a user using email and password.
   */
  async signIn(email, password) {
    const client = getClient();
    const { data, error } = await client.auth.signInWithPassword({
      email,
      password
    });

    if (error) throw error;
    return data;
  },

  /**
   * Logs out the user and clears the session.
   */
  async signOut() {
    const client = getClient();
    const { error } = await client.auth.signOut();
    if (error) throw error;
  },

  /**
   * Sends a password reset email to the user.
   * When they click the link, they are redirected to /reset-password.html.
   */
  async forgotPassword(email) {
    const client = getClient();
    const resetUrl = `${window.location.origin}/reset-password.html`;
    const { data, error } = await client.auth.resetPasswordForEmail(email, {
      redirectTo: resetUrl
    });

    if (error) throw error;
    return data;
  },

  /**
   * Updates the password for the currently active reset session.
   */
  async resetPassword(newPassword) {
    const client = getClient();
    const { data, error } = await client.auth.updateUser({
      password: newPassword
    });

    if (error) throw error;
    return data;
  },

  /**
   * Get the current active session.
   */
  async getCurrentSession() {
    const client = getClient();
    const { data, error } = await client.auth.getSession();
    if (error) return null;
    return data.session;
  },

  /**
   * Retrieves the current user's profile details from the "profiles" table.
   */
  async getUserProfile(userId) {
    const client = getClient();
    const { data, error } = await client.from('profiles')
      .select('*')
      .eq('id', userId)
      .single();
    
    if (error) throw error;
    return data;
  },

  /**
   * Subscribes to auth state changes (e.g. login, logout).
   */
  onAuthStateChange(callback) {
    const client = getClient();
    return client.auth.onAuthStateChange(callback);
  }
};
