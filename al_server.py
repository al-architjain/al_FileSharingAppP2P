# This the server of the file sharing App
#python3

import socket
import select
import _thread
import sys

class FileServer:
	def __init__(self,port):
		self.port = port
		self.host = socket.gethostname()
		self.ssocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		self.ssocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.ssocket.bind((self.host, self.port))
		self.ssocket.listen(5)
		
		self.peers_list    = []
		self.rfc_list      = []
		self.combined_list = []

	def run(self):
		while True:
			csocket, caddr = self.ssocket.accept()
			



if __name__ == '__main__':
	sobj = FileServer(sys.argv[1])
	sobj.run()
