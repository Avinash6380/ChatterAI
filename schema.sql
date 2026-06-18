-- =========================================================================
-- SQL Schema for Supabase User Profiles Table (Updated)
-- =========================================================================

-- 1. Create the public profiles table
-- This table stores user profile information and links to Supabase Auth's users table.
CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  provider TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
  CONSTRAINT check_username_format CHECK (username ~ '^[A-Za-z][A-Za-z0-9]*$')
);

-- 2. Enable Row Level Security (RLS)
-- By default, this prevents any unauthorized read/write access.
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- 3. Drop existing policies to avoid duplicates
DROP POLICY IF EXISTS "Allow select for all" ON public.profiles;
DROP POLICY IF EXISTS "Allow users to insert their own records" ON public.profiles;
DROP POLICY IF EXISTS "Allow users to update their own records" ON public.profiles;

-- 4. Create secure RLS Policies
-- Allow anyone to read profiles (e.g. to display usernames in the chat interface)
CREATE POLICY "Allow select for all" 
  ON public.profiles 
  FOR SELECT 
  USING (true);

-- Allow authenticated users to insert their own profile record (matching their auth.users.id)
CREATE POLICY "Allow users to insert their own records" 
  ON public.profiles 
  FOR INSERT 
  WITH CHECK (auth.uid() = id);

-- Allow authenticated users to update only their own profile details
CREATE POLICY "Allow users to update their own records" 
  ON public.profiles 
  FOR UPDATE 
  USING (auth.uid() = id);
