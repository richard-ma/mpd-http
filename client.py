from mpd import MPDClient


class Client:
    def __init__(self, host: str, port=6600) -> None:
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.idletimeout = None

        self.client.connect(host, port)
    
    def __del__(self) -> None:
        self.client.close()
        self.client.disconnect()

    # control playback
    def next(self) -> None:
        self.client.next()

    def prev(self) -> None:
        self.client.previous()

    def pause(self) -> None:
        self.client.pause()

    def play(self) -> None:
        self.client.play()

    def stop(self) -> None:
        self.client.stop()

    # playlist
    def add(self, uri: str) -> None:
        self.client.add(uri)

    def playlist(self):
        return self.client.playlist()