from website import createApp

app = createApp()

if __name__ == '__main__':
    app.run("0.0.0.0",port=80,debug=False)