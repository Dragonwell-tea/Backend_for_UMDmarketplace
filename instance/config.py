import os

BASE_URL = "http://localhost"
SQLALCHEMY_DATABASE_URI = "mysql://root:qy123456@localhost/marketplace"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_ALGORITHM = "RS256"
JWT_PRIVATE_KEY='''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAlZX5d8i7z/rwEfGefxYqIh3LFeKnoa0EDU4soBfsOUSf+MMg
/GoHL/ZoATuEvs+w8KRbnFoTVTvfovZ+R8us2qO0rLaaIGflUzAme+3XGN6/Zxzw
XFHY2/ykhGw3nLtafc5lBpZDd7g6nX16zPtvD3TuKZ9jbdKf9zRbSERWHGPB1WFZ
wFbTlk8kvdjID+ktNVpKjD4TNNms6gbL7LaXiKaZZSA2gwy7bNm3XwRKTxonuqAy
iWdThpZasAbdANd4UwrJQdkOcBDcUKvbcONnafscjL697kwJcL7+m4wot80UcbOg
Kd+dkaEtyxGakaCzonDaRgrMzuu/uxCifyksZwIDAQABAoIBAGArWYWPQmAGPs3q
fzHJeDES4nwhihBBgbdkKQCMIMz4t7hhCxX8vL4zNs6EC2X5dRJhOJyetIs5wR+u
RaW25lxynzfi9dgbs6316OgIEx/kJT4PtuBDpp5YIRUZ1e8n7JexV/YSKTIQ+W5D
O+4JQG+5h1yvImd64Gk3+e/OL2Z0KIyJKVd3coGineRCD8UzpPssoWc1CGPLlvj0
iJt4uGj5tfQWbqvl3XqysG0dEJwA3eye2qsVyKRLKQj82V6SThhpHyQcD1LKwGYH
W3A0lmHsQbDGMWgErtwybqX0AqMkIfhK6qw1ftUwvF9L0+ZiBHn+TGzfZg6yZsF4
ib7rg6ECgYEAxGl3xEt4xkEzoF0VFD/9WanEYGo1x9wGjL7GsOWttZGNLgyBCEbh
DdtYHZs5UVxe+jTD5oXsQ+TURC6ZAxqZz+rZIxd7j76lvgR+Og3yclJNf5JjKToO
b8EfU58YEQIToYxTGqDugssHbA3kgTaYrxx5Ds22bRVvBoCYnJ9tLu8CgYEAwve1
GfFYPNbLu1vwxdyo5MV6i6FOhYAAftbuxuB7PjwoHgOR1Vr/CVKPNCdIL3EsP/jo
fUoExA9X7CsLF5Kjm0p83vFkBhgmBDo4MYheS3zvOPzJ7e7JeSmnytI/IcO00wzE
eccC/2sKRahfCQjZjnUPakklRKydojnad/tV2gkCgYBuKxpaqFqeGYRztsJUEXBy
Ep9r1SdFa0zhNUENiEbfSTz/T1Qw6FDkDNxn/uEvmbhMb7xSWVwk2P2XIOwCqbEM
xpX08P8FqdIduzdyKNCM/00o+VtVjJL8bD6+EMbXA2sveh5DGXGvO2J2YXSCZbVO
w5HDk+93UEZuR0NS1rnPUQKBgEfSFCagX07aGWbFcaaRqK3NiV0SaOiIxKX06zTb
0MqWQnj7+6bKxJRck2A08ER5vkE6ofo1YBgRRuQ63vUqEZbNE77U0XHlR2vbPoQQ
phvMxBsMFB7QDevSSntOg+8eNuhgFah+hT4t4jTS119uoSX3PVx74Xyw0cjG4xG7
xl5xAoGBAIVt8TOqNvzSUv5Cj6an7nIsIFUWH+v8q9IpItm1j+cU0OxAVGjy70EB
W94WiTPQtTq0ADm/awT59cb/LZx2TgkdLTvmoaOKDvgBL0O0UNpEo2fNSjAHHKdT
ppdRsmIm4kosf7JYFK7AgT4JMCwlXU+kQKIldFozEjWBqXe7RuLB
-----END RSA PRIVATE KEY-----'''

JWT_PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlZX5d8i7z/rwEfGefxYq
Ih3LFeKnoa0EDU4soBfsOUSf+MMg/GoHL/ZoATuEvs+w8KRbnFoTVTvfovZ+R8us
2qO0rLaaIGflUzAme+3XGN6/ZxzwXFHY2/ykhGw3nLtafc5lBpZDd7g6nX16zPtv
D3TuKZ9jbdKf9zRbSERWHGPB1WFZwFbTlk8kvdjID+ktNVpKjD4TNNms6gbL7LaX
iKaZZSA2gwy7bNm3XwRKTxonuqAyiWdThpZasAbdANd4UwrJQdkOcBDcUKvbcONn
afscjL697kwJcL7+m4wot80UcbOgKd+dkaEtyxGakaCzonDaRgrMzuu/uxCifyks
ZwIDAQAB
-----END PUBLIC KEY-----
'''

COMMENT_COMMENT_PER_PAGE = 10
