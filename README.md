# AI Coding Agent Recommendation System

A comprehensive system that recommends the best AI coding agent (GitHub Copilot, Cursor, or Replit) for your specific coding tasks using intelligent analysis and scoring algorithms.

## 🚀 Features

- **Natural Language Task Analysis**: Describe your coding task in plain English
- **Intelligent Scoring Algorithm**: Advanced algorithm that analyzes task complexity, type, and requirements
- **Top 3 Recommendations**: Get ranked recommendations with detailed justifications
- **Comprehensive Agent Database**: Detailed information about capabilities, tools, and pricing
- **Modern UI**: Beautiful and responsive React interface with Mantine UI components
- **Real-time Analysis**: Fast API-driven recommendations with detailed explanations

## 🛠 Tech Stack

### Backend

- **FastAPI**: High-performance Python web framework with automatic API documentation
- **Pydantic**: Data validation and serialization
- **Python 3.8+**: Core language
- **Uvicorn**: ASGI server for production-ready performance

### Frontend

- **React 18**: Modern UI library with hooks and functional components
- **TypeScript**: Type-safe JavaScript for better development experience
- **Vite**: Lightning-fast build tool and development server
- **Mantine UI**: Modern React components library with built-in theming
- **Tabler Icons**: Beautiful icon set optimized for Mantine
- **Emotion**: CSS-in-JS library for styling

## 🏗 Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   React Frontend │────▶│  FastAPI Backend │
│   (TypeScript)   │     │    (Python)     │
│   + Mantine UI   │     │  + Pydantic     │
└─────────────────┘     └─────────────────┘
         │                        │
         │                        │
    ┌─────────┐              ┌─────────┐
    │ Tabler  │              │ Agent   │
    │ Icons + │              │Knowledge│
    │Emotion  │              │  Base   │
    └─────────┘              └─────────┘
```

## 🎯 Supported AI Coding Agents

### GitHub Copilot

- **Strengths**: Enterprise-grade security, GitHub integration, multiple AI models (Claude 3.5 Sonnet, GPT-4.1, Gemini 2.0)
- **Best For**: Code completion, review, autonomous development, enterprise workflows
- **Pricing**: Free (limited), Pro ($10/month), Pro+ ($39/month), Business/Enterprise
- **Tools**: Code completion, Copilot Chat, coding agent, code review, pull request summaries

### Cursor

- **Strengths**: Deep codebase understanding, multi-file editing, fast code editor
- **Best For**: Large codebases, complex refactoring, codebase exploration
- **Pricing**: Free tier available, Pro subscription for advanced features
- **Tools**: AI Editor, Composer, chat interface, symbol search, codebase indexing

### Replit

- **Strengths**: Rapid prototyping, instant deployment, no setup required
- **Best For**: Prototypes, education, quick demos, collaborative coding
- **Pricing**: Free tier with limitations, paid plans for advanced features
- **Tools**: Replit Agent, cloud IDE, built-in database, deployment system

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd q2
   ```

