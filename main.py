#!/usr/bin/env python3
"""
Main entry point for the Python to C++ code converter application.
"""
from dotenv import load_dotenv

load_dotenv(override=True)


def main():
    """Initialize and launch the code converter application."""
    try:
        from ui.app import CodeConverterApp

        # Create and launch the application
        app = CodeConverterApp()
        app.launch(share=False)  # Set share=True to get a public URL

    except ImportError as e:
        print(f"Error importing required modules: {e}")
        print("Please make sure you have installed all required dependencies.")
        print("Run: pip install -r requirements.txt")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
