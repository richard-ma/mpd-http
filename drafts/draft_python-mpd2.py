from mpd import MPDClient

client = MPDClient()
client.timeout = 10
client.idletimeout = None

client.connect("192.168.1.100", 6600)

print(client.mpd_version)
print(client.find("any", "蔡依林"))

client.iterate = True
for song in client.playlistinfo():
    print(song["file"])

client.play()

client.close()
client.disconnect()