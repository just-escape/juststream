#!/usr/bin/env python

from flask import Flask, Response
from juststream.camera import Camera

app = Flask(__name__)


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


@app.route('/')
def stream():
    r = Response(
        streamer(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )
    return r


if __name__ == '__main__':
    app.run()
