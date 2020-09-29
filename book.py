class books(dict):
    def __init__(self):
        self = dict()
    
    def add(self,index,title,link):
        self[index] = {}
        self[index]['Title'] = title
        self[index]['Link'] = link
    
    def get_results(self):
        return self
    
    def show_results(self,i):
        print(len(self))
        indices = [0, 5, 10,15]
        index = indices[i-1] + 1
        print("\n")
        while index <= indices[i]:
            print("[{}].{}".format(index,self[index]['Title']))
            index += 1
        if(i < 3): print("[0].More")

    def get_url(self,i):
        return self[i]['Link']

    def get_title(self,i):
        return self[i]['Title']