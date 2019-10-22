import json
#json.dumps(payload) 구문확인
data = {'user': {
                        'login': 'test',
                        'firstname': '길동',
                        'lastname': '홍',
                        'mail': '4seeders@test.com',
                        'password': 'pass'
                    }
            }

print (json.dumps(data))