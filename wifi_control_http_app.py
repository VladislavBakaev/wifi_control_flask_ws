from wifi_http_control import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8002)
