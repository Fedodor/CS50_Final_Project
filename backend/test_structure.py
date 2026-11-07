#!/usr/bin/env python
"""
Simple test to verify the project structure and basic imports
"""
import sys
import os

def test_imports():
    """Test that basic imports work"""
    try:
        # Test imports
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        
        # Test basic module imports without running the server
        import src.main
        import src.router
        import src.init
        import src.http_client
        import src.config
        
        print("✓ All modules imported successfully")
        return True
        
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)