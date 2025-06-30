from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import re
import json

app = FastAPI(title="AI Coding Agent Recommendation System", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class TaskRequest(BaseModel):
    description: str
    complexity: Optional[str] = None
    project_type: Optional[str] = None
    
class AgentRecommendation(BaseModel):
    name: str
    score: float
    justification: str
    strengths: List[str]
    use_cases: List[str]
    pricing: str
    tools: List[str]

class RecommendationResponse(BaseModel):
    recommendations: List[AgentRecommendation]
    task_analysis: Dict[str, str]

# Agent Knowledge Base
AGENT_KNOWLEDGE_BASE = {
    "Copilot": {
        "capabilities": [
            "Code completion", "Chat assistance", "Code review", "Pull request summaries",
            "Multi-language support", "IDE integration", "GitHub integration", "Agent mode",
            "Coding agent for autonomous development", "Next edit suggestions"
        ],
        "strengths": [
            "Excellent code completion accuracy",
            "Deep GitHub integration",
            "Multiple AI model support (Claude 3.5 Sonnet, GPT-4.1, Gemini 2.0)",
            "Autonomous coding agent capabilities",
            "Code review and security scanning",
            "Wide language support",
            "Enterprise-grade security and compliance"
        ],
        "tools": [
            "Code completion", "Copilot Chat", "Copilot coding agent", "Code review",
            "Pull request summaries", "Copilot Extensions", "GitHub Models",
            "Copilot Edits", "Next edit suggestions", "Windows Terminal integration"
        ],
        "use_cases": [
            "Code completion and suggestions",
            "Code review and security analysis", 
            "Autonomous issue resolution",
            "Multi-file code changes",
            "Learning new languages and frameworks",
            "Debugging and error fixing",
            "Enterprise development workflows"
        ],
        "pricing": "Free (limited), Pro ($10/month), Pro+ ($39/month), Business/Enterprise",
        "ideal_for": ["enterprise", "collaborative", "github_workflow", "security", "code_review"],
        "complexity_handling": ["simple", "medium", "complex"],
        "project_types": ["web_app", "api", "mobile", "desktop", "enterprise", "open_source"]
    },
    "Cursor": {
        "capabilities": [
            "AI-powered code editor", "Multi-file editing", "Codebase understanding",
            "Chat with codebase", "Composer for complex changes", "Fast apply edits",
            "Symbol navigation", "Code generation", "Debugging assistance"
        ],
        "strengths": [
            "Deep codebase understanding and context",
            "Excellent multi-file editing capabilities",
            "Fast and intuitive code editor",
            "Composer for complex multi-step changes",
            "Smart symbol navigation and search",
            "Privacy-focused with local processing options",
            "Advanced prompt engineering capabilities"
        ],
        "tools": [
            "AI Editor", "Composer", "Chat interface", "Symbol search",
            "Multi-file editing", "Codebase indexing", "Smart apply",
            "Debug mode", "Terminal integration", "File tree navigation"
        ],
        "use_cases": [
            "Large codebase navigation and understanding",
            "Complex multi-file refactoring",
            "Code generation and completion",
            "Debugging and problem solving",
            "Learning and exploring new codebases",
            "Privacy-sensitive development",
            "Advanced prompt-based coding"
        ],
        "pricing": "Free tier available, Pro subscription for advanced features",
        "ideal_for": ["large_codebase", "refactoring", "exploration", "privacy", "advanced_prompting"],
        "complexity_handling": ["medium", "complex", "very_complex"],
        "project_types": ["web_app", "api", "desktop", "enterprise", "research"]
    },
    "Replit": {
        "capabilities": [
            "Natural language to app generation", "Full-stack development", "Instant deployment",
            "Collaborative coding", "Multi-language support", "Built-in database",
            "Authentication system", "Agent-based development"
        ],
        "strengths": [
            "Fastest prototyping and deployment",
            "No setup required - cloud-based",
            "Natural language app generation",
            "Built-in database and authentication",
            "Excellent for beginners and rapid prototyping",
            "Strong collaboration features",
            "Integrated deployment pipeline"
        ],
        "tools": [
            "Replit Agent", "Cloud IDE", "Built-in database", "Replit Auth",
            "Deployment system", "Collaboration tools", "Package manager",
            "Version control", "Secret management", "Custom domains"
        ],
        "use_cases": [
            "Rapid prototyping and MVP development",
            "Educational projects and learning",
            "Quick demos and proof of concepts",
            "Collaborative coding sessions",
            "No-code/low-code app development",
            "Instant web app deployment",
            "Hackathons and competitions"
        ],
        "pricing": "Free tier with limitations, paid plans for advanced features",
        "ideal_for": ["prototyping", "education", "beginners", "rapid_deployment", "collaboration"],
        "complexity_handling": ["simple", "medium"],
        "project_types": ["web_app", "prototype", "educational", "mvp", "demo"]
    }
}

# Scoring Algorithm
class RecommendationEngine:
    def __init__(self):
        self.keyword_weights = {
            # Task type keywords
            "web app": {"Replit": 0.9, "Copilot": 0.8, "Cursor": 0.7},
            "website": {"Replit": 0.9, "Copilot": 0.7, "Cursor": 0.6},
            "api": {"Copilot": 0.9, "Cursor": 0.8, "Replit": 0.7},
            "mobile": {"Copilot": 0.8, "Cursor": 0.7, "Replit": 0.6},
            "enterprise": {"Copilot": 0.95, "Cursor": 0.8, "Replit": 0.4},
            "prototype": {"Replit": 0.95, "Copilot": 0.6, "Cursor": 0.5},
            "mvp": {"Replit": 0.9, "Copilot": 0.7, "Cursor": 0.6},
            
            # Complexity indicators
            "simple": {"Replit": 0.9, "Copilot": 0.8, "Cursor": 0.7},
            "complex": {"Cursor": 0.9, "Copilot": 0.9, "Replit": 0.5},
            "large": {"Cursor": 0.95, "Copilot": 0.8, "Replit": 0.4},
            "refactor": {"Cursor": 0.95, "Copilot": 0.8, "Replit": 0.3},
            
            # Workflow keywords
            "github": {"Copilot": 0.95, "Cursor": 0.6, "Replit": 0.5},
            "collaboration": {"Copilot": 0.9, "Replit": 0.8, "Cursor": 0.6},
            "deployment": {"Replit": 0.9, "Copilot": 0.7, "Cursor": 0.6},
            "security": {"Copilot": 0.9, "Cursor": 0.7, "Replit": 0.6},
            
            # Experience level
            "beginner": {"Replit": 0.9, "Copilot": 0.7, "Cursor": 0.5},
            "learning": {"Replit": 0.9, "Copilot": 0.8, "Cursor": 0.6},
            "education": {"Replit": 0.95, "Copilot": 0.7, "Cursor": 0.5},
        }
    
    def analyze_task(self, description: str) -> Dict[str, str]:
        """Analyze the task description to extract key characteristics"""
        description_lower = description.lower()
        
        analysis = {
            "complexity": "medium",
            "project_type": "general",
            "workflow": "standard",
            "experience_level": "intermediate"
        }
        
        # Determine complexity
        if any(word in description_lower for word in ["simple", "basic", "quick", "prototype", "demo"]):
            analysis["complexity"] = "simple"
        elif any(word in description_lower for word in ["complex", "enterprise", "large", "advanced", "production"]):
            analysis["complexity"] = "complex"
        
        # Determine project type
        if any(word in description_lower for word in ["web app", "website", "frontend"]):
            analysis["project_type"] = "web_application"
        elif any(word in description_lower for word in ["api", "backend", "server"]):
            analysis["project_type"] = "api_backend"
        elif any(word in description_lower for word in ["mobile", "app", "android", "ios"]):
            analysis["project_type"] = "mobile_application"
        elif any(word in description_lower for word in ["enterprise", "business"]):
            analysis["project_type"] = "enterprise_application"
        
        # Determine workflow needs
        if any(word in description_lower for word in ["github", "git", "version control"]):
            analysis["workflow"] = "github_integrated"
        elif any(word in description_lower for word in ["deploy", "deployment", "hosting"]):
            analysis["workflow"] = "deployment_focused"
        elif any(word in description_lower for word in ["collaborate", "team", "share"]):
            analysis["workflow"] = "collaborative"
        
        # Determine experience level
        if any(word in description_lower for word in ["beginner", "new", "learning", "first time"]):
            analysis["experience_level"] = "beginner"
        elif any(word in description_lower for word in ["advanced", "expert", "experienced"]):
            analysis["experience_level"] = "advanced"
        
        return analysis
    
    def calculate_score(self, agent_name: str, description: str, analysis: Dict[str, str]) -> float:
        """Calculate a score for an agent based on task description and analysis"""
        base_score = 0.5
        description_lower = description.lower()
        
        # Apply keyword-based scoring
        for keyword, agent_scores in self.keyword_weights.items():
            if keyword in description_lower:
                if agent_name in agent_scores:
                    base_score += agent_scores[agent_name] * 0.3
        
        # Apply analysis-based scoring
        agent_data = AGENT_KNOWLEDGE_BASE[agent_name]
        
        # Complexity matching
        if analysis["complexity"] in agent_data["complexity_handling"]:
            base_score += 0.2
        
        # Project type matching
        if analysis["project_type"] in agent_data.get("project_types", []):
            base_score += 0.2
        
        # Ideal use case matching
        for ideal_case in agent_data.get("ideal_for", []):
            if ideal_case in description_lower:
                base_score += 0.15
        
        return min(1.0, base_score)
    
    def generate_justification(self, agent_name: str, score: float, analysis: Dict[str, str]) -> str:
        """Generate a justification for why this agent was recommended"""
        agent_data = AGENT_KNOWLEDGE_BASE[agent_name]
        
        if score >= 0.8:
            strength = "Excellent"
        elif score >= 0.6:
            strength = "Good"
        else:
            strength = "Moderate"
        
        justification = f"{strength} match for your requirements. "
        
        # Add specific reasons based on analysis
        if analysis["complexity"] == "simple" and agent_name == "Replit":
            justification += "Replit excels at rapid prototyping and simple applications with no setup required. "
        elif analysis["complexity"] == "complex" and agent_name in ["Cursor", "Copilot"]:
            justification += f"{agent_name} handles complex projects well with advanced AI capabilities. "
        
        if analysis["project_type"] == "web_application" and agent_name == "Replit":
            justification += "Perfect for web apps with built-in deployment and database. "
        elif analysis["workflow"] == "github_integrated" and agent_name == "Copilot":
            justification += "Native GitHub integration makes it ideal for GitHub-based workflows. "
        
        return justification.strip()

# Initialize recommendation engine
engine = RecommendationEngine()

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(request: TaskRequest):
    """Get AI coding agent recommendations based on task description"""
    try:
        # Analyze the task
        analysis = engine.analyze_task(request.description)
        
        # Calculate scores for each agent
        recommendations = []
        
        for agent_name, agent_data in AGENT_KNOWLEDGE_BASE.items():
            score = engine.calculate_score(agent_name, request.description, analysis)
            justification = engine.generate_justification(agent_name, score, analysis)
            
            recommendation = AgentRecommendation(
                name=agent_name,
                score=round(score, 2),
                justification=justification,
                strengths=agent_data["strengths"][:4],  # Top 4 strengths
                use_cases=agent_data["use_cases"][:4],  # Top 4 use cases
                pricing=agent_data["pricing"],
                tools=agent_data["tools"][:6]  # Top 6 tools
            )
            recommendations.append(recommendation)
        
        # Sort by score (descending)
        recommendations.sort(key=lambda x: x.score, reverse=True)
        
        # Return top 3 recommendations
        return RecommendationResponse(
            recommendations=recommendations[:3],
            task_analysis=analysis
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/agents")
async def get_all_agents():
    """Get information about all available coding agents"""
    return AGENT_KNOWLEDGE_BASE

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "AI Coding Agent Recommendation System API",
        "version": "1.0.0",
        "endpoints": {
            "/recommend": "POST - Get agent recommendations",
            "/agents": "GET - Get all agent information",
            "/docs": "GET - API documentation"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 