#!/usr/bin/env python3
"""
Test script to verify the AI Coding Agent Recommendation System works
"""
import requests
import json
import time

def test_api():
    """Test the FastAPI backend"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing AI Coding Agent Recommendation System")
    print("=" * 50)
    
    # Test 1: Root endpoint
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✓ Root endpoint working")
        else:
            print("✗ Root endpoint failed")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to backend. Make sure it's running on localhost:8000")
        return False
    
    # Test 2: Get all agents
    try:
        response = requests.get(f"{base_url}/agents")
        if response.status_code == 200:
            agents = response.json()
            print(f"✓ Agents endpoint working ({len(agents)} agents found)")
        else:
            print("✗ Agents endpoint failed")
            return False
    except Exception as e:
        print(f"✗ Agents endpoint error: {e}")
        return False
    
    # Test 3: Get recommendations
    test_tasks = [
        "Build a simple todo app with React frontend",
        "Create a REST API for a blog with user authentication", 
        "Develop a complex enterprise application with microservices",
        "Build a quick prototype for a mobile-first web app",
        "Refactor a large existing codebase to improve performance"
    ]
    
    print("\n🎯 Testing recommendation engine with sample tasks:")
    
    for i, task in enumerate(test_tasks, 1):
        try:
            response = requests.post(f"{base_url}/recommend", json={
                "description": task
            })
            
            if response.status_code == 200:
                data = response.json()
                recommendations = data["recommendations"]
                top_agent = recommendations[0]["name"]
                score = recommendations[0]["score"]
                print(f"  {i}. Task: '{task[:50]}...'")
                print(f"     → Top recommendation: {top_agent} (score: {score:.2f})")
            else:
                print(f"✗ Recommendation failed for task {i}")
                return False
                
        except Exception as e:
            print(f"✗ Recommendation error for task {i}: {e}")
            return False
    
    print("\n✅ All tests passed! The system is working correctly.")
    print("\n🌐 You can now access:")
    print("   Frontend: http://localhost:5173")
    print("   Backend API: http://localhost:8000")
    print("   API Docs: http://localhost:8000/docs")
    
    return True

def wait_for_backend(max_retries=10):
    """Wait for backend to be ready"""
    print("⏳ Waiting for backend to start...")
    
    for i in range(max_retries):
        try:
            response = requests.get("http://localhost:8000/")
            if response.status_code == 200:
                print("✓ Backend is ready!")
                return True
        except requests.exceptions.ConnectionError:
            if i < max_retries - 1:
                print(f"   Attempt {i+1}/{max_retries}: Backend not ready, waiting...")
                time.sleep(2)
            else:
                print("✗ Backend failed to start after maximum retries")
                return False
    
    return False

if __name__ == "__main__":
    if wait_for_backend():
        test_api()
    else:
        print("\n💡 To start the backend, run: python backend/main.py")
        print("💡 To start the frontend, run: cd frontend && npm run dev") 