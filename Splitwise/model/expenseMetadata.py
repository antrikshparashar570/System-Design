class ExpenseMetadata:
    def __init__(self, name, image, url):
        self.name = name
        self.image = image
        self.url = url

        def getName():
            return self.name

        def setName(name):
            self.name = name

        def getImage():
            return self.image

        def setImage(image):
            self.image = image

        def getUrl():
            return self.url

        def setUrl(url):
            self.url = url
