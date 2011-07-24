# emacs-mode: -*- python-*-
from _Framework.NotifyingControlElement import NotifyingControlElement
#from _Framework.ButtonElement import ButtonElement
#from _Framework.ButtonMatrixElement import ButtonMatrixElement
class SwitchboardElement(NotifyingControlElement):
	__module__ = __name__
	__doc__ = ' Class that connects and disconnects monomodular clients'

	def __init__(self, host, clients):
		#ButtonMatrixElement.__init__(self)
		NotifyingControlElement.__init__(self)
		self._host = host
		self.client_0 = clients[0]
		self.client_1 = clients[1]
		self.client_2 = clients[2]
		self.client_3 = clients[3]
		self.client_4 = clients[4]
		self.client_5 = clients[5]
		self.client_6 = clients[6]
		self.client_7 = clients[7]
		self._client = clients

	def disconnect(self):
		for client in self._client:
			client = None
		self._client = []
		self._send('ping', 'disconnect')
		NotifyingControlElement.disconnect(self)

	def send_swing(self, client, val):
		#self._host._script.log_message('send_swing' + ' ' + str(client) + ' ' + str(val))
		self._host._client[client].receive_swing(val)

	def _send(self, args1 = None, args2 = None, args3 = None, args4 = None):
#		self._button_value(args1, args2, args3, args4)
		for entry in self._value_notifications:
			callback = entry['Callback']
			callback(args1, args2, args3, args4)

	def reset(self):
		pass

#	def _button_value(self, args1 = None, args2 = None, args3 = None, args4 = None):
#		for entry in self._value_notifications:
#			callback = entry['Callback']
#			callback(args1, args2, args3, args4)

	def request_connection(self, device):
		#self._host._script.log_message('request_connection ' + str(device))
		host_num = 8
		for index in range(8):   ##range(len(self._client)):
			if self._client[index]._connected is False:
				self._client[index]._connect_to(device)
				host_num = index
				break
		return host_num
	

	def force_connection(self, device, client_number):
		#self._host._script.log_message('force ' + str(device) + ' ' + str(client_number))
		for client in self._client:
			if client.device == device:
				client._disconnect_client()
		self._client[client_number]._connect_to(device)
		self._send('ping', 'check_connection', client_number)
		return client_number
	

	def connections(self):
		for index in range(8):
			ping = ('ping', 'connection', index, client[index].device)
			return ping



# local variables:
# tab-width: 4