2. **Set up Python virtual environment**

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`
   Interactive docs at `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**

   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`

## 📚 API Documentation

### Endpoints

#### `POST /recommend`

Get AI coding agent recommendations based on task description.

**Request Body:**

```json
{
  "description": "Build a React e-commerce website with payment integration",
  "complexity": "medium", // optional
  "project_type": "web_app" // optional
}
```

**Response:**

```json
{
  "recommendations": [
    {
      "name": "Replit",
      "score": 0.97,
      "justification": "Excellent match for your requirements. Perfect for web apps with built-in deployment and database.",
      "strengths": [
        "Fastest prototyping and deployment",
        "No setup required - cloud-based",
        "Natural language app generation",
        "Built-in database and authentication"
      ],
      "use_cases": [
        "Rapid prototyping and MVP development",
        "Educational projects and learning",
        "Quick demos and proof of concepts",
        "Collaborative coding sessions"
      ],
      "pricing": "Free tier with limitations, paid plans for advanced features",
      "tools": [
        "Replit Agent",
        "Cloud IDE",
        "Built-in database",
        "Replit Auth",
        "Deployment system",
        "Collaboration tools"
      ]
    }
  ],
  "task_analysis": {
    "complexity": "medium",
    "project_type": "web_application",
    "workflow": "standard",
    "experience_level": "intermediate"
  }
}
```

#### `GET /agents`

Get information about all available coding agents.

#### `GET /docs`

Interactive API documentation (Swagger UI).

## 🧠 Recommendation Algorithm

The system uses a sophisticated scoring algorithm that considers:

1. **Task Type Analysis**: Web apps, APIs, mobile apps, enterprise applications
2. **Complexity Assessment**: Simple, medium, complex based on keywords and context
3. **Workflow Requirements**: GitHub integration, deployment needs, collaboration
4. **Experience Level**: Beginner, intermediate, advanced
5. **Keyword Matching**: Weighted scoring based on task description keywords
6. **Agent Capabilities**: Matching task requirements with agent strengths

### Scoring Factors

- **Base Score**: 0.5 (starting point)
- **Keyword Matching**: +0.3 weighted by relevance
- **Complexity Matching**: +0.2 if agent handles task complexity
- **Project Type Matching**: +0.2 if agent specializes in project type
- **Use Case Alignment**: +0.15 per matching ideal use case

### Example Scoring

For "Build a React e-commerce website with payment integration":

- **Replit**: 0.97 (web app + rapid deployment keywords)
- **Copilot**: 0.91 (code completion + React keywords)
- **Cursor**: 0.88 (multi-file editing capabilities)

## 🎨 UI Components

The frontend uses **Mantine UI** for a modern, professional interface:

### Key Components

- **Container & Stack**: Layout and spacing
- **Paper & Card**: Content sections with elevation
- **Button & Textarea**: Interactive form elements
- **Badge & ThemeIcon**: Visual indicators and icons
- **Loader**: Loading states with smooth animations
- **Group**: Flexible layout groups

### Features

- **Gradient Header**: Eye-catching purple gradient with brain icon
- **Feature Cards**: Showcasing system capabilities
- **Example Tasks**: Quick-start buttons for common scenarios
- **Professional Results**: Ranked cards with scores and detailed information
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Loading States**: Smooth animations during API calls

## 🔧 Configuration

### Backend Configuration

- **CORS Settings**: Configured for frontend communication
- **Agent Knowledge Base**: Comprehensive database in `AGENT_KNOWLEDGE_BASE`
- **Scoring Weights**: Customizable weights in `RecommendationEngine.keyword_weights`

### Frontend Configuration

- **API Endpoint**: Configured to `http://localhost:8000`
- **Mantine Theme**: Default theme with custom components
- **TypeScript**: Strict type checking enabled

## 🧪 Example Queries

Try these example tasks to see the system in action:

1. **"Build a React e-commerce website with payment integration"**

   - **Result**: Replit (0.97) → Perfect for rapid web app development

2. **"Create a machine learning model for image classification"**

   - **Result**: Copilot (0.9+) → Enterprise-grade AI assistance

3. **"Develop a REST API with authentication and database"**

   - **Result**: Cursor (0.9+) → Multi-file editing and complex architecture

4. **"Fix bugs in existing Python Django application"**

   - **Result**: Cursor (0.95+) → Codebase understanding and debugging

## 🚧 Development

### Project Structure

```
q2/
├── backend/
│   ├── main.py              # FastAPI application & recommendation engine
│   ├── requirements.txt     # Python dependencies
│   └── venv/               # Virtual environment (excluded from git)
├── frontend/
│   ├── src/
│   │   ├── App.tsx         # Main Mantine UI application
│   │   ├── main.tsx        # Entry point with Mantine styles
│   │   └── index.css       # Minimal base styles
│   ├── package.json        # Node.js dependencies
│   └── node_modules/       # Dependencies (excluded from git)
├── .gitignore              # Excludes venv, node_modules, etc.
└── README.md               # This file
```

### Key Files

- **`backend/main.py`**: Complete FastAPI app with agent knowledge base and scoring
- **`frontend/src/App.tsx`**: Single-file React app with all Mantine UI components
- **`.gitignore`**: Comprehensive exclusions for Python and Node.js

### Adding New Agents

1. Update `AGENT_KNOWLEDGE_BASE` in `backend/main.py`
2. Add scoring weights in `RecommendationEngine.keyword_weights`
3. The frontend will automatically display new agents

### Customizing Scoring

Modify the `RecommendationEngine` class methods:

- **`analyze_task()`**: Task analysis logic
- **`calculate_score()`**: Scoring algorithm
- **`generate_justification()`**: Recommendation explanations

## 🔄 Running Both Servers

For full functionality, run both servers simultaneously:

**Terminal 1 (Backend):**

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python main.py
```

**Terminal 2 (Frontend):**

```bash
cd frontend
npm run dev
```

Then visit:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Mantine UI** for the beautiful React components
- **FastAPI** for the excellent Python web framework
- **GitHub Copilot, Cursor, and Replit** for inspiration and agent information
- **Tabler Icons** for the clean, modern icon set

---

**Built with ❤️ for developers choosing the right AI coding assistant.**

_Get personalized recommendations in seconds - describe your task and let our AI find your perfect coding partner!_
