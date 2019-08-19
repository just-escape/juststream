#!/usr/bin/env python

from flask import Flask, Response
from juststream.camera import Camera


def streamer():
    camera = Camera()
    while True:
        frame = camera.get_frame()
        ret = [
            b'--frame',
            b'Content-Type: image/jpeg',
            b'',
            frame,
        ]

        yield b'\r\n'.join(ret)


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def stream():
        r = Response(
            streamer(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
        )
        return r

    return app
