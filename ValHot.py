#!/usr/bin/python

import requests
import json
import argparse
import os.path
import urllib.parse

def checkEmailAvailibity(email,salida):
	newFile = open(salida,"a+")
	if "gmail.com" in email:
		host = "https://accounts.google.com/"
		segmentRequest = "_/lookup/accountlookup?hl=es&_reqid=74941&rt=j"
		headers = {
			"Connection": "keep-alive",
			"Content-Length": "2980",
			"X-Same-Domain": "1",
			"DNT": "1",
			"Google-Accounts-XSRF": "1",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 OPR/68.0.3618.56",
			"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
			"Accept": "*/*",
			"Origin": "https://accounts.google.com",
			"Sec-Fetch-Site": "same-origin",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Dest": "empty",
			"Referer": "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
			"Accept-Language": "en-US,en;q=0.9",
			"Cookie": "SEARCH_SAMESITE=CgQIlI8B; CONSENT=YES+PE.es+20170219-14-0; ANID=AHWqTUnx2pfYeY7FK3fbKdXHylUWm3r3saGiwm7DLYanUI3k7Jpgcnjqs0xm0pNZ; 1P_JAR=2020-04-28-20; NID=203=eFmWzz9lhcvYQMdKe2_G4lJaz8SaH_ssrfR-6hUW55ZvtpdlZrDGUdyQiJoG7YCNwf01QXa4eYE6CBxsr5ltM4wHKL431XoA5F_qDEo5uOtf9GubQar-P5jRi3DCjPiXmFFt8tNAJFOtAn68HyG031FL2Au-G19YRv0zwrNElK6sv3n8V0mSFSL0ew; ACCOUNT_CHOOSER=AFx_qI7cgDoWx42TFtU8kqnVHNyH6JRzLhnIuVTTO5uHByXsPPxQAHrfFzSTnjNi4HSMNbLN-ai8; GAPS=1:UDsUl-DNiWXkp3RLyLsxNNMtk7nqYv2c4BkA5virr83-S8_nVpVGiGwHGBiAgyhviEzBnBxwE3nRCm-f_2hwFiF7iTgqKA:pYe3wa4QAh5rysEE; __Host-GAPS=1:UDsUl-DNiWXkp3RLyLsxNNMtk7nqYv2c4BkA5virr83-S8_nVpVGiGwHGBiAgyhviEzBnBxwE3nRCm-f_2hwFiF7iTgqKA:pYe3wa4QAh5rysEE",
			"Host": "accounts.google.com"
		}
		email = urllib.parse.quote_plus(email)

		payload = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&rm=false&ltmpl=default&scc=1&ss=1&osid=1&emr=1&f.req=%5B%22'+email+'%22%2C%22AEThLlwfD64jQqG8RAgRuiZXg1RVqStkmCYpNUYrVFo4ZQK1NHWaK-csJVI9fYvlCNt186KwKsl8Ctdvb_H0Ugzwdje_ZsCnDuxJiDDwOyncdRbuJY-I_V_qKwsqwCj-X5ESZpL_3oGEr_nMwrOS7NKltvdzSKIO7Xxf4a1ZVUto1lJ3JNDdv4Y5vUZcSMsHf17_KtGk4wUm%22%2C%5B%5D%2Cnull%2C%22PE%22%2Cnull%2Cnull%2C2%2Cfalse%2Ctrue%2C%5Bnull%2Cnull%2C%5B2%2C1%2Cnull%2C1%2C%22https%3A%2F%2Faccounts.google.com%2FServiceLogin%3Fservice%3Dmail%26passive%3Dtrue%26rm%3Dfalse%26continue%3Dhttps%253A%252F%252Fmail.google.com%252Fmail%252F%26ss%3D1%26scc%3D1%26ltmpl%3Ddefault%26ltmplcache%3D2%26emr%3D1%26osid%3D1%22%2Cnull%2C%5B%5D%2C4%2C%5B%5D%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%5D%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Ctrue%5D%2C%22'+email+'%22%2Cnull%2Cnull%2Cnull%2Ctrue%2Ctrue%2C%5B%5D%5D&bgRequest=%5B%22identifier%22%2C%22!t7SltJVCYWWmNC8i3e5YrHl-XEqX0ZgCAAABRFIAAABzmQPbj4eAm7kSMZUM2kIcXQ3E-keGu7NFWmMHGofc4CKPBsqvI3huAJAOnrAKXscpgx6at76VRlgcY_4mK2JNjz-oJFP-oiPVXR7IibdPq7n4V_zQNQ9ztxXqLPJ0AhTivxEZNHfs6ZxX1lthmF-g1udMem_5QAIlwjEYrb-NNRZ1Fkm-zPo03_KADRSH126PEmwSr4Lq579fGR-MRHZQHm5ZPyjTs_t4l8FBjxa8xilEviQUwPgrnQ9DkRLQx5uCnfNA23sTMKaIWA9PFWN9MeWu2qi5zA8i5pxxwBOc80J2iXGVTTgRzoozXJTNfQFEQlWnr0AWz6k5Ybe9NDEiNb5_ZSFI-frGQVO-cA1yuMfSyy_ZQd8UdRtR49lg3ZztkxZOTe7lE9PrSWRdHxsxmRVNK2iYb53ai9f9dFiw54Tv1T5QN8grJDRDkXIU7GutX4PGNsaalb77JnIquLkX81l1teNI28jLOhQvtHGUlfNRpforeiLaRtoeUFvOnZPNUMmKAV0BXieJkLo_QP29ohKRI1GZq_vOZffaiGLiagmZEdgkl-tO8f8hHrUNb1x5IMwjDL2xWmTveROLF_NBvzQGhObEHxS9KCzyikVDPG74_8xQ8IWCabSSPm_nLzigqeYeEmm4-3FjAaYgquGiCUXsEHp-EgwqeC8dcM7aIewY3rpur9Y9mBR2JqnfBfw16warSQzKR-TPDPSiPcCMBDgMEhSjiW0uxJ5L5TC1_DZ8HAD8DfQgmmuQWQNzsjvepEnpGxXDqPS3OXpTsD8U6FcVviEnVqxOGX6X1YJ0pkjLEWiExaY_idM8ZvHV06bamdBVIdYMEXZqA0YiU_eDwjc6BmA21pTbaj3A-OLq8ljNK75REIU04UAkOcXQDEH2b-v_dNqx8g3AhaBhz4xAeDsDDlVn1MUtFR1TOd7PBYOaKem-UoDjxKrGHLEaAIfBrroOIBBKkejuiE50K8kaqg_MRdWnzS-tpU7yKQ--ARl5drgAqL7582VQ7w99GEj6VAeNBONn6kb842qvm-9SV-_yznMl1rYQcmY5FcxkNfW_yWWJgLnXU0LwyJ8vEsioQlwE_-3xlbGXBhaHpxLAnGVX1zIWRWbfjoPtEzA6nBEnbW09ie1PKuun1t4v0Nrd2rGo1hSkx_8eqvITPMA-coEGigiXFQ1QwtJGkyjw1zLgru4ZscRqQpbSs1aTzWIyPtclMkZP87eQRNdrge5w7wqedxjFJmknqACMj94q8L62LR3fTMlUbpUuDjgR4MTvMoIGkgr06r1v-6mm9C68-c9vi_2R1Nb-vCE1bWwG%22%5D&azt=AFoagUUzXPqoLDPOMw1FYKVrDXFPAW3gVg%3A1588211294716&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22PE%22%2Cnull%2Cnull%2C%5B%5D%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5D%5D%5D&gmscoreversion=undefined&'

		response = requests.post(host+segmentRequest,data=payload,headers=headers)
		if(response.status_code==200 and "google.com" not in response.text):
			try:
				print("	[*] El correo " + email +  " no existe.\n",end ='')
				newFile.write(email+"\n")
			except Exception as e:
				print(e)
	else:
		host = "https://login.live.com/"
		segmentRequest = "GetCredentialType.srf?opid=78A03330E2A9EDBD&wa=wsignin1.0&rpsnv=13&ct=1559185559&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d5e4def6c-b0e1-ec3f-b70a-6b552fc99466&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&vv=1600&mkt=ES-ES&lc=3082&uaid=c90caf22909a4a519a6e16f0e7ab5c4b"
		headers = {
				"Host": "login.live.com",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
				"Accept": "application/json",
				"Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
				"Accept-Encoding": "gzip, deflate",
				"Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1559185559&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d5e4def6c-b0e1-ec3f-b70a-6b552fc99466&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
				"hpgid": "33",
				"hpgact": "0",
				"client-request-id": "c90caf22909a4a519a6e16f0e7ab5c4b",
				"Content-type": "application/json; charset=utf-8",
				"Content-Length": "623",
				"Connection": "close",
				"Cookie": "logonLatency=LGN01=636947823596154405; optimizelyEndUserId=oeu1559185555590r0.7718000502835731; uaid=c90caf22909a4a519a6e16f0e7ab5c4b; MSPRequ=lt=1559185560&co=1&id=292841; MSCC=179.6.199.210-PE; OParams=11DeRZmdB!3mXw!FLZH8Xx7swmZYOREoDE6bnGCXxDBudvC1q1Ju78hG6dO7PyWsOabcuL0R3rLsoApnjRnmj6URLLqwSLCeXj5!SoFqABIYfj39aRg2FI75rrk5MovRtldYDKYkDLcr5ql3dyXr1seBdCjf4gGYJbYa5yORn!i8hCo5e3Ur!2bGbXS99LH6erxUAOyr6XPPkoNs8PC2aAC8f3SlHcbGtBbCxjuvPBwj2ZD6StS2jRZW6rL2!bbBrzXrf7bAFkNGNi97P68Yg*N5p0k!9cXIL3HadPwy3dkWE*MHyjVKoD53SE88TxviV6aPXuBd65X1XXk5Mcf*SBpcArg4Z*Fv6S0sa94jAFjulU0aULrZuLwNbGuOT0mlG8A!tQvYV9BHEAE9!5lJWwmGsdml!9lysdIe5w5pNA1kbeB!Pi0gNKB80Q1gwgIcsGUc20wBYJTSdlpaknVRtXaJklSPIuXWzo123bWsNbaInWu0XtYFq!euW6!dpCuZTTtg$$; MSPOK=$uuid-206f3139-a763-4e98-a929-68cf04e1cf0e; CkTst=G1559185562765"

			}

		payload = '{"username":"'+email+'","uaid":"c90caf22909a4a519a6e16f0e7ab5c4b","isOtherIdpSupported":true,"checkPhones":true,"isRemoteNGCSupported":true,"isCookieBannerShown":false,"isFidoSupported":false,"forceotclogin":false,"otclogindisallowed":true,"isExternalFederationDisallowed":false,"isRemoteConnectSupported":false,"flowToken":"DRohV1i9th1M6cTTrzUFcKgwmS8kSfWHR*zqeZw3ZEzXMQ0by5Gr0PdKa2u7sEl1kOIXmaHpJAIQbwSYgkOWGtizsGjeTcRSdtLjhuhX*lRN5biHZpmFlInymzPgjljgibTGI8N*92HeHHSOKuEpgec1DeKc5W*J1CF2*rl94rfL!LPz5leiyHm4M8kwWE3h1xPzNy2oUJhXsI2*diPu6PR7cfrl3Yq48qoWyaFG7hd5G2bvFUCdFHV*2I3sFWd0dLPatsO7wMPS0AMcKrHHx60$"}'

		response = requests.post(host+segmentRequest,data=payload,headers=headers)

		if(response.status_code==200):
			json_data = json.loads(response.text)
			try:
				if(json_data['IfExistsResult']==1):
					#Makes sure than this hotmail doens't really exists due to an issue in microsoft validation system
					host = "https://signup.live.com/"
					segmentRequest = "API/CheckAvailableSigninNames?wa=wsignin1.0&rpsnv=13&ct=1588194444&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d6b485324-4e37-9d49-8375-c3ced32dc8fc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C93C7C15B6EEF620&bk=1588194444&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=b700688994474ee1b0fcceef2ea89ee7&username="+email
					headers = {
						"Host": "signup.live.com",
						"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
						"Accept": "application/json",
						"Accept-Language": "en-US,en;q=0.5",
						"Accept-Encoding": "gzip, deflate, br",
						"Referer": "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1588194444&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d6b485324-4e37-9d49-8375-c3ced32dc8fc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C93C7C15B6EEF620&bk=1588194444&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=b700688994474ee1b0fcceef2ea89ee7&username="+email,
						"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
						"canary": "+8TFewobmKpL7wDzVz6tz4I6KxMuxoNiSx6nx/rnUVcDxND3IGXNQCjsi+tRXc7RSENsLh+nQSsz0VpYEdvGyfhgnNdLi3FraIlXDUVfVkhy1xCB5Bj9uIRzLruNPUuCdO0bmdC/N+xLc1l9A9Ch3ped3M2Yvk+lu67xJJZ97bg/xNJT0b/ll8wu+3LtINLyIfyG+Q2qwXRP6WBVDuwH95qITM9l2kmI062jgcytUrjKzqz8aeqF9TX3JUzd24JR:2:3c",
						"x-ms-apiVersion": "2",
						"x-ms-apiTransport": "xhr",
						"uiflvr": "1001",
						"scid": "100118",
						"hpgid": "Signup_MemberNamePage_Client",
						"uaid": "b700688994474ee1b0fcceef2ea89ee7",
						"tcxt": "d5yaVxHVEH4oO36oBQ7fmhaO+678Tr+7jTDOOtcCeoQ9yL0KZniDstnwwikwKnmiEqxPWu2AHi3AAcOyR39gP97EXljvNVeWmTeI1t7c8CKLq/EIqc8cJDDWcwq70mfo11wy3vay8gU5EiZg5Ao3Gt3qLOI90XynuZCKeyZtRFQ8WP99KJYrkvKfEuSi0RgxG1gZN4pc70Ga0GTT0FAoF5vDXUzhnImrOc3XEKEpfpwU88jF+KFh+r48TMHF6/w5MlBrolsGLgZQaFNefudZ+Z0Mihsq08cvSdZGiioAFlb6A7GN6Sws95TBIZGCYSmORLWqPh8LFxHWve/OMk8BhoPMi1tnRJTze2hkA2ZW9lgP5NdbXTLNSDRoWZInd2o6r+NTrj4y2DYPvP6cLEbTojx9rL5bwaIqK03k/D/AL1ut4EXdBGytjJHipw8qXrNGTu1ERITMm6pvy0MaIonVTwQs8Dw171DqswjOyCYwCJVi4/D339IEj9mSdl4NIVBLYeYBolFIK4/rVUtIONY0aLNbjE1rCVws1rCiqjCwE3Y=:2:3",
						"X-Requested-With": "XMLHttpRequest",
						"Content-Length": "175",
						"Origin": "https://signup.live.com",
						"Connection": "keep-alive",
						"Cookie": "optimizelyEndUserId=oeu1579140141434r0.1277099667321795; mkt=en-US; wlidperf=FR=L&ST=1588003572361; MUID=2CD6D00EEA1367AA27AEDE5CEE136472; clrc={%2218382%22%3a[%22+VC+x0R6%22%2c%22d7PFy/1V%22%2c%22fwRyxlqk%22%2c%22P2yuZgWD%22]}; wla42=Ym4xMzAyfGRtMjMwMSoxLEExRTk3MUUyOEVBQTU5RDksMCwsMCwtMSwtMXwxLDdGQTM3QkIxNjRFN0UyMTgsMSwsMCwtMSwtMXwxLDU1NjU4MjU0MjAwOENFMUIsMSwsMCwtMSwtMQ==; logonLatency=LGN01=637237912444749195; mkt1=en-US; amsc=SJL9EylqNlxi3c5wCVGIXMCMXk9EM90RnJkwQX2gYg7zFM3t5jIAQ6Ge5phUhzu+/HmNnIrFUUNXKugZh/yLJgyND3uNwxUiCOUIzSZNGn1PoxvV05eo1mp54zFk6QfleuVzpk6Q8ji1kaW1q7b9RXjNlzeJW1O+wp8rv9OIUuUBGHxD9LAa5H9A9DiJh5Lz/A2LDhrFKCp0pf7/W0TOjNVU/gAQonAw+E8SJY7cx0leQz5koqNuvAD26XHqbimOGPomHZJ99A0T9buCulfNeART0RwCtkj1ceX8nwBX9kObFDpfoX6mcjJ2GB/YVPnm:2:3c",
						"Pragma": "no-cache",
						"Cache-Control": "no-cache",
						"TE": "Trailers"
					}

					payload = '{"signInName":"'+email+'","uaid":"b700688994474ee1b0fcceef2ea89ee7","includeSuggestions":true,"uiflvr":1001,"scid":100118,"hpgid":"Signup_MemberNamePage_Client"}'

					response = requests.post(host+segmentRequest,data=payload,headers=headers)
					if(response.status_code==200):
						json_data = json.loads(response.text)
						try:
							if(json_data['isAvailable'] != False):
								print("	[*] El correo " + email +  " no existe.\n",end ='')
								newFile.write(email+"\n")
						except Exception as e:
							print(e)
			except Exception as e:
				print("Internal Server Error")
		newFile.close()

