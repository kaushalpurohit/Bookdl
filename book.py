class books(dict):
    def __init__(self):
        self.dict = dict()
        self.itr = 1
    
    def add(self,index,title,link):
        self.dict[index] = {}
        self.dict[index]['Title'] = title
        self.dict[index]['Link'] = link
    
    def get_results(self):
        return self.dict
    
    def show_results(self):
        size = len(self.dict)
        last = self.itr + 5
        i = self.itr
        print("\n")
        while i < last:
            try:
                print("[{}].{}".format(i,self.dict[i]['Title']))
            except:
                break
            i += 1
        if(i <= size): print("[0].More")
        self.itr = i

    def get_url(self,i):
        return self.dict[i]['Link']

    def get_title(self,i):
        return self.dict[i]['Title']