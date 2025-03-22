from app import create_app

print("✅ Reached run.py")  # Debug print

try:
    app = create_app()
    print("✅ App created!")
except Exception as e:
    print(f"❌ Error creating app: {e}")

if __name__ == '__main__':
    print("✅ Running app...")
    app.run(debug=True)
