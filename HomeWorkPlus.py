#There's no such thing as private properties on a coffeescript object! But, maybe there are? Implement a function createSecretHolder(secret) which accepts any value as secret and returns an object with ONLY two methods getSecret() which returns the secretsetSecret() which sets the secret obj = createSecretHolder(5) obj.getSecret() # returns 5 obj.setSecret(2) obj.getSecret() # returns 2
class SecretHolder:
    def __init__(self, secret):
        self.__secret = secret
    def getSecret(self):
        return self.__secret
    def setSecret(self, new_secret):
        self.__secret = new_secret
obj = SecretHolder(5)
print(obj.getSecret())
obj.setSecret(2)
print(obj.getSecret())