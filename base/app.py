from chatbot.base import app

print("in app")

if __name__ == '__main__':
    app.run(port=5555, threaded=True, debug=True)
