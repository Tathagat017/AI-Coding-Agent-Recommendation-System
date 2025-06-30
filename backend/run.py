#!/usr/bin/env python3
"""
Simple script to run both the FastAPI backend and React frontend
"""
import subprocess
import sys
import os
import time
import signal
from pathlib import Path

def check_requirements():
    """Check if required dependencies are installed"""
    try:
        import uvicorn
        import fastapi
        print("✓ Python dependencies found")
    except ImportError as e:
        print(f"✗ Missing Python dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    # Check if node_modules exists
    frontend_path = Path("frontend")
    if not (frontend_path / "node_modules").exists():
        print("✗ Frontend dependencies not found")
        print("Please run: cd frontend && npm install")
        return False
    
    print("✓ Frontend dependencies found")
    return True

def run_servers():
    """Run both backend and frontend servers"""
    if not check_requirements():
        return
    
    print("\n🚀 Starting AI Coding Agent Recommendation System...")
    print("=" * 60)
    
    # Start backend server
    print("Starting FastAPI backend on http://localhost:8000")
    backend_process = subprocess.Popen([
        sys.executable, "backend/main.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait a moment for backend to start
    time.sleep(3)
    
    # Start frontend server
    print("Starting React frontend on http://localhost:5173")
    frontend_process = subprocess.Popen([
        "npm", "run", "dev"
    ], cwd="frontend", shell=True)
    
    print("\n✅ Both servers are starting...")
    print("🌐 Frontend: http://localhost:5173")
    print("🔧 Backend API: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop both servers")
    
    def signal_handler(sig, frame):
        print("\n\n🛑 Shutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Wait for processes
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        backend_process.terminate()
        frontend_process.terminate()

if __name__ == "__main__":
    run_servers() 