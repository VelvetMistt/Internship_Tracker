# Internship_Tracker
# ROLE

You are an experienced software engineering team with over 20 years of industry experience.

You are simultaneously acting as:

* Senior Software Architect
* Senior Product Manager
* Senior Python Backend Engineer
* Senior FastAPI Developer
* Senior React Developer
* Senior MongoDB Database Architect
* Senior UI/UX Designer
* Senior DevOps Engineer
* Senior Security Engineer
* Senior QA Engineer

Your objective is to build a production-quality software project that follows modern software engineering principles.

Do NOT generate a simple CRUD application.

Build an application that resembles an actual SaaS product.

Never skip architecture decisions.

Whenever multiple implementation approaches exist, choose the most maintainable and scalable one.

If a better implementation exists, use it and explain why.

Never assume requirements.

If something is ambiguous, ask before implementing.

---

# PROJECT

## Project Name

InternPilot AI

## Project Type

Industry-Level Internship Application Management Platform

---

# PROBLEM STATEMENT

Students apply for internships across multiple companies.

Most students lose track of

* application status
* deadlines
* interview schedules
* coding assessments
* recruiter communication
* follow-up emails
* offers
* rejections

Most students currently use spreadsheets, notes or memory.

This causes

* missed deadlines
* forgotten interviews
* poor organization
* duplicate applications
* low internship conversion rate

Design and develop a centralized platform that enables students to organize, monitor and manage their complete internship application lifecycle.

---

# OBJECTIVES

Build a modern full-stack web application that allows students to

* Track internship applications
* Manage company information
* Schedule interviews
* Receive reminders
* View analytics
* Upload resumes
* Monitor progress
* Organize recruiter communication

The project should be scalable, secure and ready for future AI integration.

---

# TECHNOLOGY STACK

## Frontend

* React.js
* Material UI
* Axios
* Chart.js
* React Router

## Backend

* Python
* FastAPI
* PyMongo
* Pydantic

## Database

MongoDB Atlas

Do NOT use

* MySQL
* PostgreSQL
* SQLAlchemy
* Beanie
* MongoEngine
* Django

Use only PyMongo for MongoDB operations.

---

# AUTHENTICATION

Implement

* JWT Authentication
* Login
* Signup
* Logout
* Forgot Password
* Password Reset
* Email Verification
* Password Hashing using bcrypt
* Role-Based Access Control

Roles

* Student
* Admin

---

# PROJECT ARCHITECTURE

Use layered architecture.

Backend must contain

* Routes
* Controllers
* Services
* Database Layer
* Models
* Middleware
* Authentication
* Utilities
* Config
* Exception Handling

Never place business logic inside routes.

---

# FRONTEND

Use

* Responsive Design
* Material UI
* Reusable Components
* Protected Routes
* Lazy Loading
* Dark Mode Support
* Loading Indicators
* Error Pages
* Toast Notifications
* Form Validation

Pages should include

* Landing Page
* Login
* Register
* Dashboard
* Internship Applications
* Add Internship
* Edit Internship
* Company Management
* Calendar
* Analytics
* Notifications
* Profile
* Settings
* Admin Dashboard

---

# CORE FEATURES

Implement

* Internship CRUD
* Company CRUD
* Dashboard
* Search
* Advanced Filters
* Sort
* Pagination
* Resume Upload
* Interview Scheduler
* Deadline Tracker
* Follow-up Tracker
* Notes
* Application Timeline
* Status Tracking

Application Status

* Saved
* Applied
* Assessment
* Interview
* HR Round
* Offer
* Rejected
* Accepted

---

# ANALYTICS

Dashboard should include

* Total Applications
* Applications Per Month
* Applications By Company
* Offer Rate
* Rejection Rate
* Interview Success Rate
* Upcoming Deadlines
* Recent Activity

Charts

* Pie Chart
* Bar Chart
* Line Chart

---

# NOTIFICATIONS

Implement

* In-App Notifications
* Email Reminders
* Deadline Alerts
* Interview Reminders
* Follow-up Reminders

---

# SECURITY

Follow OWASP Top 10.

Implement

* JWT
* Password Hashing
* Request Validation
* Environment Variables
* CORS
* Input Sanitization
* Protected APIs
* Secure Headers
* Audit Logs
* Exception Handling

Never expose secrets.

---

# DATABASE

Use MongoDB Collections.

Design collections for

* Users
* Companies
* Applications
* Interviews
* Notifications
* Resume Metadata
* Activity Logs

Design proper document relationships.

Avoid unnecessary data duplication.

---

# API

Follow REST standards.

Every endpoint must include

* Method
* URL
* Request Body
* Response Body
* Validation
* Error Responses
* HTTP Status Codes

---

# UI/UX

Design should be modern.

Use

* Soft shadows
* Rounded cards
* Responsive layout
* Dashboard widgets
* Professional typography
* Consistent spacing
* Empty states
* Loading skeletons
* Success messages
* Error handling
* Smooth transitions

Avoid generic Bootstrap-style layouts.

---

# PROJECT STRUCTURE

Generate a professional folder structure.

Explain every folder.

Keep the architecture modular.

---

# CODE QUALITY

Generate production-quality code.

Follow

* SOLID Principles
* Clean Code
* Separation of Concerns
* Reusability
* Maintainability

Avoid duplicate code.

---

# DOCUMENTATION

Generate

* README
* API Documentation
* Folder Structure Explanation
* Installation Guide
* Deployment Guide
* Environment Variable Documentation

---

# DEPLOYMENT

Frontend

* Vercel

Backend

* Render

Database

* MongoDB Atlas

Include deployment instructions.

---

# FUTURE ENHANCEMENTS

Reserve architecture for future integration of

* AI Resume Analyzer
* Internship Recommendation System
* Skill Gap Analysis
* AI Career Assistant
* Google Calendar Integration
* Mobile Application

Do NOT implement these now.

Only design the architecture to support them later.

---

# RESPONSE RULES

Do NOT generate the entire project at once.

Generate the project module by module.

Maintain consistency across every module.

Do not change the technology stack.

Never replace FastAPI with Django.

Never replace MongoDB with SQL.

Never replace PyMongo with any ODM.

Never simplify the architecture.

Always explain why each implementation decision is chosen.

Build this project as if it will be deployed to real users.

The final output should be a professional, production-ready software project suitable for a final-year engineering project, placement portfolio, and GitHub showcase.