def validMailtoRequest(mail):
	#El correo solo de puede ser "@hotmail.com","@outlook.com" y "@outlook.es" o "@gmail.com". 
	if(not len(email)>0):
		return False
	if(not "hotmail.com" in email and not "outlook.com" in email and not "outlook.es" in email and not "gmail.com"):
		return False
	return True
def validar_argumentos(args):
	if(args.i == None):
		print("Debe Ingresar un archivo a analizar.")
		return False
	elif(not os.path.exists(args.i) or not os.path.isfile(args.i)):
		print("El archivo a analizar no se ha encontrado.")
		return False
	elif(args.o == None):
		print("Debe Ingresar el nombre del archivo que se asignará al archivo resultante.")
		return False
	else:
		return True

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Ubicación del archivo a analizar.')
parser.add_argument('-o', help='Ubicacion del archivo analizado.(Si ya existe se sobreescribirá)')
argumentos = parser.parse_args()
ingreso = argumentos.i
salida = argumentos.o
if(validar_argumentos(argumentos)):
	file_path = ingreso
	file = open(file_path,"r")
	content_file = file.readlines()
	file.close()
	for email in content_file:
		email=email.strip()
		if(validMailtoRequest(email)):
			print("Verificando Correo : "+email+"\n",end='')
			checkEmailAvailibity(email,salida) 

    
