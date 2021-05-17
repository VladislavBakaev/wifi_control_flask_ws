import subprocess

class WiFiControl():
	def __init__(self):
		self.monitor_cmd = 'nmcli -f ACTIVE,BSSID,SSID,SECURITY d wifi'
		self.del_save_connection_cmd = 'nmcli con del {}'
		self.connect_wifi_pass_cmd = 'nmcli d wifi connect {} password {}'
		self.connect_wifi_non_pass_cmd = 'nmcli d wifi connect {}{}'
		self.save_connection_show_cmd = 'nmcli -f NAME connection show'
		self.get_ip4_cmd = 'nmcli -f IP4 connection show {}'
	
	def get_ip4(self, ssid):
		ip4_list = subprocess.Popen(self.get_ip4_cmd.format(ssid), stdout=subprocess.PIPE, shell=True)
		ip4_list = ip4_list.stdout.read().decode('UTF-8').split('\n')
		ip4 = ip4_list[0].split()[1]
		return ip4


	def get_all_wifi(self):
		name_list = []
		result_list = []
		wifi_list = subprocess.Popen(self.monitor_cmd, stdout=subprocess.PIPE, shell=True)
		wifi_list = wifi_list.stdout.read().decode('UTF-8').split('\n')[1:-1]

		save_connection = subprocess.Popen(self.save_connection_show_cmd, stdout=subprocess.PIPE, shell=True)
		save_connection = save_connection.stdout.read().decode('UTF-8').replace(' ','').split('\n')[1:-1]

		for i,el in enumerate(wifi_list):
			el = el.split()
			if el[2] in name_list:
				continue
			else:
				name_list.append(el[2])

			if (el[0]=="yes"):
				el[0] = "active"
			else:
				el[0] = "non-active"
			
			if (el[3]=='--'):
				el = el[:3] + ['non-password']
			else:
				el = el[:3] + ['password']
			
			if el[2] in save_connection:
				el.append('saved')
			else:
				el.append('non-saved')
			
			if(el[0] == 'active'):
				el.append(self.get_ip4(el[2]))
			else:
				el.append('')
			
			result_list.append(el)
		
		return result_list
	
	def del_save_connection(self, ssid):
		out = subprocess.Popen(self.del_save_connection_cmd.format(ssid), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		out = out.stdout.read().decode().split('\n')

		return out[0]
	
	def wifi_connect(self, ssid, password=''):
		if password == '':
			cmd = self.connect_wifi_non_pass_cmd
		else:
			cmd = self.connect_wifi_pass_cmd
		out = subprocess.Popen(cmd.format(ssid, password), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		out = out.stdout.read().decode().split('\n')
		return out[0]