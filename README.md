**Django Todo List App**

This is a fully functional and beginner-friendly Todo List Web Application built using Django, a high-level Python web framework. It enables users to register, log in, and manage their personal todo items in a secure and intuitive way.

The app supports full CRUD operations (Create, Read, Update, Delete) for todos and includes authentication, user data isolation, and form validation—all wrapped in a clean, responsive UI styled with Bootstrap.


📌 **Features**

✅ User Registration & Authentication - Users can create an account, log in, and securely manage their todos.

✏️ Create, Edit, and Delete Todos - Each authenticated user can add new tasks, edit existing ones, or delete them entirely.

🔒 User-Specific Todo Access - Todos are tied to user accounts. Each user can only access and manage their own list.

🛡️ CSRF Protection - All forms include CSRF tokens, guarding against cross-site request forgery attacks.

📱 Mobile-Responsive UI - Built with Bootstrap for a modern look and feel across all screen sizes.

⚠️ Basic Error Handling & Feedback - Displays validation errors for login/signup forms and highlights missing or incorrect input.



🚀 **Tech Stack Used**

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core programming language      |
| Django     | Backend web framework          |
| SQLite     | Lightweight default database   |
| HTML/CSS   | Template rendering and styling |
| Bootstrap  | Responsive UI components       |



**🔧 How It Works**

User Registration & Login - New users are prompted to sign up. Once registered, they can log in to access their personal todo dashboard.

Todo Management- Logged-in users can create tasks with a title and description. Tasks can be updated or deleted at any time.

User Isolation- The app ensures that each user can only view and modify their own todos—there is no shared access.

Security Measures - Django's built-in authentication system secures login credentials. CSRF tokens protect form submissions.

Error Feedback - The UI provides immediate feedback for invalid credentials, missing fields, or unauthorized actions.


