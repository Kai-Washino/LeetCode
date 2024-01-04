class Solution:
    def isValid(self, s: str) -> bool:
        flag = []
        for char in s:
            if char == '[':        
                flag.append("small")
                # print(flag)
            if char == '{':                
                flag.append("mid")
                # print(flag)
            if char == '(':                            
                flag.append("big")
                # print(flag)

            if char == ']':            
                # print(flag)
                if flag and flag[-1] == "small":
                    flag.pop(-1)
                else:  
                    return False
            if char == '}':                
                # print(flag)
                if flag and flag[-1] == "mid":
                    flag.pop(-1)
                else:  
                    return False                     
            if char == ')':               
                # print(flag)
                if flag and flag[-1] == "big":
                    flag.pop(-1)
                else:  
                    return False
        if not flag :
            return True
        else:
            return False