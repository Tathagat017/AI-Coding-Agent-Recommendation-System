# AI Coding Agent Recommendation System

A comprehensive system that recommends the best AI coding agent (GitHub Copilot, Cursor, or Replit) for your specific coding tasks using intelligent analysis and scoring algorithms.

## 🚀 Features

- **Natural Language Task Analysis**: Describe your coding task in plain English
- **Intelligent Scoring Algorithm**: Advanced algorithm that analyzes task complexity, type, and requirements
- **Top 3 Recommendations**: Get ranked recommendations with detailed justifications
- **Comprehensive Agent Database**: Detailed information about capabilities, tools, and pricing
- **Modern UI**: Beautiful and responsive React interface with Tailwind CSS
- **Real-time Analysis**: Fast API-driven recommendations with detailed explanations

## 🛠 Tech Stack

### Backend

- **FastAPI**: High-performance Python web framework
- **Pydantic**: Data validation and serialization
- **Python 3.8+**: Core language
- **Uvicorn**: ASGI server

### Frontend

- **React 18**: Modern UI library
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool and dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful icons
- **Axios**: HTTP client for API calls

## 🏗 Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   React Frontend │────▶│  FastAPI Backend │
│   (TypeScript)   │     │    (Python)     │
└─────────────────┘     └─────────────────┘
         │                        │
         │                        │
    ┌─────────┐              ┌─────────┐
    │Tailwind │              │ Agent   │
    │   CSS   │              │Knowledge│
    └─────────┘              │  Base   │
                             └─────────┘
```

## 🎯 Supported AI Coding Agents

### GitHub Copilot

- **Strengths**: Enterprise-grade, GitHub integration, multiple AI models
- **Best For**: Code completion, review, enterprise workflows
- **Pricing**: Free to $39/month

### Cursor

- **Strengths**: Deep codebase understanding, multi-file editing
- **Best For**: Large codebases, refactoring, exploration
- **Pricing**: Free tier + Pro subscription

### Replit

- **Strengths**: Rapid prototyping, instant deployment, no setup
- **Best For**: Prototypes, education, quick demos
- **Pricing**: Free + paid plans

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd ai-coding-agent-recommender
   ```

2. **Set up Python virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server**
   ```bash
   cd backend
   python main.py
   ```
   The API will be available at `http://localhost:8000`

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
  "description": "Build a React web app with user authentication",
  "complexity": "medium", // optional
  "project_type": "web_app" // optional
}
```

**Response:**

```json
{
  "recommendations": [
    {
      "name": "Copilot",
      "score": 0.85,
      "justification": "Excellent match for your requirements...",
      "strengths": ["Code completion", "GitHub integration"],
      "use_cases": ["Web development", "Team collaboration"],
      "pricing": "Free (limited), Pro ($10/month)",
      "tools": ["Code completion", "Copilot Chat"]
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

## 🎨 UI Components

### Main Components

- **TaskInput**: Task description input with examples
- **RecommendationResults**: Displays ranked recommendations
- **AgentCard**: Showcases individual agent information

### Features

- Responsive design (mobile-first)
- Loading states and animations
- Error handling and user feedback
- Example task suggestions
- Detailed agent comparisons

## 🔧 Configuration

### Backend Configuration

- CORS settings in `backend/main.py`
- Agent knowledge base in `AGENT_KNOWLEDGE_BASE`
- Scoring weights in `RecommendationEngine.keyword_weights`

### Frontend Configuration

- API endpoint in `frontend/src/components/TaskInput.tsx`
- Tailwind config in `frontend/tailwind.config.js`
- TypeScript config in `frontend/tsconfig.json`

## 🧪 Example Queries

Try these example tasks to see the system in action:

1. **"Build a simple todo app with React frontend"**

   - Likely recommends Replit for rapid prototyping

2. **"Create enterprise microservices architecture with security"**

   - Likely recommends Copilot for enterprise features

3. **"Refactor large existing Python codebase for performance"**

   - Likely recommends Cursor for codebase understanding

4. **"Quick prototype for mobile-first web app"**
   - Likely recommends Replit for fast deployment

## 🚧 Development

### Project Structure

```
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── App.tsx          # Main application
│   │   └── App.css          # Styles
│   ├── package.json         # Node.js dependencies
│   └── tailwind.config.js   # Tailwind configuration
└── README.md                # This file
```

### Adding New Agents

1. Update `AGENT_KNOWLEDGE_BASE` in `backend/main.py`
2. Add scoring weights in `RecommendationEngine.keyword_weights`
3. Update frontend components if needed

### Customizing Scoring

Modify the `RecommendationEngine` class methods:

- `analyze_task()`: Task analysis logic
- `calculate_score()`: Scoring algorithm
- `generate_justification()`: Recommendation explanations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- GitHub Copilot documentation and features
- Cursor AI editor capabilities
- Replit platform information
- FastAPI and React communities

---

Built with ❤️ for developers choosing the right AI coding assistant.
