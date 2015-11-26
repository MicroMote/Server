from MicroMote import create_app

# TODO make a better launcher
app = create_app()
app.run(host='0.0.0.0', port=8080, debug=True)
