from src import app

if __name__ == "__main__":
    # db.create_all()
    app.env = "development"
    app.run(debug=True)