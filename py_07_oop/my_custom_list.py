class ElementDuplicationError (Exception):
    pass


class MyList (list):
    def pop(self):
        return super().pop(0)
    
    # def append(self, __object) -> None:
    #     return super().insert(0, __object)
    def append(self, __object) -> None:
        try:
            if __object in self:
                raise ElementDuplicationError
            
            super().append(__object)
        
        except ElementDuplicationError:
            print("Element is duplicated")
            exit()
    
    def remove(self, __value) -> None:
        if __value not in self: return
        super().remove(__value)
        self.remove(__value)


lst = MyList([1,2,3,4,5,1,2,3,4,5])
lst.pop()
lst.append(1)
lst.remove(5)
print(lst)
